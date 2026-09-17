from scanner import PromptScanner
import json
true_positives=0
false_negatives=0
true_negatives=0
false_positives=0
with open("tests/fixtures/malicious_samples.json", "r") as f:
    known_bads=json.load(f)
with open("tests/fixtures/benign_samples.json","r") as f:
    known_goods=json.load(f)
my_scanner=PromptScanner()
for bad_input in known_bads:
    report=my_scanner.scan(bad_input)
    if report.risk_score>0:
        true_positives+=1
    else:
        false_negatives+=1
for good_input in known_goods:
    report=my_scanner.scan(good_input)
    if report.risk_score==0.0:
        true_negatives+=1
    else:
        false_positives+=1
precision=0.0
recall=0.0

if true_positives+false_positives:
    precision=true_positives/(true_positives+false_positives)
if true_positives+false_negatives:
    recall=true_positives/(true_positives+false_negatives)
print(f"recall is : {recall}")
print(f"Precision: {precision * 100}%")
if precision!=0 or recall!=0:
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f1_score)

