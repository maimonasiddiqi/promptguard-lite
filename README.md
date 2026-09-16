# PromptGuard

> A pure-Python prompt injection and jailbreak detection engine.

## 🚀 Quickstart

To get this engine up and running on your local machine, run the following commands:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn api:app --reload
```

## 🏗️ Architecture

PromptGuard is built with security and reliability in mind:
* **API Gatekeeper:** The API endpoints are strictly secured using custom authorization headers. Requests without a valid API Key are immediately rejected at the gate with a `401 Unauthorized` response.
* **CI/CD Integration:** The engine is backed by a robust testing pipeline using `pytest`, ensuring that every update to the detection logic is verified automatically before deployment.

## 🛡️ Threat Model

PromptGuard actively scans and intercepts malicious inputs based on predefined heuristic patterns. Our detection engine catches:
* **Role Overrides:** Attempts to force the AI to ignore its system prompt and assume a new, unauthorized persona.
* **Jailbreaks:** Sophisticated prompts designed to bypass ethical constraints and safety filters.
* **Delimiter Evasion:** Inputs attempting to inject code or commands outside of expected boundaries.
* **Data Exfiltration:** Malicious instructions aiming to leak sensitive system information.