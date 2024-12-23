import re
import math

class TextComplexityAnalyzer:
    @staticmethod
    def calculate_complexity(text):
        """
        Calculate text complexity based on multiple factors
        
        :param text: Input text to analyze
        :return: Complexity score (0-100)
        """
        # Word count complexity
        words = re.findall(r'\w+', text.lower())
        word_count = len(words)
        
        # Unique word ratio
        unique_words = len(set(words))
        unique_word_ratio = unique_words / word_count if word_count > 0 else 0
        
        # Sentence complexity (based on average word length and sentence length)
        sentences = re.split(r'[.!?]+', text)
        avg_sentence_length = sum(len(re.findall(r'\w+', sentence)) for sentence in sentences) / len(sentences) if sentences else 0
        
        # Vocabulary complexity (using average word length as a proxy)
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
        
        # Combine factors with weighted scoring
        complexity = (
            0.3 * min(word_count / 50, 1) +  # Penalize very long texts
            0.2 * unique_word_ratio +  # Reward diverse vocabulary
            0.3 * (avg_sentence_length / 20) +  # Sentence complexity
            0.2 * (avg_word_length / 6)  # Word complexity
        ) * 100
        
        return min(max(complexity, 0), 100)
    
    @staticmethod
    def get_complexity_category(complexity_score):
        """
        Categorize text complexity
        
        :param complexity_score: Complexity score (0-100)
        :return: Complexity category
        """
        if complexity_score < 20:
            return 'simple'
        elif complexity_score < 50:
            return 'moderate'
        elif complexity_score < 75:
            return 'complex'
        else:
            return 'very_complex'
    
    @staticmethod
    def suggest_summarization(text):
        """
        Generate a summarization suggestion based on text complexity
        
        :param text: Input text to analyze
        :return: Summarization suggestion
        """
        complexity = TextComplexityAnalyzer.calculate_complexity(text)
        category = TextComplexityAnalyzer.get_complexity_category(complexity)
        
        suggestions = {
            'simple': "Your message seems straightforward. Could you highlight the key point?",
            'moderate': "That's quite detailed. Could you summarize the main idea?",
            'complex': "Wow, that's a lot of information! Could you break down the core message?",
            'very_complex': "This seems like a comprehensive topic. Could you distill it to its essence?"
        }
        
        return suggestions.get(category, suggestions['complex'])
