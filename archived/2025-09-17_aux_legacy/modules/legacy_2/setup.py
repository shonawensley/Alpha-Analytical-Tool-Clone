"""
Setup script for the Lottery Data Analysis Tool.
"""

import os
import subprocess
import sys

def main():
    """Install dependencies and set up the application."""
    print("Setting up Lottery Data Analysis Tool...")
    
    # Create required directories
    print("Creating required directories...")
    os.makedirs("data/original", exist_ok=True)
    os.makedirs("data/cleaned", exist_ok=True)
    os.makedirs("data/outputs", exist_ok=True)
    
    # Install requirements
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False
    
    print("\nSetup completed successfully!")
    print("\nTo run the application, use the command:")
    print("    streamlit run app.py")
    print("\nBefore running, make sure to place your Pick3StatsC4.xlsm file in the data/original directory")
    
    return True

if __name__ == "__main__":
    main() 