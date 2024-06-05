"""Escolhendo palavras atraves do Chat-Gpt"""
from openai import OpenAI

# constructing client object
OPEN_AI_KEY = "sk-proj-zCGeJqs2orLARuQI1Nx7T3BlbkFJ3rKkS13CInFrtaXdvUxk"
client = OpenAI(api_key=OPEN_AI_KEY)

prompt = []
def define_prompt_content():
    # Begin by allowing user to select language and handling errors
    while True:
        valid_language_settings = ["ENGLISH","PORTUGUESE"]
        language_setting = input("Select language setting (ENGLISH or PORTUGUESE) ").upper()
        if not(language_setting in valid_language_settings):
            print(f"{language_setting} is an invalid setting!!\n")
        else:
            break  
    while True:
        valid_difficulties = ["EASY","NORMAL","HARD","VERY HARD"]
        difficulty = input("Select a difficulty\nEASY, NORMAL, HARD, VERY HARD").upper()
        if not(difficulty in valid_difficulties):
            print(f"{difficulty} is not a valid setting!!\n")
        else:
            break
    prompt_content = f"Give me a {difficulty} word for a hangman game in {language_setting}"
    return prompt_content
 
def generate_word(max_reponse_tokens=50, model="gpt-3.5-turbo-0125"):
    user_query = define_prompt_content()
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
