from scanner import PromptScanner
my_scanner=PromptScanner()
try:
    while True:
        prompt = input("promptguard> ")
        if prompt in ['exit', 'quit']:
            break
        report=my_scanner.scan(prompt)
        print(f"Risk Score: {report.risk_score} | Hits: {report.hits}")
except KeyboardInterrupt:
    print("\n Gracefully shutting down the code")
