from dotenv import load_dotenv
import os
from openai import OpenAI
import webbrowser

def main():
    # Load environment variables
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    print("\n--- Starting File Summarization ---")

    # Read file contents
    with open("test.txt", "r", encoding="utf-8") as f:
        contents = f.read()
        print("DEBUG: File contents:\n", contents) #Remove line to get rid of file contents.

    # Use Chat Completions API to summarize
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text clearly and concisely."},
            {"role": "user", "content": f"Please summarize the following text:\n\n{contents}"}
        ]
    )

    summary = response.choices[0].message.content
    print("\n--- File Summary ---\n")
    print(summary)
    print("\n--------------------\n")

def display_in_browser(summary):
    html_content = f"<html><body><h1>File Summary</h1><p>{summary}</p></body></html>"
    with open("summary.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    webbrowser.open("summary.html")

if __name__ == "__main__":
    main()