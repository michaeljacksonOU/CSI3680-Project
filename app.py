import sys
from tkinter import filedialog
from dotenv import load_dotenv
import os
from openai import OpenAI
import webbrowser
from summary import Summary
from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
def get_detail_level():
    input_box = customtkinter.CTkInputDialog(text=" Welcome to our AI Text Summarizer.\n\n" \
    "This application will utilize GPT-4o to summarize text you upload to it.\n\n" \
    "You have two simple steps to follow:\n\n" \
    "1. Select how detailed of a response you want.\n 2. Select a .txt file that you would like summarized.\n\n" \
    "Your Response is then hosted at 127.0.0.1:5500/summary.html.\n\n " \
    "When you are ready, you may proceed with step 1!\n\n" \
    "      Enter level of detail (1 - high, 2 - medium, 3 - low):", title="AI Text Summarizer")
    try:
        if int(input_box.get_input()) not in [1, 2, 3]:
            raise ValueError
    except (ValueError, TypeError):
        error_box = customtkinter.CTkInputDialog(text="Invalid input. Please enter 1, 2, or 3 for the level of detail.", title="Error")
        sys.exit()


def main(detail_level_response):
    # Load environment variables
    level_of_detail_dict = {1 : "high detail",
                       2 : "medium detail",
                       3 : "low detail"}
    level_of_detail = level_of_detail_dict.get(detail_level_response)
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    print("\n--- Starting File Summarization ---")

    file_path = choose_file()

    # response = int(input("Enter level of detail (1 - high, 2 - medium, 3 - low): ")
    global response
    level_of_detail = level_of_detail_dict.get(response)
    print(level_of_detail)

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
    keywords = mySummary.key_words
    keyword_tags = ''.join([f'<span class="keyword-tag">{word}</span>' for word in keywords])
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Summary</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section:last-child {{
            margin-bottom: 0;
        }}
        
        .section-title {{
            font-size: 1.8em;
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            display: inline-block;
        }}
        
        .summary-text {{
            font-size: 1.1em;
            color: #555;
            line-height: 1.8;
            text-align: justify;
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }}
        
        .keywords-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 20px;
        }}
        
        .keyword-tag {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            font-size: 0.95em;
            font-weight: 500;
            box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3);
            transition: transform 0.2s, box-shadow 0.2s;
            display: inline-block;
        }}
        
        .keyword-tag:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        
        @media (max-width: 768px) {{
            body {{
                padding: 20px 10px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            .content {{
                padding: 30px 20px;
            }}
            
            .section-title {{
                font-size: 1.5em;
            }}
            
            .summary-text {{
                font-size: 1em;
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📄 Text Summary</h1>
            <p>AI-Powered Content Analysis</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2 class="section-title">Summary</h2>
                <div class="summary-text">
                    {mySummary.summary}
                </div>
            </div>
            
            <div class="section">
                <h2 class="section-title">Key Words</h2>
                <div class="keywords-container">
                    {keyword_tags}
                </div>
            </div>
        </div>
        
        <div class="footer">
            Summary Generated with OpenAI GPT-4
        </div>
    </div>
</body>
</html>"""
    
    with open("summary.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    webbrowser.open("summary.html")

def choose_file():
    # Pick file to summarize from a file picker
    try:
        file = filedialog.askopenfilename(title="Select file to summarize", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if not file:
            raise Exception("No file selected")
        else:
            return file
    except Exception:
        print(f"Application was canceled")
        sys.exit()

if __name__ == "__main__":
    # root.mainloop()
    response = get_detail_level()
    main(response)