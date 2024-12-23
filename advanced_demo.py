import main
import text_complexity
import communication_coach

def test_advanced_bot_responses():
    test_inputs = [
        # Short inputs
        "hi",
        "yo",
        
        # Normal inputs
        "hello there",
        "how are you doing?",
        "what's up?",
        
        # Complex inputs with varying complexity
        "can you give me some advice about life and everything?",
        "I'm feeling a bit lost and need some guidance on my career path and personal development",
        
        # Very long and complex inputs
        "I want to discuss the intricate details of artificial intelligence, machine learning, neural networks, deep learning, and how these technologies are transforming our world in ways we could never have imagined just a decade ago, with potential implications for every single industry from healthcare to transportation to education and beyond.",
        
        "Artificial intelligence represents a paradigm shift in computational capabilities, enabling machines to learn from data, recognize patterns, and make decisions with increasing sophistication. The evolution of neural networks and deep learning algorithms has dramatically expanded the potential applications of AI across diverse domains, from predictive analytics in healthcare to autonomous navigation systems in transportation, and from personalized education platforms to advanced robotics in manufacturing.",
        
        # Unrelated inputs
        "blah blah random stuff",
        "asdfghjkl",
        
        # Farewell
        "bye"
    ]
    
    print("Advanced Bot Response Demonstration")
    print("-" * 50)
    print("Complexity Analysis and Communication Coaching Enabled\n")
    
    for user_input in test_inputs:
        print(f"You: {user_input}")
        
        # Show complexity analysis
        complexity = text_complexity.TextComplexityAnalyzer.calculate_complexity(user_input)
        category = text_complexity.TextComplexityAnalyzer.get_complexity_category(complexity)
        print(f"[Complexity: {category.capitalize()} (Score: {complexity:.2f})]")
        
        # Show communication insights
        if len(user_input.split()) > 10:
            insights = communication_coach.CommunicationCoach.analyze_communication_style(user_input)
            print("[Communication Insights]")
            print(f"  Sentence Structure: {insights['sentence_structure']['length_feedback']}")
            print(f"  Vocabulary: {insights['vocabulary']['vocabulary_feedback']}")
        
        # Get bot response
        response = main.get_response(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    test_advanced_bot_responses()
