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

evaluator_user_prompt = f"The pain point is: {pain_point}. Please provide an agentic AI business idea that could be used to solve the pain point."

messages = [{"role": "system", "content": evaluator_user_prompt}]

messages.append({"role": "user", "content": evaluator_user_prompt.format(pain_point=pain_point)})

response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=messages
)

agentic_ai_business_idea = response.choices[0].message.content

print(agentic_ai_business_idea)