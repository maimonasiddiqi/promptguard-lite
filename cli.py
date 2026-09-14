import argparse
from scanner import PromptScanner
def main():
    parser = argparse.ArgumentParser(description="PromptGuard-Lite CLI")
    parser.add_argument("--text", type=str, help="Direct text to scan")
    parser.add_argument("--file", type=str, help="Path to a text file to scan")
    args = parser.parse_args()
    try:
        my_scanner=PromptScanner()
        if args.text:
            report=my_scanner.scan(args.text)
            print(report)
        elif args.file:
            with open(args.file, 'r', encoding='utf-8') as f:
                file_content=f.read()
                report=my_scanner.scan(file_content)
                print(report)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()
