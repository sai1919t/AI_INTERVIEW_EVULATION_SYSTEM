# interview/question_selector.py

import random
from interview.department_knowledge import DEPARTMENTS

# ==========================================================
# SMART QUESTION ROTATION SYSTEM (Cooldown Based)
# ==========================================================

# Stores previous interview question history per department
INTERVIEW_HISTORY = {}

# Number of previous interviews remembered
COOLDOWN_LIMIT = 5


def select_questions(department, num_questions=10):
    """
    Selects questions for a department with:
    - Smart cooldown rotation
    - No repetition in last N interviews
    - Automatic reset if insufficient questions
    """

    if not department:
        return []

    department = department.upper()

    # Department validation
    if department not in DEPARTMENTS:
        print(f"[ERROR] Department '{department}' not found.")
        return []

    all_questions = DEPARTMENTS[department]

    # If department has no questions
    if not isinstance(all_questions, list) or len(all_questions) == 0:
        print(f"[ERROR] No questions available for {department}")
        return []

    # Initialize history if not exists
    if department not in INTERVIEW_HISTORY:
        INTERVIEW_HISTORY[department] = []

    # -----------------------------------------
    # Collect recent questions (cooldown memory)
    # -----------------------------------------
    recent_questions = set()

    for past_round in INTERVIEW_HISTORY[department]:
        for question_text in past_round:
            recent_questions.add(question_text)

    # -----------------------------------------
    # Filter available questions
    # -----------------------------------------
    available_questions = [
        q for q in all_questions
        if q.get("question") not in recent_questions
    ]

    # -----------------------------------------
    # If not enough remaining → reset cooldown
    # -----------------------------------------
    if len(available_questions) < num_questions:
        available_questions = all_questions
        INTERVIEW_HISTORY[department] = []
        print(f"[INFO] Cooldown reset for {department}")

    # -----------------------------------------
    # Random Selection (No duplicates)
    # -----------------------------------------
    selected_questions = random.sample(
        available_questions,
        min(num_questions, len(available_questions))
    )

    # -----------------------------------------
    # Save to history (Only question text)
    # -----------------------------------------
    selected_texts = [q["question"] for q in selected_questions]
    INTERVIEW_HISTORY[department].append(selected_texts)

    # Maintain cooldown size
    if len(INTERVIEW_HISTORY[department]) > COOLDOWN_LIMIT:
        INTERVIEW_HISTORY[department].pop(0)

    # Debug print (optional)
    print(f"[DEBUG] Selected {len(selected_questions)} questions for {department}")

    return selected_questions