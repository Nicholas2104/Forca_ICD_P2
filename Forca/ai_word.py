"""Escolhendo palavras atraves do Chat-Gpt"""
from openai import OpenAI

# constructing client object
OPEN_AI_KEY = "sk-proj-zCGeJqs2orLARuQI1Nx7T3BlbkFJ3rKkS13CInFrtaXdvUxk"
client = OpenAI(api_key=OPEN_AI_KEY)

ENGLISH_PROMPT_CONTENT = "Give me a random word for a game of hangman - output only that word"
PORTUGUESE_PROMPT_CONTENT = "Give me a random word in portuguese for a game of hangman - output only that word"
prompt = []

def generate_word(language_setting, max_reponse_tokens=50, model="gpt-3.5-turbo-0125"):
    # Begin by allowing user to select language and handling errors
    while True:
        valid_language_settings = ["ENG","PORT"]
        language_setting = input("Select language setting (ENG or PORT) ").upper()
        
        if not(language_setting in valid_language_settings):
            print(f"{language_setting} is and Invalid setting!!\n")
        else:
            if language_setting == "ENG":
                user_query = ENGLISH_PROMPT_CONTENT
            else:
                user_query = PORTUGUESE_PROMPT_CONTENT
            break
    # save user prompts so model remembers out ocnversation while session is running (*)
    prompt.append({"role":"user","content":user_query})
    # query the model by creating assistant reponse
    assistant_response = client.chat.completions.create(
        model=model,
        messages=prompt,
        max_tokens=max_reponse_tokens,
        temperature=0)
    assistant_response_content = assistant_response.choices[0].message.content
    # save responses also to avoid repetition
    prompt.append({"role":"assistant","content":assistant_response_content})
    return assistant_response_content
