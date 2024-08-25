# src/model.py

def generate_meditation(features):
    """
    Generates a personalized meditation session based on input features.
    
    Args:
        features (dict): Processed input features including mood_level and duration_minutes.
        
    Returns:
        str: A string containing the generated meditation session.
    """
    mood_level = features.get('mood_level')
    duration = features.get('duration_minutes')
    
    # Example meditation content generation - customize as needed
    if mood_level == 1:
        mood_phrase = "You are calm and at peace."
    elif mood_level == 2:
        mood_phrase = "Let go of your stress and find tranquility."
    elif mood_level == 3:
        mood_phrase = "Release your anxiety and embrace serenity."
    else:
        mood_phrase = "Find your inner balance."
    
    meditation_script = f"""
    Welcome to your {duration}-minute meditation session.
    
    {mood_phrase}
    
    Close your eyes and take a deep breath...
    
    [Meditation instructions continue here...]
    
    """
    
    return meditation_script.strip()
