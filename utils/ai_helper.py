import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_summary(transcript_text: str, summary_format: str) -> str:
    """
    Sends the raw transcript to Groq's FREE developer engine.
    Dynamically adjusts instructions based on the user's preferred format choice.
    """
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise Exception("Groq API Key not found in environment! Please check your .env file spelling.")
        
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key
    )
    
    # --- Guardrail ---
    words = transcript_text.split()
    if len(words) > 3500:
        transcript_text = " ".join(words[:3500]) + "... [Transcript truncated for length analysis]"
    
    # --- Dynamic Prompt Engineering ---
    if summary_format == "Bullet Points":
        system_instruction = "You are an expert content summarizer. Take the raw video transcript and break it down into 5-6 clear, high-impact bullet points capturing the core takeaways."
    elif summary_format == "Action Items":
        system_instruction = "You are an expert project manager. Analyze the transcript and extract an actionable list of key steps, tasks, or lessons learned that the viewer can apply immediately."
    else:
        # Default Paragraph format
        system_instruction = "You are an expert content summarizer. Take the following raw video transcript and provide a short, accurate 3-4 sentence paragraph summary."
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": f"Transcript:\n{transcript_text}"}
            ],
            temperature=0.5
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"AI Engine Error: {str(e)}")