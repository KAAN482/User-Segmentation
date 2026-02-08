def validate_input(data):
    """
    Validates the input JSON data for the evaluate endpoint.
    Checks if 'user' and 'segments' keys are present.
    
    Args:
        data (dict): The JSON data received from the request.
        
    Returns:
        tuple: (bool, str|None) - True if valid, False and error message if invalid.
    """
    # Check if data exists
    if not data:
        return False, "Invalid input. No data provided."
    
    # Check for 'user' key
    if 'user' not in data:
        return False, "Invalid input. 'user' key is required."
    
    # Check for 'segments' key
    if 'segments' not in data:
        return False, "Invalid input. 'segments' key is required."
        
    return True, None
