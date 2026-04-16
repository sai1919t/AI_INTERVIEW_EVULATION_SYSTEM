from flask import Flask, render_template, request, session
from interview.question_selector import select_questions
from evaluation.final_evaluation import evaluate_all
from evaluation.learning_resources import suggest_resources
import os
import uuid
import subprocess

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

app.secret_key = "smart_interview_secret_key"
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB

UPLOAD_FOLDER = os.path.abspath("uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

NUM_QUESTIONS = 10


# -------------------------------------------------
# HOME
# -------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------------------------
# START INTERVIEW
# -------------------------------------------------
@app.route("/start", methods=["POST"])
def start_interview():

    dept = request.form.get("department", "").upper()
    questions = select_questions(dept, num_questions=NUM_QUESTIONS)

    if not questions:
        return f"No questions found for department: {dept}"

    session["questions"] = questions
    session["department"] = dept

    return render_template(
        "interview.html",
        department=dept,
        questions=questions
    )


# -------------------------------------------------
# SAFE VIDEO CONVERSION
# -------------------------------------------------
def convert_webm_to_mp4(input_path):

    output_path = input_path.replace(".webm", ".mp4")

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        output_path
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("FFMPEG ERROR:")
        print(result.stderr)
        return None

    if not os.path.exists(output_path):
        print("MP4 file was not created!")
        return None

    return output_path


# -------------------------------------------------
# SUBMIT INTERVIEW
# -------------------------------------------------
@app.route("/submit", methods=["POST"])
def submit():

    department = session.get("department", "")
    questions = session.get("questions", [])

    if not questions:
        return "Error: Questions not found in session."

    user_answers = []
    transcripts = []

    # -------- SAVE VIDEO --------
    video = request.files.get("full_session_video")

    if not video:
        return "Error: No video uploaded."

    webm_filename = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.webm")
    video.save(webm_filename)

    print("Saved WEBM:", webm_filename)
    print("WEBM exists:", os.path.exists(webm_filename))

    video_path = convert_webm_to_mp4(webm_filename)

    print("Converted MP4:", video_path)
    print("MP4 exists:", os.path.exists(video_path) if video_path else "No MP4")

    if not video_path:
        return "Error: Video conversion failed."

    # -------- COLLECT ANSWERS --------
    for i in range(1, NUM_QUESTIONS + 1):
        answer = request.form.get(f"answer{i}", "").strip()
        user_answers.append(answer)
        transcripts.append(answer)

    # -------- EVALUATE --------
    avg_k, avg_s, avg_b, final_score, weak_topics, verdict = evaluate_all(
        user_answers,
        questions,
        video_path,
        transcripts
    )

    # -------- SUGGEST RESOURCES --------
    resources = []
    if final_score < 7:
        resources = suggest_resources(department, weak_topics)

    return render_template(
        "result.html",
        department=department,
        domain_score=round(avg_k, 2),
        speech_score=round(avg_s, 2),
        behaviour_score=round(avg_b, 2),
        total_score=round(final_score, 2),
        verdict=verdict,
        weak_topics=weak_topics,
        resources=resources
    )


# -------------------------------------------------
# RUN SERVER
# -------------------------------------------------
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)