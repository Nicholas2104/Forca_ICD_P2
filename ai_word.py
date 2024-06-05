"""Escolhendo palavras atraves do Chat-Gpt"""
from openai import OpenAI

# constructing client object
OPEN_AI_KEY = "sk-proj-zCGeJqs2orLARuQI1Nx7T3BlbkFJ3rKkS13CInFrtaXdvUxk"
client = OpenAI(api_key=OPEN_AI_KEY)

prompt = []

def generate_word(language_setting, characters_setting, difficult_setting, max_reponse_tokens=50, model="gpt-3.5-turbo-0125"):
    user_query = f"Give me a random word for a game of hangman in {language_setting} with {characters_setting} characters and difficult {difficult_setting} - output only that word"
    # save user prompts so model remembers out ocnversation while session is running (*)
    prompt.append({"role":"user","content":user_query})
    # query the model
    assistant_response = client.chat.completions.create(
        model=model,
        messages=prompt,
        max_tokens=max_reponse_tokens,
        temperature=0)
    assistant_response_content = assistant_response.choices[0].message.content
    # save responses also to avoid repetitionJ
    prompt.append({"role":"assistant","content":assistant_response_content})
    return assistant_response_content

print(generate_word(language, characters, difficult))