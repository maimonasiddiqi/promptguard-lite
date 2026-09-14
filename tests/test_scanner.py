from scanner import PromptScanner
import json
def test_malicious_prompts():
    my_scanner=PromptScanner()
    with open("tests/fixtures/malicious_samples.json") as f:
        file_content=json.load(f)
        for prompt in file_content:
            report=my_scanner.scan(prompt)
            assert report.risk_score>0
def test_benign_prompts():
    my_scanner=PromptScanner()
    with open("tests/fixtures/benign_samples.json") as f:
        file_content=json.load(f)
        for prompts in file_content:
            report=my_scanner.scan(prompts)
            assert report.risk_score==0.0

