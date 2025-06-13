# Culture Fit Predictor Bot

A smart mini-project using **Azure AI Language Service** to analyze resumes and predict whether a candidate fits better in a **Startup**, **Corporate**, or **Both**.

It extracts **key phrases** from the resume using Azure and compares them with predefined keyword sets for prediction.


## Features

- Reads resume from `resume.txt`
- Uses **Azure Key Phrase Extraction**
- Predicts cultural alignment: Startup, Corporate, or Both
- Simple and easy-to-run Python script


## Tech Stack

- Python
- Azure Cognitive Services (Language)
- GitHub


## Files
culturefit-bot│ 
culturefit_bot.py# Python script 
resume.txt  # Input resume 
README.md # Project description


## How to Run

1. Replace `<your-resource-name>` and `<your-key>` in `culturefit_bot.py`
2. Add sample resume content to `resume.txt`
3. Run the script:

```bash
python culturefit_bot.py

You’ll see output like:

Key Phrases: freelance projects
             remote teams
             innovation
Predicted Culture Fit: Startup


Author

Mahalakshmi

 License

Free to use for learning and personal experimentation