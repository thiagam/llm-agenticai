from dotenv import load_dotenv
load_dotenv(override=True)
import os
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print("OpenAI API Key exists ")
else:
    print("OpenAI API Key does not exists. So exiting")
    raise SystemExit(0)


from openai import OpenAI
openai = OpenAI()
messages = [{"role": "user", "content": "Say Hello World in any random non computer language. Mention the name of the language"}]


response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print(response.choices[0].message.content)
