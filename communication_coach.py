import re
import math
import random
import text_complexity

class CommunicationCoach:
    @staticmethod
    def analyze_communication_style(text):
        """
        Analyze the communication style and provide constructive feedback
        
        :param text: Input text to analyze
        :return: Dictionary with communication insights
        """
        # Complexity analysis
        complexity = text_complexity.TextComplexityAnalyzer.calculate_complexity(text)
        category = text_complexity.TextComplexityAnalyzer.get_complexity_category(complexity)
        
        # Sentence structure analysis
        sentences = re.split(r'[.!?]+', text)
        avg_sentence_length = sum(len(re.findall(r'\w+', sentence)) for sentence in sentences) / len(sentences)
        
        # Vocabulary analysis
        words = re.findall(r'\w+', text.lower())
        unique_words = len(set(words))
        word_diversity_ratio = unique_words / len(words) if words else 0
        
        # Communication style insights
        insights = {
            'complexity': {
                'score': complexity,
                'category': category
            },
            'sentence_structure': {
                'avg_length': avg_sentence_length,
                'length_feedback': (
                    "Your sentences are concise." if avg_sentence_length < 10 else
                    "Try breaking down long sentences." if avg_sentence_length > 20 else
                    "Your sentence length is balanced."
                )
            },
            'vocabulary': {
                'diversity_ratio': word_diversity_ratio,
                'vocabulary_feedback': (
                    "Great vocabulary diversity!" if word_diversity_ratio > 0.5 else
                    "Consider using more varied language." if word_diversity_ratio < 0.3 else
                    "Your vocabulary is reasonably diverse."
                )
            }
        }
        
        return insights
    
    @staticmethod
    def generate_communication_guidance(text):
        """
        Generate specific guidance to improve communication
        
        :param text: Input text to analyze
        :return: Constructive communication advice
        """
        insights = CommunicationCoach.analyze_communication_style(text)
        
        guidance_templates = [
            # Complexity-based guidance
            {
                'condition': insights['complexity']['category'] == 'very_complex',
                'advice': [
                    "Your message is quite complex. Could you break it down into key points?",
                    "I'm sensing a lot of depth. Would you mind highlighting the main idea?",
                    "That's a comprehensive perspective. Can you distill it to its core message?"
                ]
            },
            {
                'condition': insights['complexity']['category'] == 'complex',
                'advice': [
                    "Your message has layers. What's the primary point you want to convey?",
                    "Interesting thoughts! Could you summarize the key takeaway?",
                    "I see multiple ideas here. Which one would you like to focus on?"
                ]
            },
            
            # Sentence structure guidance
            {
                'condition': insights['sentence_structure']['avg_length'] > 20,
                'advice': [
                    f"{insights['sentence_structure']['length_feedback']} Try using shorter, clearer sentences.",
                    "Long sentences can be hard to follow. Consider breaking them up.",
                    "Aim for clarity: shorter sentences often communicate ideas more effectively."
                ]
            },
            
            # Vocabulary guidance
            {
                'condition': insights['vocabulary']['diversity_ratio'] < 0.3,
                'advice': [
                    f"{insights['vocabulary']['vocabulary_feedback']} Experiment with more descriptive words.",
                    "Varied language can make your communication more engaging.",
                    "Try using synonyms to add depth to your expression."
                ]
            }
        ]
        
        # Select first matching guidance
        for guidance in guidance_templates:
            if guidance['condition']:
                return random.choice(guidance['advice'])
        
        # Default guidance
        return "Your message is clear. What specific aspect would you like to discuss?"
    
    @staticmethod
    def suggest_communication_framework(text):
        """
        Suggest a communication framework for organizing thoughts
        
        :param text: Input text to analyze
        :return: Structured communication suggestion
        """
        frameworks = [
            "Consider using the STAR method: Situation, Task, Action, Result",
            "Try the 5W1H framework: Who, What, When, Where, Why, How",
            "Organize your thoughts: Context, Problem, Solution, Benefits",
            "Break down your message: Main Idea, Supporting Points, Conclusion"
        ]
        
        complexity = text_complexity.TextComplexityAnalyzer.calculate_complexity(text)
        
        if complexity > 75:
            return f"Your message is quite complex. {random.choice(frameworks)}"
        
        return None
