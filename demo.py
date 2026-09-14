from scanner import PromptScanner
my_scanner=PromptScanner()
try:
    while True:
        prompt = input("promptguard> ")
        if prompt in ['exit', 'quit']:
            break
        report=my_scanner.scan(prompt)
        print(report)
except KeyboardInterrupt:
    print("\n Exiting the code bcz of wrong input")
