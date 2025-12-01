# CSI3680 Project - Text Summarization Tool

A Python-based text summarization application that uses OpenAI's GPT API to generate concise summaries of text files and displays them in a web browser with keyword extraction.

## Features

- Automatic text summarization using GPT-4o
- Keyword extraction from summaries
- Web browser-based result display

## Installation

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install openai python-dotenv
   ```
3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Test Usage

1. Place your text file as `test.txt` in the project directory
2. Run the application:
   ```bash
   python app.py
   ```
3. View the summary in your default web browser

## Project Structure

- `app.py` - Main application entry point
- `summary.py` - Summary class with keyword extraction
- `summary.html` - Generated HTML output
- `test.txt` - Input text file

## Possible Enhancements

### Core Functionality
- **Multi-file support**: Allow users to select files via CLI arguments or file picker instead of hardcoding `test.txt`
- **Batch processing**: Summarize multiple files at once and generate a combined report
- **Summary length control**: Add options for brief, standard, or detailed summaries
- **Language detection**: Support non-English text with appropriate prompts
- **File format support**: Handle PDF, DOCX, and other document formats

### Output & Display
- **Improved HTML template**: Add proper CSS styling and responsive design
- **Better keyword formatting**: Display keywords as styled tags instead of Python list syntax
- **Export options**: Add PDF, Markdown, or plain text export formats
- **Comparison metrics**: Show original text length vs summary length, estimated reading time saved
- **Dark mode**: Add theme toggle for better viewing experience

### Summary Class Enhancements
- **N-gram extraction**: Extract key phrases (2-3 word combinations) not just single words
- **Sentiment analysis**: Add tone/sentiment detection to summaries
- **Word frequency visualization**: Generate charts showing word distribution
- **Enhanced stopword filtering**: Expand stopword list or integrate NLTK's stopwords
- **Category detection**: Automatically categorize content type (news, technical, narrative, etc.)

### Error Handling & User Experience
- **API error handling**: Gracefully handle rate limits, network errors, and invalid API keys
- **File validation**: Check file existence, handle encoding issues, and enforce size limits
- **Progress indicators**: Show status updates for large file processing
- **Configuration file**: Store user preferences (model choice, max tokens, temperature) in a config file
- **Logging**: Add comprehensive logging for debugging and audit trails

### Performance & Cost Optimization
- **Token optimization**: Intelligently truncate or chunk very large files
- **Caching system**: Save summaries to avoid re-processing identical files
- **Model selection**: Allow users to choose between GPT-4o, GPT-3.5-turbo, or other models based on needs and cost
- **Streaming responses**: Display summary incrementally as it's generated

### Additional Features
- **CLI interface**: Add argparse for `--file`, `--output`, `--format`, and other flags
- **Summary history**: Track all summaries with timestamps in a database or JSON file
- **Custom prompts**: Let users define their own summarization style or focus areas
- **Highlight extraction**: Pull out important quotes or key sentences from original text
- **Comparison mode**: Compare multiple summaries side-by-side
- **API integration**: Expose functionality via REST API for integration with other tools
- **GUI application**: Create a desktop or web-based GUI for easier interaction

## License

[Add your license here]

## Contributors

[Add contributors here]
