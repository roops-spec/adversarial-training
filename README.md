# Adversarial Training

This project explores adversarial machine learning techniques using the Groq API.

## References & Research
This project is based on the methodologies discussed in:
* **Paper:** [Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572)
* **Authors:** Ian J. Goodfellow, Jonathon Shlens, Christian Szegedy
* **Key Concept:** The Fast Gradient Sign Method (FGSM), which I used to generate adversarial perturbations in this repository.

## Setup
1. Clone the repository.
2. Create a `.env` file and add your `GROQ_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`

## Usage
Run the main script:
```python
python main.py
