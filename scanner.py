from base import DetectorRegistry 
import detectors
from exceptions import DetectorRegistrationError,MalformedInputError
import time
from models import ScanResult
from utils import load_patterns,clean_text,generate_input_hash
class PromptScanner:
    def __init__(self):
        if len(DetectorRegistry.registry)==0:
            raise DetectorRegistrationError("No detectors registered in the system!")
        else:
            self.active_detectors = []
            for detector_class in DetectorRegistry.registry.values():
                detector_instance=detector_class()
                self.active_detectors.append(detector_instance)
    def scan(self, raw_prompt: str) -> ScanResult:
        if  not isinstance(raw_prompt, str) or raw_prompt=="" or len(raw_prompt)>100000:
            raise MalformedInputError("input data does not complete the requirements!")
        prompt_hash=generate_input_hash(raw_prompt)
        cleaned_text=clean_text(raw_prompt)
        all_hits=[]
        for each_detector in self.active_detectors:
            current_hits = each_detector.scan(cleaned_text)
            all_hits.extend(current_hits)
        unique_hits={}
        for hit in all_hits:
            key = (hit.category, hit.pattern)
            if not key in unique_hits:
                unique_hits[key] = hit
            if hit.severity_weight > unique_hits[key].severity_weight:
                unique_hits[key] = hit
        return ScanResult(time_stamp=time.time(),input_hash=prompt_hash,raw_length=len(raw_prompt),hits=list(unique_hits.values()))