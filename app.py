from tkinter import filedialog
from dotenv import load_dotenv
import os
from openai import OpenAI
import webbrowser
from summary import Summary

def main():
    # Load environment variables
    level_of_detail_dict = {1 : "high detail",
                       2 : "medium detail",
                       3 : "low detail"}

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    print("\n--- Starting File Summarization ---")

    file_path = choose_file()

    response = int(input("Enter level of detail (1 - high, 2 - medium, 3 - low): "))
    level_of_detail = level_of_detail_dict.get(response)

    # Read file contents
    with open(file_path, "r", encoding="utf-8") as f:
        contents = f.read()
        print("DEBUG: File contents:\n", contents) #Remove line to get rid of file contents.

    # Use Chat Completions API to summarize
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text clearly and concisely."},
            {"role": "user", "content": f"Please summarize the following text with {level_of_detail} :\n\n{contents}"}
        ]
    )

    mySummary = Summary(response.choices[0].message.content)
    summary = response.choices[0].message.content
    print("\n--- File Summary ---\n")
    print(summary)
    print("\n--------------------\n")

    # Display summary in web browser
    display_in_browser(mySummary)

    # Keep the script running so browser stays open
    input("\nPress Enter to close...")

def display_in_browser(mySummary):
    html_content = f"<html><body><h1>File Summary</h1><p>{mySummary.summary}</p><br><h1>Key Words</h1><p>{mySummary.key_words()}</p></body></html>"
    with open("summary.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    webbrowser.open("summary.html")

def choose_file():
    # Pick file to summarize from a file picker
    file = filedialog.askopenfilename(title="Select file to summarize", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    return file
    

if __name__ == "__main__":
    main()