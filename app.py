import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY") or open(".env").read().split("OPENAI_API_KEY=")[1].strip()
client = OpenAI(api_key=api_key)


def analyze(song, artist):
    prompt = f"""
You're a music analyst for a broadcast radio network.

Analyze "{song}" by {artist}. Return exactly this, no extra text:

MOOD: [1-2 words]
ENERGY: [1-10]
GENRE: [main genre]
TEMPO: [slow / mid / fast]
BEST AIRTIME: [morning drive / midday / afternoon / evening / late night]
LISTENER: [one sentence on who listens to this]
RADIO FIT: [high / medium / low]
SUMMARY: [one sentence on what makes this track what it is]
"""
    res = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return res.choices[0].message.content.strip()


def main():
    print()
    print("=" * 48)
    print("  Audio Mood Classifier")
    print("  Built for broadcast and streaming pipelines")
    print("=" * 48)

    while True:
        print()
        song = input("Song (or q to quit): ").strip()
        if song.lower() in ["q", "quit", "exit"]:
            break

        artist = input("Artist: ").strip()
        if not song or not artist:
            print("Need both a song and artist name.")
            continue

        print("\nAnalyzing...\n")

        try:
            result = analyze(song, artist)
            print("-" * 48)
            print(result)
            print("-" * 48)
        except Exception as e:
            print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
