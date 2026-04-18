from flask import Flask, render_template, request, session, redirect, url_for
from interview.question_selector import select_questions
from evaluation.final_evaluation import evaluate_all
from evaluation.learning_resources import suggest_resources
from database import init_db, register_user, validate_user, save_results, get_last_result
import os
import uuid
import subprocess
import glob

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

app.secret_key = "smart_interview_secret_key"

UPLOAD_FOLDER = os.path.abspath("uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

NUM_QUESTIONS = 10

# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html", logged_in=("user" in session))

# -----------------------------
# DASHBOARD
# -----------------------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    last_result = get_last_result(session["user"])

    return render_template(
        "dashboard.html",
        last_result=last_result
    )

# -----------------------------
# ABOUT PAGE
# -----------------------------
@app.route("/about")
def about():
    return render_template("about.html")

# -----------------------------
# RESOURCES PAGE
# -----------------------------
@app.route("/resources")
def resources():
    return render_template("resources.html")

# -----------------------------
# SIGNUP
# -----------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password != confirm:
            return "Passwords do not match"

        if not register_user(email, password):
            return "User already exists"

        return redirect(url_for("login"))

    return render_template("signup.html")

# -----------------------------
# LOGIN  ✅ FIXED HERE
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if validate_user(email, password):
            session["user"] = email
            return redirect(url_for("home"))

        return "Invalid credentials"

    return render_template("login.html")

# -----------------------------
# LOGOUT
# -----------------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

# -----------------------------
# START INTERVIEW
# -----------------------------
@app.route("/start", methods=["POST"])
def start_interview():

    if "user" not in session:
        return redirect(url_for("login"))

    dept = request.form.get("department", "").upper()
    questions = select_questions(dept, num_questions=NUM_QUESTIONS)

    if not questions:
        return "No questions found"

    session["questions"] = questions
    session["department"] = dept

    return render_template(
        "interview.html",
        department=dept,
        questions=questions
    )

# -----------------------------
# VIDEO CONVERSION
# -----------------------------
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
        print("FFMPEG ERROR:\n", result.stderr)
        return None

    if not os.path.exists(output_path):
        print("MP4 file not created!")
        return None

    return output_path



def clean_old_videos(folder, max_files=10):
    files = glob.glob(os.path.join(folder, "*"))
    
    # Sort by creation time (oldest first)
    files.sort(key=os.path.getctime)

    # Delete extra files
    while len(files) > max_files:
        try:
            os.remove(files[0])
            print("Deleted old file:", files[0])
            files.pop(0)
        except:
            break
# -----------------------------
# SUBMIT INTERVIEW
# -----------------------------
@app.route("/submit", methods=["POST"])
def submit():

    if "user" not in session:
        return redirect(url_for("login"))

    department = session.get("department", "")
    questions = session.get("questions", [])

    if not questions:
        return "Session expired. Restart interview."

    # ---------------- VIDEO ----------------
    video = request.files.get("full_session_video")

    video_path = None  # ✅ ALWAYS DEFINE
    clean_old_videos(UPLOAD_FOLDER , max_files=10)  # Clean old videos before saving new one

    if video and video.filename != "":
        webm_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}.webm")
        video.save(webm_path)

        print("Saved WEBM:", webm_path)

        video_path = convert_webm_to_mp4(webm_path)

        print("Converted MP4:", video_path)

    # ---------------- ANSWERS ----------------
    user_answers = []
    transcripts = []

    for i in range(1, NUM_QUESTIONS + 1):
        ans = request.form.get(f"answer{i}", "").strip()
        user_answers.append(ans)
        transcripts.append(ans)

    # ---------------- SAFE EVALUATION ----------------
    try:
        avg_k, avg_s, avg_b, final_score, weak_topics, verdict = evaluate_all(
            user_answers,
            questions,
            video_path,   # can be None now
            transcripts
        )
    except Exception as e:
        print("Evaluation Error:", e)

        # fallback → only knowledge score
        avg_k = 5
        avg_s = 5
        avg_b = 5
        final_score = 5
        weak_topics = []
        verdict = "Evaluation Partial (Video Failed)"

    # ---------------- RESOURCES ----------------
    resources = []
    if final_score < 7:
        resources = suggest_resources(department, weak_topics)
    save_results(session["user"], final_score, verdict)
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
# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    init_db()
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000)