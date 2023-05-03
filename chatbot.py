import os
import openai


class OpenAIChatbot:
    def __init__(self, api_key, model="gpt-3.5-turbo", temperature=0.9):
        openai.api_key = api_key
        self.model = model
        self.conversation_history = [
            {
                "role": "system",
                "content": "You are a helpful assistant that understands and answers user questions as a pirate"
            }
        ]

    def respond(self, user_message: str):
        self.conversation_history.append({"role": "user", "content": user_message})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.conversation_history
        )

        assistant_message = response.choices[0].message['content']
        self.conversation_history.append({"role": "assistant", "content": assistant_message})
        return assistant_message

api_key = ""  # Replace this with your actual OpenAI API key

#chatbot = OpenAIChatbot(api_key)
#
## Interactive chat loop
#print("Type 'exit' to end the chat.")
#while True:
#    user_message = input("You: ")
#    if user_message.lower() == "exit":
#        break
#    response = chatbot.respond(user_message)
#    print(f"Assistant: {response}")
#
