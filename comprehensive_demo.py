import text_complexity
import communication_coach
import long_responses

def detailed_text_analysis(text):
    print("=" * 50)
    print(f"Text Analysis for: {text}")
    print("=" * 50)
    
    # Complexity Analysis
    complexity = text_complexity.TextComplexityAnalyzer.calculate_complexity(text)
    category = text_complexity.TextComplexityAnalyzer.get_complexity_category(complexity)
    
    print(f"1. Complexity Analysis:")
    print(f"   - Complexity Score: {complexity:.2f}")
    print(f"   - Complexity Category: {category.capitalize()}")
    
    # Communication Insights
    insights = communication_coach.CommunicationCoach.analyze_communication_style(text)
    
    print("\n2. Communication Insights:")
    print(f"   Sentence Structure: {insights['sentence_structure']['length_feedback']}")
    print(f"   Vocabulary Diversity: {insights['vocabulary']['vocabulary_feedback']}")
    
    # Summarization Request
    summarization_suggestion = text_complexity.TextComplexityAnalyzer.suggest_summarization(text)
    
    print("\n3. Summarization Suggestion:")
    print(f"   {summarization_suggestion}")
    
    # Communication Framework
    framework_suggestion = communication_coach.CommunicationCoach.suggest_communication_framework(text)
    
    if framework_suggestion:
        print("\n4. Communication Framework:")
        print(f"   {framework_suggestion}")
    
    # Bot Response
    print("\n5. Bot Response:")
    bot_response = long_responses.unknown(input_text=text)
    print(f"   {bot_response}")
    print("\n")

def main():
    test_texts = [
        # Simple input
        "Hi",
        
        # Moderate input
        "I want to discuss my day",
        
        # Complex input
        "I'm feeling uncertain about my career path and would like some guidance on how to proceed with my professional development",
        
        # Very complex input
        "Artificial intelligence represents a paradigm shift in computational capabilities, enabling machines to learn from data, recognize patterns, and make decisions with increasing sophistication. The evolution of neural networks and deep learning algorithms has dramatically expanded the potential applications of AI across diverse domains, from predictive analytics in healthcare to autonomous navigation systems in transportation, and from personalized education platforms to advanced robotics in manufacturing."
    ]
    
    for text in test_texts:
        detailed_text_analysis(text)

if __name__ == "__main__":
    main()
