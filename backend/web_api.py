from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import subprocess
import uuid

from interview.question_selector import select_questions
from evaluation.speech_to_text import transcribe_audio
from evaluation.knowledge import evaluate_answers
from evaluation.learning_resources import suggest_resources
from interview.department_knowledge import DEPARTMENTS

app = FastAPI()

# ===============================
# CORS CONFIG
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# FOLDERS
# ===============================
os.makedirs("data/web_uploads", exist_ok=True)

INTERVIEW_SESSIONS = {}

# ===============================
# HOME
# ===============================
@app.get("/")
def home():
    return {"message": "AI Interview Web API Running"}

# ===============================
# GET DEPARTMENTS
# ===============================
@app.get("/departments")
def get_departments():
    return {"departments": list(DEPARTMENTS.keys())}

# ===============================
# START INTERVIEW (10 QUESTIONS)
# ===============================
@app.post("/start")
async def start_interview(dept: str = Form(...)):

    # Select 10 questions per interview
    raw_questions = select_questions(dept)[:10]

    questions_only = []

    for item in raw_questions:
        if isinstance(item, tuple):
            questions_only.append(item[0])
        else:
            questions_only.append(item)

    session_id = str(uuid.uuid4())

    INTERVIEW_SESSIONS[session_id] = {
        "questions": raw_questions,   # full (question, answer)
        "dept": dept,
        "videos": []
    }

    return {
        "session_id": session_id,
        "questions": questions_only
    }

# ===============================
# SUBMIT ANSWER
# ===============================
@app.post("/submit")
async def submit_answer(
    session_id: str = Form(...),
    video: UploadFile = File(...)
):

    if session_id not in INTERVIEW_SESSIONS:
        return {"error": "Invalid Session"}

    webm_path = f"data/web_uploads/{uuid.uuid4()}.webm"
    wav_path = webm_path.replace(".webm", ".wav")

    with open(webm_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # Convert to WAV (16kHz for Whisper)
    subprocess.run([
        "ffmpeg", "-y", "-i", webm_path,
        "-ar", "16000",
        wav_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    INTERVIEW_SESSIONS[session_id]["videos"].append({
        "webm": webm_path,
        "wav": wav_path
    })

    return {"status": "Answer received"}

# ===============================
# FINALIZE INTERVIEW
# ===============================
@app.post("/finalize")
def finalize_interview(session_id: str = Form(...)):

    if session_id not in INTERVIEW_SESSIONS:
        return {"error": "Invalid Session"}

    session = INTERVIEW_SESSIONS[session_id]
    questions = session["questions"]
    videos = session["videos"]

    if len(videos) == 0:
        return {"error": "No answers submitted"}

    transcripts = []
    video_files = []

    for v in videos:
        try:
            text = transcribe_audio(v["wav"])
        except:
            text = ""

        # 🔥 Clean Noise
        if not text or len(text.strip()) < 5:
            text = ""

        # Debug (optional)
        print("Transcript:", text)

        transcripts.append(text)
        video_files.append(v["webm"])

    # If user did not speak at all
    if all(t == "" for t in transcripts):
        return {
            "knowledge_score": 0,
            "behavior_score": 0,
            "speech_score": 0,
            "final_score": 0,
            "weak_topics": [],
            "resources": {}
        }

    knowledge_score, behavior_score, speech_score, final_score, weak_topics = evaluate_answers(
        transcripts,
        questions,
        video_files,
        transcripts
    )

    resources = {}
    if final_score < 7:
        resources = suggest_resources(weak_topics)

    return {
        "knowledge_score": knowledge_score,
        "behavior_score": behavior_score,
        "speech_score": speech_score,
        "final_score": final_score,
        "weak_topics": weak_topics,
        "resources": resources
    }