def validate_input(data):
    """
    Validates the input JSON data for the evaluate endpoint.
    Checks if 'user' and 'segments' keys are present.
    """
    if not data:
        return False, "Invalid input. No data provided."
    if 'user' not in data:
        return False, "Invalid input. 'user' key is required."
    if 'segments' not in data:
        return False, "Invalid input. 'segments' key is required."
    return True, None
