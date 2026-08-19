import os
import json
from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def qualify_lead(lead):
    user_prompt = USER_PROMPT_TEMPLATE.format(
        company=lead.get("company", "Not provided"),
        industry=lead.get("industry", "Not provided"),
        company_size=lead.get("company_size", "Not provided"),
        budget=lead.get("budget", "Not provided"),
        business_need=lead.get("business_need", "Not provided"),
        timeline=lead.get("timeline", "Not provided"),
        decision_maker=lead.get("decision_maker", "Not provided")
    )

    prompt = f"""
{SYSTEM_PROMPT}

{user_prompt}
"""

    try:
        response = client.models.generate_content(
           model="gemini-3.5-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        result = json.loads(response.text)

        score = int(result.get("score", 0))
        score = max(0, min(100, score))

        return {
            "score": score,
            "classification": result.get(
                "classification", "Unqualified"
            ),
            "reason": result.get(
                "reason", "No reason provided."
            ),
            "recommended_action": result.get(
                "recommended_action",
                "Review the lead manually."
            )
        }

    except Exception as error:
        return {
            "score": 0,
            "classification": "Unqualified",
            "reason": f"LLM processing error: {error}",
            "recommended_action": "Review the lead manually."
        }

