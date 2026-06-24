import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url: str) -> str:
    """
    Extracts the 11-character YouTube video ID using Regular Expressions.
    """
    pattern = r'(?:v=|\/v\/|youtu\.be\/|\/embed\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_video_transcript(video_id: str) -> str:
    """
    Fetches the raw transcript data using the modern instance-based .fetch() method
    and reads attributes directly from the FetchedTranscriptSnippet dataclass.
    """
    try:
        # 1. Create an instance of the API class
        api_instance = YouTubeTranscriptApi()
        
        # 2. Fetch the transcript data for the video ID
        transcript_data = api_instance.fetch(video_id, languages=['en'])
        
        # 3. Modern Property Syntax: Use entry.text instead of entry['text']
        full_transcript = " ".join([entry.text for entry in transcript_data])
        return full_transcript
        
    except Exception as err:
        raise Exception(f"YouTube Transcript Error: {str(err)}")