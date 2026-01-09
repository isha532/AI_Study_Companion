import streamlit as st
from groq import Groq
from prompts import explain_topic_prompt, revision_notes_prompt, practice_questions_prompt

# Groq client
client = Groq(api_key="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")

st.title("🤖 AI Study Companion")

# Input topic
topic = st.text_input("Enter topic:")

# Feature selection
feature = st.radio(
    "Choose feature:",
    ("Explanation", "Revision Notes", "Practice Questions")
)

# Run AI when button clicked
if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic!")
    else:
        # Select prompt
        if feature == "Explanation":
            prompt = explain_topic_prompt(topic)
        elif feature == "Revision Notes":
            prompt = revision_notes_prompt(topic)
        else:
            prompt = practice_questions_prompt(topic)

        # Call AI
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        # Display output
        st.subheader("AI Output")
        st.write(output)

        # Option to save
        if st.button("Save Output"):
            filename = f"{topic.replace(' ', '_')}.txt"
            with open(filename, "a", encoding="utf-8") as f:
                f.write("\n" + "-"*30 + "\n")
                f.write(output + "\n")
            st.success(f"Saved to {filename}")
