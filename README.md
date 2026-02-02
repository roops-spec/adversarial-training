# Adversarial Training

This project explores adversarial machine learning techniques using the Groq API.

## Methodology: Red Teaming
This project implements a manual Red Teaming framework to evaluate the robustness of `llama-3.1-8b-instant`. 

### Features
- **Adversarial Probing:** Users can input "jailbreak" or "stress-test" prompts.
- **Categorized Logging:** Failures are stored in `failures.csv` with metadata (Timestamp, Prompt, Response, Category).
- **Evaluation Categories:** Logic, Safety, and Hallucination.

### Research Reference
- **Paper:** *Red Teaming Language Models to Identify Toxic Cascades...* (Ganguli et al.)
- **Concept:** Human-led evaluation is critical for identifying "long-tail" failures that automated benchmarks often miss.

## Setup
1. Clone the repository.
2. Create a `.env` file and add your `GROQ_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the main script:
```python
python main.py
