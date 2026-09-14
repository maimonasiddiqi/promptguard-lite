from dataclasses import dataclass,field,asdict
from enum import Enum
class SeverityLevel(Enum):
    SAFE=0
    LOW=1
    MEDIUM=2
    HIGH=3
    CRITICAL=4
@dataclass
class DetectionHit:
    category:str
    pattern:str
    severity_weight:int
    atlas_technique_id:str
    matched_text:str
    def __str__(self):
        return f'Severity Weight is {self.severity_weight} and Category Name is {self.category}'
    def __repr__(self):
        return f'DETECTIONHIT (category={self.category} , pattern={self.pattern})'
    def __len__(self):
        return len(self.matched_text)
@dataclass
class ScanResult:
    time_stamp:float
    input_hash:str
    raw_length:int
    hits:list['DetectionHit']= field(default_factory=list)
    def __bool__(self):
        return bool(self.hits)
    def __add__(self, other):
        merged=self.hits+other.hits
        return ScanResult(hits=merged,time_stamp=self.time_stamp,input_hash=self.input_hash,raw_length=self.raw_length)
    def to_dict(self):
        return asdict(self)
    def __str__(self):
        return f"""--- SCAN REPORT ---

        Timestamp: {self.time_stamp}

        Input Hash: {self.input_hash}

        Length: {self.raw_length}

        Detections Found: {self.hits}

        """
    @property
    def risk_score(self) -> float:
        total_weight=sum(hit.severity_weight for hit in self.hits)
        return min(float(total_weight), 10.0)
    @property 
    def threat_level(self) -> SeverityLevel:
        if self.risk_score==0.0:
            return SeverityLevel.SAFE
        elif self.risk_score<=3.9:
            return SeverityLevel.LOW
        elif self.risk_score<=6.9:
            return SeverityLevel.MEDIUM
        elif self.risk_score<=8.9:
            return SeverityLevel.HIGH
        else:
            return SeverityLevel.CRITICAL