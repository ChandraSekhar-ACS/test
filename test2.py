import os

if __name__ == "__main__":
    # Load environment variables from .env file
    from dotenv import load_dotenv
    load_dotenv()

    # Get the GEMINI_API_KEY from environment variables
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if gemini_api_key:
        print("GEMINI_API_KEY loaded.")
    else:
        print("GEMINI_API_KEY not found in environment variables.")
