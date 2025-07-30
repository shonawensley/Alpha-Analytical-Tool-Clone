"""
Run script for the Lottery Data Analysis Tool.
"""

import os
import subprocess
import sys

def main():
    """Run the Streamlit application."""
    # Ensure directories exist
    os.makedirs("data/original", exist_ok=True)
    os.makedirs("data/cleaned", exist_ok=True)
    os.makedirs("data/outputs", exist_ok=True)
    
    print("Starting Lottery Data Analysis Tool...")
    
    # Check if Excel file exists in data/original
    excel_files = [f for f in os.listdir("data/original") if f.endswith((".xlsx", ".xlsm"))]
    
    if not excel_files:
        print("No Excel files found in data/original directory.")
        print("You can upload a file through the Streamlit interface.")
    else:
        print(f"Found Excel files in data/original: {', '.join(excel_files)}")
        print("You can select these files in the application.")
    
    # Run the Streamlit app
    cmd = [sys.executable, "-m", "streamlit", "run", "app.py"]
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error running application: {e}")
    
    return True

if __name__ == "__main__":
    main() 