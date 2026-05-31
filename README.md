# Audio Mood Classifier

A command-line tool that uses GPT-4 to analyze any song and return structured broadcast intelligence — mood, energy, genre, optimal airtime, radio suitability, and listener profile.

Built this because I wanted to understand how media companies could automate content classification at scale. Radio programmers manually categorize thousands of tracks — this does it in seconds.

## What it returns

    MOOD:         Euphoric
    ENERGY:       9/10
    GENRE:        Synth-pop / R&B
    TEMPO:        Fast
    BEST AIRTIME: Morning drive
    LISTENER:     Urban professionals aged 22-35 who work out and commute
    RADIO FIT:    High
    SUMMARY:      A relentless, nostalgic rush built for peak-hour rotation

## Stack

- Python 3
- OpenAI GPT-4
- python-dotenv

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Add your OpenAI key to a .env file then run:

    python3 app.py

## Why structured output matters

Free-form AI responses are hard to use downstream. This tool returns consistent labeled fields every time which means you could pipe the output into a database, a spreadsheet, or a larger scheduling pipeline without parsing unpredictable text.

## Real use cases

- Radio station content scheduling automation
- Streaming playlist mood matching
- Podcast and music catalog tagging at scale
- Broadcast programming intelligence

## What I would add next

- Spotify API integration to pull real audio features like tempo, valence, and danceability
- SQLite caching so the same song does not hit the API twice
- Streamlit UI so non-technical users can run it without the terminal
- Batch mode where you pass a CSV of songs and get back a fully classified CSV
