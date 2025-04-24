# List of states (excluding Georgia and West Virginia)
STATES = [
    "Connecticut4", "Delaware4", "Florida4", "Indiana4",
    "Michigan4", "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4",
    "OntarioCanada4", "Pennsylvania4", "PuertoRico4", "SouthCarolina4", 
    "TriState4", "Virginia4"
]

def get_state_display_name(state_name):
    """Convert state sheet name to display format (e.g., "Connecticut4" -> "Connecticut")"""
    # Remove the trailing "4"
    if state_name.endswith("4"):
        return state_name[:-1]
    return state_name

def get_state_file_name(state_name):
    """Ensure state name has the correct format for file naming"""
    # Make sure it ends with "4" for the file
    if not state_name.endswith("4"):
        return f"{state_name}4"
    return state_name 