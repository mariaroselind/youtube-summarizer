# 📺 Smart Video Summarizer

An AI-powered web application built with **Streamlit** that extracts transcripts from YouTube videos and leverages open-source LLMs via **Groq** to generate dynamic, multi-format content analyses instantly.

---

## 🚀 Live Demo
🔗 **[Launch Live Web Application](https://youtube-summarizer26.streamlit.app/)**

---

## ✨ Features
* **Zero-Cost Architecture:** Powered entirely by free-tier developer tools and open-source models (Meta's Llama 3.1).
* **Dynamic Prompt Engineering:** Choose your preferred analytical format via an interactive sidebar dashboard:
  * 📝 **Paragraph:** A cohesive, 3-4 sentence overview of the video content.
  * 📊 **Bullet Points:** A high-impact breakdown of the core takeaways.
  * ⚡ **Action Items:** A task-focused list of lessons learned or next steps.
* **Crash-Proof Token Guardrail:** Includes automatic text-truncation algorithms to keep raw transcript data safely within free-tier API token-per-minute (TPM) limits.
* **Exportable Data:** Seamlessly download your generated AI summary as a `.txt` file with one click.
* **Source Transparency:** Expandable drawer to inspect the raw, time-stamped video transcript text.

---

## 🛠️ Tech Stack & Dependencies
* **Frontend UI:** Streamlit (Python Web Framework)
* **AI Engine:** Groq API Cloud Client (`llama-3.1-8b-instant`)
* **Scraping Engine:** YouTube Transcript API
* **Environment Management:** Python-Dotenv

---

## 📦 Installation & Local Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/mariaroselind/youtube-summarizer.git](https://github.com/mariaroselind/youtube-summarizer.git)
cd youtube-summarizer
