from models import DetectionHit
import re
class BaseDetector():
    def scan(self,text: str) -> list[DetectionHit]:
        raise NotImplementedError("Subclasses must implement scan method")
class DetectorRegistry:
    registry={}
    @classmethod
    def register(cls,detector_cls):
        cls.registry[detector_cls.__name__] = detector_cls
        return detector_cls
