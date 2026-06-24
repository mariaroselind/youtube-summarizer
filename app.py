import streamlit as st
from utils.youtube_helper import extract_video_id, get_video_transcript
from utils.ai_helper import generate_summary

# 1. Page Configuration
st.set_page_config(
    page_title="Smart Video Summarizer",
    page_icon="📺",
    layout="centered"
)

# 2. Sidebar Configuration Dashboard
st.sidebar.header("⚙️ Configuration Settings")
st.sidebar.markdown("Customize how your AI engine extracts and styles your summary output.")

summary_style = st.sidebar.selectbox(
    label="Select Output Format",
    options=["Paragraph", "Bullet Points", "Action Items"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.caption("Powered by Streamlit 🎈 & Llama 3.1")

# 3. Main App Header & Title
st.title("📺 Smart Video Summarizer")
st.markdown("Paste a YouTube video link below to instantly generate an AI-powered content analysis.")

# 4. User Input Layout
youtube_url = st.text_input(
    label="YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

# 5. Action Button Execution
if st.button("Generate Analysis", type="primary"):
    if youtube_url:
        video_id = extract_video_id(youtube_url)
        
        if video_id:
            try:
                # Step 1: Extraction phase
                with st.spinner("Step 1/2: Extracting transcript from YouTube..."):
                    transcript = get_video_transcript(video_id)
                
                # Step 2: AI Generation Phase
                with st.spinner(f"Step 2/2: Structuring analysis into {summary_style} format..."):
                    ai_summary = generate_summary(transcript, summary_style)
                
                # Step 3: Display results
                st.success("Analysis Generated Successfully!")
                
                st.subheader(f"📌 AI Video Summary ({summary_style})")
                st.write(ai_summary)
                
                # --- NEW PORTFOLIO FEATURE: FILE DOWNLOAD ---
                # Bundle the text cleanly for a file download layout
                download_text = f"YOUTUBE ANALYSIS ({summary_style.upper()})\n"
                download_text += f"Source URL: {youtube_url}\n"
                download_text += "="*40 + "\n\n"
                download_text += ai_summary

                st.download_button(
                    label="📥 Download Summary as TXT",
                    data=download_text,
                    file_name=f"video_summary_{summary_style.lower().replace(' ', '_')}.txt",
                    mime="text/plain"
                )
                # --------------------------------------------
                
                # Hidden raw data drawer
                with st.expander("📄 View Full Raw Transcript"):
                    st.write(transcript)
                    
            except Exception as e:
                st.error(f"Error encountered: {str(e)}")
        else:
            st.error("Could not parse the YouTube URL. Please make sure it's a valid link.")
    else:
        st.warning("Please enter a valid YouTube URL first.")