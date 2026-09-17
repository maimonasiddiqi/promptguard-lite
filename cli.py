import argparse
from scanner import PromptScanner
def main():
    parser = argparse.ArgumentParser(description="PromptGuard-Lite CLI")
    parser.add_argument("--scan", type=str, help="Direct text to scan")
    parser.add_argument("--scan-file", type=str, help="Path to a text file to scan")
    args = parser.parse_args()
    try:
        my_scanner=PromptScanner()
        if args.scan:
            report=my_scanner.scan(args.text)
            print(report)
        elif args.scan_file:
            with open(args.file, 'r', encoding='utf-8') as f:
                file_content=f.read()
                report=my_scanner.scan(file_content)
                print(f"Risk Score: {report.risk_score} | Threat Level: {report.threat_level}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()
