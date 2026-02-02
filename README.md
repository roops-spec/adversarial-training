# Adversarial Training

This project explores adversarial machine learning techniques using the Groq API.

## Methodology: Red Teaming
This project implements a manual Red Teaming framework to evaluate the robustness of `llama-3.1-8b-instant`. 

### Features
- **Adversarial Probing:** Users can input "jailbreak" or "stress-test" prompts.
- **Categorized Logging:** Failures are stored in `failures.csv` with metadata (Timestamp, Prompt, Response, Category).
- **Evaluation Categories:** Logic, Safety, and Hallucination.

- ## Key Research & Theoretical Basis
This project is informed by the core concepts of adversarial robustness, specifically:
- [cite_start]**Mathematical Vulnerability:** Based on *Explaining and Harnessing Adversarial Examples* (Goodfellow et al., 2014), which demonstrates that adversarial examples are a result of models being "too linear" in high-dimensional spaces.
- [cite_start]**Transferability:** Leveraging the insight that adversarial examples often generalize across different models, making proactive Red Teaming essential for deployment[cite: 215].

## Setup
1. Clone the repository.
2. Create a `.env` file and add your `GROQ_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the main script:
```python
python main.py
