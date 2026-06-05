import os
import sys
import subprocess

# Local environment configuration mapping
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def handler(request, response):
    """
    Vercel Serverless Entrypoint Wrapper for Streamlit Framework
    """
    try:
        # Triggering the internal Streamlit execution runtime pipeline
        subprocess.Popen([
            "streamlit", "run", "chatbot_app.py", 
            "--server.port", "8501", 
            "--server.address", "0.0.0.0",
            "--server.headless", "true"
        ])
        return {
            "statusCode": 200,
            "body": "Quantum FAQ Core Bootstrap Initiated. Fetching client nodes..."
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Bootstrap Glitch Matrix: {str(e)}"
        }