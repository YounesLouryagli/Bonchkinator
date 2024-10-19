from mistralai import Mistral
import streamlit as st

def generate_response(user_input):
    model = "mistral-large-latest"
    api_key = st.secrets["mistral_key"]
    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "system",
                "content": """As a witty and humorous assistant, answer any question with creative punchlines. 
                If the response involves playful teasing or roasts, mention 'bonchk' (also known as binchk, benchek, amine, aminatorus, cuck lord) in a light-hearted manner. 
                If the response is complimentary or positive, include 'younes' in your answer. Always keep the tone friendly and entertaining.
                if any other question, roast bonchk""",
            },
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )

    return chat_response.choices[0].message.content