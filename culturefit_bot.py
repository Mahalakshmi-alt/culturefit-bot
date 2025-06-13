import requests
import json


endpoint = "https://culturefit-bot.cognitiveservices.azure.com/"
key = "GHDXQeKRnxI6EAht0uMfauWX7z7X9ZoV7mxpkfAeR8pMnZFEnuUGJQQJ99BFACYeBjFXJ3w3AAAEACOGdPmg"

keyphrase_url = endpoint + "/text/analytics/v3.0/keyPhrases"


with open("resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()


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

response = requests.post(keyphrase_url, headers=headers, json=body)
result = response.json()


try:
    key_phrases = result["documents"][0]["keyPhrases"]
except Exception as e:
    print("Error extracting key phrases:", result)
    exit()


def predict_culture_fit(phrases):
    phrases = [p.lower() for p in phrases]
    if any(word in phrases for word in ["innovation", "fast-paced", "startups", "ambiguity", "remote teams"]):
        return "Startup"
    elif any(word in phrases for word in ["process", "structure", "policy", "compliance", "corporate"]):
        return "Corporate"
    else:
        return "General"

culture_fit = predict_culture_fit(key_phrases)


print("Key Phrases:")
for phrase in key_phrases:
    print(f"- {phrase}")

print(f"\nPredicted Culture Fit: {culture_fit}")
