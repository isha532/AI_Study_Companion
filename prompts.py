def explain_topic_prompt(topic):
    return f"""
You are a friendly and patient teacher.

Explain the topic "{topic}" in very simple language.
Assume the student is a beginner.

Use:
- short paragraphs
- simple examples if needed
"""

def revision_notes_prompt(topic):
    return f"""
You are an academic tutor.

Create short and clear revision notes for "{topic}".
Use bullet points.
Keep it easy to remember.
"""

def practice_questions_prompt(topic):
    return f"""
You are an exam preparation assistant.

Generate 5 practice questions with answers for the topic "{topic}".
Difficulty level: beginner to intermediate.
"""
