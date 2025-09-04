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

messages = [{"role": "user", "content": "Identify a business area for exploring opportunities for Agentic AI. Please provide only the business idea, no explanation."}]

# Then make the first call:

response =openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)   

# Then read the business idea:

business_idea = response.choices[0].message.content 

print(business_idea)

prompt = f"Identify pain point for {business_idea} that could be solved by Agentic AI. Please provide only the pain point, no explanation."

messages.append({"role": "user", "content": prompt})

response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=messages
)

pain_point = response.choices[0].message.content

print(pain_point)