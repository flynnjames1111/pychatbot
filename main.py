import re
import long_responses as long
import random
import difflib

def advanced_word_similarity(word1, word2, threshold=0.6):
    """
    Calculate similarity between two words using difflib
    
    Args:
        word1 (str): First word to compare
        word2 (str): Second word to compare
        threshold (float): Similarity threshold (0-1)
    
    Returns:
        bool: Whether words are similar enough
    """
    similarity = difflib.SequenceMatcher(None, word1.lower(), word2.lower()).ratio()
    return similarity >= threshold

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    """
    Enhanced message probability calculation with flexible matching
    
    Args:
        user_message (list): List of words in user input
        recognised_words (list): List of words to match against
        single_response (bool): Whether this is a single response scenario
        required_words (list): Words that must be present
    
    Returns:
        int: Probability score (0-100)
    """
    message_certainty = 0
    has_required_words = True

    # Advanced matching: Check for similar words
    for user_word in user_message:
        for rec_word in recognised_words:
            if user_word == rec_word or advanced_word_similarity(user_word, rec_word):
                message_certainty += 1
                break

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words)) if recognised_words else 0

    # Checks that the required words are in the string
    for word in required_words:
        if not any(advanced_word_similarity(word, user_w) for user_w in user_message):
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def preprocess_input(user_input):
    """
    Preprocess user input for more flexible matching
    
    Args:
        user_input (str): Raw user input
    
    Returns:
        list: Processed words
    """
    # Convert to lowercase
    user_input = user_input.lower()
    
    # Remove punctuation
    user_input = re.sub(r'[^\w\s]', '', user_input)
    
    # Split into words
    words = user_input.split()
    
    # Remove common stop words that might not contribute to meaning
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    words = [word for word in words if word not in stop_words]
    
    return words

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Auto Dealership Responses -------------------------------------------------------------------------------------------------------
    response(long.generate_dynamic_response('auto_greetings'), 
             ['hello', 'hi', 'hey', 'sup', 'heyo', 'dealership', 'car', 'vehicle'], single_response=True)
    
    response('See you soon!', ['bye', 'goodbye', 'later'], single_response=True)
    
    # Vehicle Type Queries
    response('Sedans are great for daily commuting and family use.', 
             ['sedan', 'car'], required_words=['sedan'])
    response('SUVs offer versatility and space for families and adventures.', 
             ['suv', 'vehicle'], required_words=['suv'])
    response('Trucks are powerful and perfect for work and heavy-duty tasks.', 
             ['truck', 'vehicle'], required_words=['truck'])
    
    # Buying Process Queries
    response('Let me guide you through our comprehensive buying process.', 
             ['buy', 'purchase', 'process'], required_words=['buy'])
    
    # Financing Queries
    response('We offer multiple financing options to suit your needs.', 
             ['finance', 'loan', 'payment'], required_words=['finance'])
    
    # Maintenance Queries
    response('Regular maintenance is key to keeping your vehicle in top condition.', 
             ['maintain', 'service', 'repair'], required_words=['maintain'])
    
    # Negotiation Queries
    response('Our team is ready to help you get the best deal possible.', 
             ['negotiate', 'price', 'deal'], required_words=['negotiate'])

    # If no high probability match is found
    if not highest_prob_list or max(highest_prob_list.values()) < 50:
        return long.unknown(input_length=len(' '.join(message)))

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return best_match

def get_response(user_input):
    # Preprocess and split user input
    split_message = preprocess_input(user_input)
    
    # Get bot response
    response = check_all_messages(split_message)
    
    # If no good match, use text complexity for more nuanced response
    if response == long.generate_dynamic_response('unknown'):
        response = long.unknown(input_text=user_input)
    
    return response

# Testing the response system
if __name__ == "__main__":
    print("Chat Bot: Type 'quit' to exit")
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            print("Chat Bot: Goodbye!")
            break
        response = get_response(user_input)
        print('Bot:', response)
