import os
import json
from openai import OpenAI
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. Please add it to your .env file."
    )

client = OpenAI(api_key=api_key)


def qualify_lead(lead):
    """
    Analyze a sales lead using a real LLM and return
    a qualification score, classification, reason,
    and recommended sales action.
    """

    user_prompt = USER_PROMPT_TEMPLATE.format(
        company=lead.get("company", "Not provided"),
        industry=lead.get("industry", "Not provided"),
        company_size=lead.get("company_size", "Not provided"),
        budget=lead.get("budget", "Not provided"),
        business_need=lead.get("business_need", "Not provided"),
        timeline=lead.get("timeline", "Not provided"),
        decision_maker=lead.get("decision_maker", "Not provided")
    )

    try:
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

        result = json.loads(
            response.choices[0].message.content
        )

        # Validate score
        score = int(result.get("score", 0))
        score = max(0, min(100, score))

        result["score"] = score

        # Ensure required fields exist
        result["classification"] = result.get(
            "classification", "Unqualified"
        )

        result["reason"] = result.get(
            "reason", "No reason provided."
        )

        result["recommended_action"] = result.get(
            "recommended_action",
            "Review the lead manually."
        )

        return result

    except Exception as error:
        return {
            "score": 0,
            "classification": "Unqualified",
            "reason": f"LLM processing error: {error}",
            "recommended_action": "Review the lead manually."
        }
