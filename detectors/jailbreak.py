from base import BaseDetector
from base import DetectorRegistry
import re
from utils import load_patterns 
from models import DetectionHit
@DetectorRegistry.register
class JailbreakDetector(BaseDetector):
    def __init__(self):
        raw_data=load_patterns("patterns/jailbreak.json")
        self.compiled_patterns = []
        for raw in raw_data:
            pattern_string=raw.get("regex")
            compiled_rule=re.compile(pattern_string,re.IGNORECASE | re.DOTALL)
            self.compiled_patterns.append({'regex':compiled_rule,'category':raw.get('category', 'unknown'),'severity_weight':raw.get('severity_weight', 1),'atlas_technique_id':raw.get('atlas_technique_id', 'T0000')})
    def scan (self, text: str) -> list[DetectionHit]:
        hits=[]
        for pattern_dict in self.compiled_patterns:
            for match in pattern_dict['regex'].finditer(text):
                txt=match.group(0)
                new_hit = DetectionHit(
                    category=pattern_dict['category'],
                    severity_weight=pattern_dict['severity_weight'],
                    atlas_technique_id=pattern_dict['atlas_technique_id'],
                    matched_text=txt,
                    pattern=pattern_dict['regex'].pattern
                    )
                hits.append(new_hit)
        return hits
        