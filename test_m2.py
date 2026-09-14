from base import DetectorRegistry
import detectors
my_registry = DetectorRegistry.registry
print(f"Total Detectors Loaded: {len(my_registry)}")
for name in my_registry:
    print(name)
    
