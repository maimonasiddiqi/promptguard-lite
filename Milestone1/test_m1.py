from models import DetectionHit
from utils import generate_input_hash, decode_payloads
my_hit = DetectionHit(category="test", pattern="dummy_regex", severity_weight=1, atlas_technique_id="T000", matched_text="bad prompt")
print(my_hit)
print(repr(my_hit)) 
print(len(my_hit))
print(generate_input_hash("test string"))
print(decode_payloads("aGVsbG8="))
