# HW2_Zhanwu_Lin

## Video Walkthrough
https://www.youtube.com/watch?v=joDKUtjl7wI
and 
https://www.youtube.com/watch?v=NjiA6TxS9dU

This project builds a simple GenAI workflow for customer support automation for JHU HW2.

## Business Workflow
Drafting customer support email responses.

## User
Customer support agents in an e-commerce company.

## Input
A customer message, such as a complaint, question, or request.

## Output
A polite, professional, and helpful customer support email draft.

## Why This Task Is Valuable
Customer support writing is repetitive and time-consuming. A GenAI workflow can help create first-pass responses faster and more consistently, while still allowing human review when needed.

## Project Files
- `app.py` — Python script that runs the GenAI workflow
- `prompts.md` — prompt versions and revisions
- `eval_set.json` — small evaluation set with test cases
- `report.md` — short report on design, results, and limitations

## How to Run
1. Install the package:
   `pip install -U google-genai`

2. Set my API key in PowerShell:
   `$env:GEMINI_API_KEY=""`

3. Run the script:
   `python app.py`


