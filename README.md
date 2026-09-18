# AI Exam Recovery Agent

An AI-powered study recovery planner built with Streamlit, Google Gemini, and LangGraph.

## Files

- `app.py` - Streamlit user interface
- `requirements.txt` - Python dependencies
- `agent/` - LangGraph agent files
- `index.html` - Simple project page
- `render.yaml` - Render deployment configuration

## Environment Variable

Set this in Render:

`GEMINI_API_KEY=your_gemini_api_key`

Never commit your API key to GitHub.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
