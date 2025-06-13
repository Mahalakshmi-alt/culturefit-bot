import requests
import json

# === Step 1: Replace with your actual Azure key and endpoint ===
endpoint = "https://culturefit-bot.cognitiveservices.azure.com/"
key = "GHDXQeKRnxI6EAht0uMfauWX7z7X9ZoV7mxpkfAeR8pMnZFEnuUGJQQJ99BFACYeBjFXJ3w3AAAEACOGdPmg"

keyphrase_url = endpoint + "/text/analytics/v3.0/keyPhrases"

# === Step 2: Load resume or input text ===
with open("resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()

# === Step 3: Prepare request ===
headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/json"
}

body = {
    "documents": [
        {
            "id": "1",
            "language": "en",
            "text": resume_text
        }
    ]
}

# === Step 4: Send API request ===
response = requests.post(keyphrase_url, headers=headers, json=body)
result = response.json()

# === Step 5: Extract key phrases ===
try:
    key_phrases = result["documents"][0]["keyPhrases"]
except Exception as e:
    print("Error extracting key phrases:", result)
    exit()

# === Step 6: Predict Culture Fit (Simple logic for now) ===
def predict_culture_fit(phrases):
    phrases = [p.lower() for p in phrases]
    if any(word in phrases for word in ["innovation", "fast-paced", "startups", "ambiguity", "remote teams"]):
        return "Startup"
    elif any(word in phrases for word in ["process", "structure", "policy", "compliance", "corporate"]):
        return "Corporate"
    else:
        return "General"

culture_fit = predict_culture_fit(key_phrases)

# === Step 7: Output ===
print("Key Phrases:")
for phrase in key_phrases:
    print(f"- {phrase}")

print(f"\nPredicted Culture Fit: {culture_fit}")