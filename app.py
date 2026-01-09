from groq import Groq
from prompts import explain_topic_prompt, revision_notes_prompt, practice_questions_prompt

# Create Groq client
client = Groq(api_key="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")

print("Welcome to AI Study Companion 🤖\n")

topic = input("Enter the topic you want to study: ")

while True:
    # Menu
    print("\nChoose an option:")
    print("1 - Explanation")
    print("2 - Revision Notes")
    print("3 - Practice Questions")
    print("4 - Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        prompt = explain_topic_prompt(topic)
    elif choice == "2":
        prompt = revision_notes_prompt(topic)
    elif choice == "3":
        prompt = practice_questions_prompt(topic)
    elif choice == "4":
        print("Thank you for using AI Study Companion! 🚀")
        break
    else:
        print("Invalid choice. Try again.")
        continue
    
    # AI Call
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    output = response.choices[0].message.content
    print("\nAI Response:\n")
    print(output)

    # Optional: Save to file
    save = input("\nDo you want to save this output to a file? (y/n): ").lower()
    if save == "y":
        filename = f"{topic.replace(' ', '_')}.txt"
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n" + "-"*30 + "\n")
            f.write(output + "\n")
        print(f"Saved to {filename}")
