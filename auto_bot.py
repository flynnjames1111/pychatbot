import re
import random

class AutoDealershipBot:
    def __init__(self):
        self.knowledge_base = {
            'vehicle_types': {
                'sedan': ['comfortable', 'fuel-efficient', 'family-friendly'],
                'suv': ['spacious', 'versatile', 'good for families'],
                'truck': ['powerful', 'work-oriented', 'high towing capacity']
            },
            'buying_process': [
                'Research vehicles',
                'Determine budget',
                'Check financing options',
                'Test drive',
                'Negotiate price',
                'Complete purchase'
            ],
            'negotiation_tips': [
                'Know the market value',
                'Get multiple quotes',
                'Don\'t focus only on monthly payments',
                'Be prepared to walk away'
            ]
        }
        
        self.response_templates = {
            'greeting': [
                "Welcome to our Auto Dealership Assistant! How can I help you find your perfect vehicle?",
                "Hello! Ready to explore our vehicle lineup? What are you looking for?"
            ],
            'farewell': [
                "Drive safely and hope to see you soon at our dealership!",
                "Thank you for choosing our dealership. Your dream car awaits!"
            ]
        }

    def calculate_text_complexity(self, text):
        """Simple text complexity calculation"""
        word_count = len(re.findall(r'\w+', text.lower()))
        unique_words = len(set(re.findall(r'\w+', text.lower())))
        
        complexity = (
            0.5 * (word_count / 20) +  # Word count impact
            0.5 * (unique_words / word_count)  # Vocabulary diversity
        ) * 100
        
        return min(max(complexity, 0), 100)

    def generate_response(self, query):
        """Generate contextual responses based on query"""
        query = query.lower()
        
        # Greeting
        if any(word in query for word in ['hello', 'hi', 'hey']):
            return random.choice(self.response_templates['greeting'])
        
        # Farewell
        if any(word in query for word in ['bye', 'goodbye', 'later']):
            return random.choice(self.response_templates['farewell'])
        
        # Vehicle Type Queries
        for vehicle, attributes in self.knowledge_base['vehicle_types'].items():
            if vehicle in query:
                return f"Looking for a {vehicle}? They are known for being {', '.join(attributes)}."
        
        # Buying Process
        if any(word in query for word in ['buy', 'purchase', 'process']):
            return "Buying Process Steps:\n" + "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.knowledge_base['buying_process']))
        
        # Negotiation Tips
        if any(word in query for word in ['negotiate', 'price', 'deal']):
            return "Negotiation Tips:\n" + "\n".join(f"- {tip}" for tip in self.knowledge_base['negotiation_tips'])
        
        # Complexity-based response for complex queries
        complexity = self.calculate_text_complexity(query)
        if complexity > 70:
            return "Your query seems complex. Could you break it down into key points?"
        
        # Default response
        return "I specialize in auto dealership topics. Could you rephrase your automotive question?"

def main():
    bot = AutoDealershipBot()
    print("Auto Dealership Chat Bot")
    print("Type 'bye' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'bye':
            print("Bot: Drive safely! Hope to see you at our dealership soon.")
            break
        
        response = bot.generate_response(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
