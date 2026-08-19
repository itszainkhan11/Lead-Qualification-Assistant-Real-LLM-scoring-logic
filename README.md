# AI Lead Qualification Assistant – Real LLM Scoring Logic

## 📌 Project Overview

The AI Lead Qualification Assistant is an LLM-powered system that evaluates sales leads and determines their potential value for a business.

Instead of relying only on fixed rules, the system uses a real Large Language Model (LLM) to analyze lead information and generate a qualification score, classification, reasoning, and recommended sales action.

## 🎯 Objective

The main objective of this project is to automate the initial sales lead qualification process and help sales teams identify high-value prospects faster.

## ✨ Features

- Real LLM-based lead analysis
- Lead score from 0–100
- Hot, Warm, Cold, and Unqualified classification
- Budget analysis
- Business need analysis
- Buying timeline analysis
- Decision-maker analysis
- Company-fit evaluation
- AI-generated reasoning
- Recommended sales action
- Secure API key handling using environment variables

## 🧠 Scoring Logic

The LLM evaluates the following factors:

| Factor | Description |
|---|---|
| Budget | Determines the lead's available spending capacity |
| Business Need | Evaluates how strong and relevant the requirement is |
| Timeline | Checks how soon the lead intends to purchase |
| Decision Maker | Determines whether the lead can influence the buying decision |
| Company Fit | Evaluates how well the company matches the target customer |

### Lead Classification

- **80–100:** 🔥 Hot Lead
- **60–79:** 🟡 Warm Lead
- **40–59:** 🟠 Cold Lead
- **0–39:** ❌ Unqualified

## 🔄 How It Works

```text
Lead Information
       ↓
LLM Analysis
       ↓
Evaluate Lead Factors
       ↓
Generate Score (0–100)
       ↓
Classify Lead
       ↓
Generate Reason
       ↓
Recommend Sales Action
