from base import BaseDetector
from base import DetectorRegistry
import re
from utils import load_patterns 
from models import DetectionHit
@DetectorRegistry.register
class DelimiterInjectionDetector(BaseDetector):
    def __init__(self):
        raw_info=load_patterns("patterns/delimiter.json")
        self.pattern=[]
        for raw in raw_info:
            regex_detector=raw.get("regex")
            compiled_regex=re.compile(regex_detector,re.IGNORECASE | re.DOTALL)
            self.pattern.append({'regex':compiled_regex,'category':raw.get('category', 'unknown'),'severity_weight':raw.get('severity_weight', 1),'atlas_technique_id':raw.get('atlas_technique_id', 'T0000')})
    def scan(self,text : str) ->list[DetectionHit]:
        hits=[]
        for pattern_info in self.pattern:
            for rule in pattern_info['regex'].finditer(text):
                txt=rule.group(0)
                override_hit=DetectionHit(   
                    category=pattern_info['category'],
                    severity_weight=pattern_info['severity_weight'],
                    atlas_technique_id=pattern_info['atlas_technique_id'],
                    matched_text=txt,
                    pattern=pattern_info['regex'].pattern
                    )
                hits.append(override_hit)
        return hits

