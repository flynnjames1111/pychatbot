import main

def test_bot_responses():
    test_inputs = [
        "hi",
        "hello",
        "hey there",
        "can you give me some advice?",
        "I need help",
        "what do you eat?",
        "do you like food?",
        "blah blah",
        "random stuff",
        "bye"
    ]
    
    print("Bot Response Demonstration")
    print("-" * 40)
    
    for user_input in test_inputs:
        print(f"You: {user_input}")
        response = main.get_response(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    test_bot_responses()
