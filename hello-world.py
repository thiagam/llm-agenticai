from dotenv import load_dotenv
load_dotenv(override=True)
import os
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print("OpenAI API Key exists ")
else:
    print("OpenAI API Key not exists")


from openai import OpenAI
openai = OpenAI()
messages = [{"role": "user", "content": "Print Hello World in any random non computer language. Mention the name of the language"}]


response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=messages
)

print(response.choices[0].message.content)