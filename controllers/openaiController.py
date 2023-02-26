import openai

openai.api_key = "TU_API_KEY"

def response_prompt(prompt):
    prompt = prompt
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=2048
    )
    respuesta = response.choices[0].text.strip()
    return {"respuesta": respuesta}

