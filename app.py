import streamlit as st
from llm_scoring import qualify_lead

st.set_page_config(
    page_title="AI Lead Qualification Assistant",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Lead Qualification Assistant")
st.write("Use AI to score and qualify your sales leads.")

st.divider()

company = st.text_input("Company Name", placeholder="e.g. ABC Solutions")
industry = st.text_input("Industry", placeholder="e.g. Software")
company_size = st.text_input("Company Size", placeholder="e.g. 50 employees")
budget = st.text_input("Budget", placeholder="e.g. $10,000")
business_need = st.text_area(
    "Business Need",
    placeholder="Describe what the company needs..."
)
timeline = st.text_input(
    "Buying Timeline",
    placeholder="e.g. 30 days"
)
decision_maker = st.selectbox(
    "Is the person a decision maker?",
    ["Yes", "No", "Unknown"]
)

if st.button("🚀 Qualify Lead", use_container_width=True):

    if not company:
        st.warning("Please enter the company name.")
    else:
        lead = {
            "company": company,
            "industry": industry,
            "company_size": company_size,
            "budget": budget,
            "business_need": business_need,
            "timeline": timeline,
            "decision_maker": decision_maker
        }

        with st.spinner("🤖 AI is analyzing the lead..."):
            result = qualify_lead(lead)

        st.success("Lead analysis completed!")

        st.metric(
            label="AI Lead Score",
            value=f"{result['score']}/100"
        )

        st.subheader("Classification")
        st.write(result["classification"])

        st.subheader("AI Reasoning")
        st.write(result["reason"])

        st.subheader("Recommended Sales Action")
        st.write(result["recommended_action"])