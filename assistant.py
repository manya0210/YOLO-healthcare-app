health_database = {
    "headache": {
        "home_remedies": "For a headache, try resting in a quiet, dark room, applying a cold compress to the forehead, practicing relaxation techniques like deep breathing or meditation, and staying hydrated."
    },
    "cold": {
        "home_remedies": "For a common cold, get plenty of rest, stay hydrated, use saline nasal sprays or drops to relieve congestion, gargle with warm salt water for a sore throat, and use over-the-counter cold medications as needed for symptom relief."
    },
    "fever": {
        "home_remedies": "For fever, rest in a cool, comfortable environment, drink plenty of fluids, take over-the-counter fever-reducing medications like acetaminophen or ibuprofen, and use cold compresses to help lower body temperature."
    },
    "injury": {
        "home_remedies": "For minor injuries, rest, apply ice to reduce swelling, compress the injured area with a bandage, and elevate the injured limb if possible. Seek medical attention for severe injuries or if symptoms worsen."
    },
    "weakness": {
        "home_remedies": "For weakness, ensure you're getting enough restful sleep, eat a balanced diet rich in vitamins and minerals, stay hydrated, and consider gentle exercises like walking or yoga to improve circulation and energy levels."
    },
    "body pain": {
        "home_remedies": "For body pain, try resting affected areas, applying heat or cold packs, gently massaging sore muscles, taking over-the-counter pain relievers like ibuprofen or acetaminophen, and practicing relaxation techniques such as deep breathing or meditation."
    },
    "period cramps": {
        "home_remedies": "For period cramps, consider applying heat to the lower abdomen with a heating pad or warm towel, practicing gentle exercise like walking or yoga, trying herbal remedies like ginger or chamomile tea, and maintaining good hydration and nutrition."
    },
    "acidity": {
        "home_remedies": "For acidity, try avoiding trigger foods like spicy or acidic foods, eat smaller meals more frequently, avoid lying down after eating, chew gum to increase saliva production, drink plenty of water, and consider natural remedies like ginger tea, baking soda, or apple cider vinegar."
    }
}

def get_response(user_input):
    user_input_lower = user_input.lower()
    if user_input_lower in health_database:
        user_severity = input("Is it a minor issue or something more serious? (minor/serious): ").lower()
        if user_severity == 'minor':
            return f"{user_input}:\nHome Remedies: {health_database[user_input_lower]['home_remedies']}"
        elif user_severity == 'serious':
            return "I recommend consulting with a doctor for proper evaluation and treatment."
        else:
            return "Invalid input. Please enter 'minor' or 'serious'."
    else:
        return "Sorry, I couldn't understand. Could you please specify your health issue?"

def main():
    print("Welcome to the YOLO!!")
    print("Type 'exit' to end the conversation.")
    print("What health issue are you experiencing?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Stay safe and healthy! Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
