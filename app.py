import openai
import os

# Set up your API key
openai.api_key = "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"

def chat_with_gpt(user_message):
    conversation = [
        {
            "role": "system",
            "content": "You are a helpful assistant that understands and answers user questions."
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    assistant_message = response['choices'][0]['message']['content']
    return assistant_message

if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        assistant_response = chat_with_gpt(user_input)
        print("Assistant:", assistant_response)

