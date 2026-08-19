
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def qualify_lead(lead):
    """
    Send lead information to the LLM and receive
    a qualification score and recommendation.
    """

    user_prompt = USER_PROMPT_TEMPLATE.format(
        company=lead["company"],
        industry=lead["industry"],
        company_size=lead["company_size"],
        budget=lead["budget"],
        business_need=lead["business_need"],
        timeline=lead["timeline"],
        decision_maker=lead["decision_maker"]
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    result = json.loads(response.choices[0].message.content)

    return result
