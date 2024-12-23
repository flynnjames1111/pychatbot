class AutoDealershipKnowledge:
    VEHICLE_TYPES = {
        'sedan': ['comfortable', 'fuel-efficient', 'family-friendly'],
        'suv': ['spacious', 'versatile', 'good for families and outdoor activities'],
        'truck': ['powerful', 'work-oriented', 'high towing capacity'],
        'electric': ['eco-friendly', 'low maintenance', 'advanced technology'],
        'hybrid': ['fuel-efficient', 'environmentally conscious', 'lower emissions']
    }

    BUYING_PROCESS_STEPS = [
        "Research vehicles",
        "Determine budget",
        "Check credit score",
        "Get pre-approved financing",
        "Test drive vehicles",
        "Negotiate price",
        "Review contract",
        "Complete purchase"
    ]

    FINANCING_OPTIONS = [
        "Bank loan",
        "Dealership financing",
        "Credit union loan",
        "Manufacturer special financing",
        "Lease options"
    ]

    NEGOTIATION_TIPS = [
        "Know the market value of the vehicle",
        "Get quotes from multiple dealerships",
        "Don't focus only on monthly payments",
        "Be prepared to walk away",
        "Consider total cost of ownership"
    ]

    MAINTENANCE_ADVICE = {
        'frequency': [
            "Regular oil changes",
            "Tire rotation and balance",
            "Brake system check",
            "Battery and electrical system inspection"
        ],
        'importance': [
            "Prevents costly repairs",
            "Maintains vehicle value",
            "Ensures safety",
            "Improves fuel efficiency"
        ]
    }

    @classmethod
    def get_vehicle_recommendations(cls, preferences):
        """
        Provide vehicle recommendations based on user preferences
        
        :param preferences: Dict of user preferences
        :return: List of recommended vehicle types
        """
        recommendations = []
        
        if preferences.get('family_friendly'):
            recommendations.extend(['sedan', 'suv'])
        
        if preferences.get('work_needs'):
            recommendations.append('truck')
        
        if preferences.get('eco_conscious'):
            recommendations.extend(['electric', 'hybrid'])
        
        return list(set(recommendations))

    @classmethod
    def explain_financing(cls, budget=None):
        """
        Provide financing explanation
        
        :param budget: Optional budget to tailor advice
        :return: Financing explanation
        """
        explanation = "Financing Options:\n"
        for option in cls.FINANCING_OPTIONS:
            explanation += f"- {option}\n"
        
        if budget:
            explanation += f"\nConsidering your budget of ${budget}, here are some tailored suggestions:\n"
            # Add budget-specific advice
        
        return explanation

    @classmethod
    def buying_process_guide(cls):
        """
        Provide a comprehensive buying process guide
        
        :return: Step-by-step buying process
        """
        guide = "Auto Buying Process:\n"
        for i, step in enumerate(cls.BUYING_PROCESS_STEPS, 1):
            guide += f"{i}. {step}\n"
        
        return guide

def generate_auto_response(query):
    """
    Generate intelligent responses for auto-related queries
    
    :param query: User's query
    :return: Contextual response
    """
    query = query.lower()
    
    # Vehicle type queries
    for vehicle_type, attributes in AutoDealershipKnowledge.VEHICLE_TYPES.items():
        if vehicle_type in query:
            return f"Looking for a {vehicle_type}? They are known for being {', '.join(attributes)}."
    
    # Process-related queries
    if any(word in query for word in ['buy', 'purchase', 'process']):
        return AutoDealershipKnowledge.buying_process_guide()
    
    # Financing queries
    if any(word in query for word in ['finance', 'loan', 'payment']):
        return AutoDealershipKnowledge.explain_financing()
    
    # Maintenance queries
    if any(word in query for word in ['maintain', 'service', 'repair']):
        return f"Key Maintenance Tips:\n{chr(10).join(AutoDealershipKnowledge.MAINTENANCE_ADVICE['frequency'])}"
    
    # Negotiation queries
    if any(word in query for word in ['negotiate', 'price', 'deal']):
        return f"Negotiation Tips:\n{chr(10).join(AutoDealershipKnowledge.NEGOTIATION_TIPS)}"
    
    return "I can help you with vehicle types, buying process, financing, maintenance, and negotiation. What specific auto-related question do you have?"
