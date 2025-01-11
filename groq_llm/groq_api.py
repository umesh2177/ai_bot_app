import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()


def groq_api_call(model,user_input,text_context,system_prompt):
        api_key = os.getenv("Groq_api_key")
        client = Groq(api_key=api_key)
        print("============",text_context)
        #   
        # Set the system prompt
        chat_history=[]
        # system_prompt = {
        # "role": "system",
        # "content":""" You are a helpful assistant.
        #         Be remember you have to give the answer within provided context
        #         You reply with proper summary within given context.
        #         """
        # }

        # Initialize the chat history
        chat_history = [system_prompt]

        chat_history.append({"role": "user", "content": text_context})
        chat_history.append({"role": "user", "content": user_input})
        print(len(chat_history))

        response = client.chat.completions.create(model= model,#"llama-3.3-70b-versatile",#"llama3-70b-8192",
                                    messages=chat_history,
                                    max_tokens=1000,
                                    temperature=1.2,
                                    stream=False,)
        # Append the response to the chat history
        chat_history.append({
                "role": "assistant",
                "content": response.choices[0].message.content
        })
        # Print the response
        print("\n\n")
        # print("Assistant:\n", response.choices[0].message.content)
        return response.choices[0].message.content 

