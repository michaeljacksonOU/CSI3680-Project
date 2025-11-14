from dotenv import load_dotenv
import os
from openai import OpenAI

def main():
    # Load environment variables
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    print("\n--- Starting File Summarization ---")

    # Create a vector store
    vector_store = client.beta.vector_stores.create(name="File DB")

    # Read and print file contents for debugging
    with open("test.txt", "r", encoding="utf-8") as f:
        contents = f.read()
        print("DEBUG: File contents:\n", contents) #Remove line to get rid of file contents.

    # Upload file to vector store
    with open("test.txt", "rb") as f:
        client.beta.vector_stores.files.upload_and_poll(
            vector_store_id=vector_store.id,
            file=f
        )

    # Create assistant
    assistant = client.beta.assistants.create(
        name="Summarizer Assistant",
        instructions="Summarize the uploaded text file clearly and concisely.",
        model="gpt-4o",
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

    # Create a thread
    thread = client.beta.threads.create()

    # Ask the assistant to summarize
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Please summarize the contents of the uploaded file."
    )

    # Run and wait for response
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    # Retrieve and print response
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    for msg in messages.data:
        if msg.role == "assistant":
            summary = msg.content[0].text.value
            print("\n--- File Summary ---\n")
            print(summary)
            print("\n--------------------\n")
            break

if __name__ == "__main__":
    main()