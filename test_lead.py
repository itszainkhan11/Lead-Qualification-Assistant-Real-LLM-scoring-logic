from llm_scoring import qualify_lead

lead = {
    "company": "Small Local Store",
    "industry": "Retail",
    "company_size": "5 employees",
    "budget": "$500",
    "business_need": "Basic website",
    "timeline": "6 months",
    "decision_maker": "No"
}

result = qualify_lead(lead)

print("\n===== AI LEAD QUALIFICATION =====")
print("Score:", result["score"], "/100")
print("Classification:", result["classification"])
print("Reason:", result["reason"])
print("Recommended Action:", result["recommended_action"])
