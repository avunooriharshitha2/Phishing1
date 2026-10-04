print("===== Phishing Email Awareness Simulation =====")

emails = [
    {
        "subject": "URGENT: Your account will be closed!",
        "message": "Click the link immediately to verify your account.",
        "answer": "phishing"
    },
    {
        "subject": "Meeting scheduled for tomorrow",
        "message": "Please attend the department meeting at 10:00 AM.",
        "answer": "safe"
    },
    {
        "subject": "Congratulations! You won a prize!",
        "message": "Click here and provide your password to claim your prize.",
        "answer": "phishing"
    }
]

score = 0

for i, email in enumerate(emails, 1):
    print("\nEmail", i)
    print("Subject:", email["subject"])
    print("Message:", email["message"])

    choice = input("Is this email SAFE or PHISHING? ").lower()

    if choice == email["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print("Correct answer:", email["answer"].upper())

print("\n===== Simulation Completed =====")
print("Your score:", score, "/", len(emails))

if score == len(emails):
    print("Excellent! You can identify phishing emails.")
elif score >= 2:
    print("Good! Keep improving your phishing awareness.")
else:
    print("Be careful with suspicious emails and links.")

print("\nSafety Tips:")
print("1. Do not click suspicious links.")
print("2. Never share passwords through email.")
print("3. Check the sender address carefully.")
print("4. Be careful with urgent or unusual requests.")
