# src/data_processing.py

def process_input(input_data):
    """
    Processes raw input data from the user and converts it into a format suitable for the model.
    
    Args:
        input_data (dict): Dictionary containing user inputs such as mood and time.
        
    Returns:
        dict: Processed features ready for model consumption.
    """
    mood = input_data.get('mood')
    time = input_data.get('time')
    
    # Example processing - you can customize this based on your needs
    mood_levels = {
        "Relaxed": 1,
        "Stressed": 2,
        "Anxious": 3
    }
    
    features = {
        "mood_level": mood_levels.get(mood, 1),
        "duration_minutes": time
    }
    
    return features
