import random

# ========== KNOWLEDGE BASE ==========
responses = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning"],
        "replies": [
            "Hello! Welcome to ABC University. How can I help?",
            "Hi there! Ask me anything about our college!"
        ]
    },
    "admission": {
        "keywords": ["admission", "apply", "enroll", "join"],
        "replies": [
            "Admissions open June-August.\nApply online at www.abcuniv.edu\nDocuments: SSC, HSC marksheets, ID proof."
        ]
    },
    "courses": {
        "keywords": ["course", "program", "branch", "department", "study"],
        "replies": [
            "We offer:\n- B.Sc in CSE, EEE, ME, IT\n- MBA\n- BBA / MIS\n- M.Sc Engineering"
        ]
    },
    "fees": {
        "keywords": ["fee", "cost", "tuition", "price"],
        "replies": [
            "Fee Structure:\n- B.Sc Engg: Tk 1,20,000/year\n- MBA: Tk 1,50,000/year\n- BBA: Tk 60,000/year"
        ]
    },
    "placement": {
        "keywords": ["placement", "job", "package", "salary", "company"],
        "replies": [
            "Placement Highlights:\n- 92% placement rate\n- Highest: Tk 25,00,000/year\n- Average: Tk 8,00,000/year\n- Companies: Google, Grameenphone, BRAC IT"
        ]
    },
    "hostel": {
        "keywords": ["hostel", "room", "accommodation", "stay"],
        "replies": [
            "Hostel available for boys & girls.\nAC & Non-AC rooms.\nFee: Tk 50,000/year.\nWiFi, Mess, Gym included."
        ]
    },
    "contact": {
        "keywords": ["contact", "phone", "email", "address"],
        "replies": [
            "Contact Us:\nPhone: +880-2-12345678\nEmail: info@abcuniv.edu\nAddress: Dhanmondi, Dhaka"
        ]
    },
    "scholarship": {
        "keywords": ["scholarship", "financial", "aid"],
        "replies": [
            "Scholarships:\n- Merit: Up to 100% (GPA 5.00)\n- Sports: 50% waiver\n- Need-based financial aid available"
        ]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "exit", "quit", "thanks"],
        "replies": [
            "Goodbye! Have a great day!",
            "Thanks for visiting! All the best!"
        ]
    }
}

def get_response(user_input):
    user_input = user_input.lower()
    for intent, data in responses.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return random.choice(data["replies"])
    return "Sorry, I didn't understand. Ask about admission, courses, fees, or placements."

# ========== CHAT LOOP ==========
print("=" * 40)
print("  EduBot - College Assistant")
print("  Type 'quit' to exit")
print("=" * 40)

while True:
    user = input("\nYou: ")

    if user.lower() in ["quit", "exit", "q"]:
        print("EduBot: Goodbye! 👋")
        break

    reply = get_response(user)
    print(f"EduBot: {reply}")