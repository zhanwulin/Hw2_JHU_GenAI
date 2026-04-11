from google import genai
import json

client = genai.Client()

def generate_response(customer_message):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Write a polite customer support email responding to this message: {customer_message}"
    )
    return response.text

with open("eval_set.json", "r") as f:
    cases = json.load(f)

for i, case in enumerate(cases, start=1):
    print(f"\n--- Test Case {i} ---")
    print("Input:", case["input"])
    print("Expected:", case["expected"])
    print("Output:", generate_response(case["input"]))
