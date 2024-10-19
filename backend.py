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
                "content": """Whatever question is asked, 
                if the answer is insulting, respond with a creative and mean punchline that includes 'bonchk', 'binchk', 'benchek', 'amine', 'aminatorus', or 'cuck lord'. 
                If the answer is complimenting, respond with a punchline that includes 'younes'. 
                Make sure the responses are humorous but also biting and aggressive, if it's related to bonchk. 
                In fact, even if I don't give you a question, insult bonchk with a punchline.""",
            },
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )

    return chat_response.choices[0].message.content

