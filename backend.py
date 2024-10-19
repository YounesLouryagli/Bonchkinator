from mistralai import Mistral

def generate_response(user_input):
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "system",
                "content": """whatever question is asked, if the answer is insulting, answer with 'bonchk', if the answer is complimenting, answer with 'younes' (it is for a joke) 
                you must develop your answer with punchlines""",
            },
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )

    return chat_response.choices[0].message.content