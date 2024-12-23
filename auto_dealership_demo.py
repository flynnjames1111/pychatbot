import sys
sys.path.append('.')

import main
import long_responses as long
import auto_dealership_knowledge as auto_dealer

def simulate_interactions():
    print("Auto Dealership Chat Bot Demo")
    print("Simulating interactions to showcase bot capabilities\n")
    
    interactions = [
        "hello",
        "I want to buy a sedan",
        "what financing options do you have?",
        "tell me about truck maintenance",
        "how do I negotiate a good price?",
        "bye"
    ]
    
    for user_input in interactions:
        print(f"You: {user_input}")
        
        # First try auto-specific response
        auto_response = auto_dealer.generate_auto_response(user_input)
        if auto_response != "I can help you with vehicle types, buying process, financing, maintenance, and negotiation. What specific auto-related question do you have?":
            print(f"Bot: {auto_response}\n")
            continue
        
        # Fallback to main response mechanism
        response = main.check_all_messages(user_input.split())
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    simulate_interactions()
