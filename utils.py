import unicodedata
import hashlib
import base64
import codecs
import json
import os
from exceptions import PatternCompileError 
def clean_text(text: str) -> str :
    return unicodedata.normalize('NFKC',text)   
def generate_input_hash(text:str) -> str:
    byte=text.encode('utf-8')
    work=hashlib.sha256(byte)
    return work.hexdigest()
def decode_payloads(text: str) -> dict[str, str]:
    results={}
    try:
        test=base64.b64decode(text)
        result=test.decode('utf-8')
        results['base64']=result
    except Exception:
        pass
    try:
        decode=bytes.fromhex(text).decode('utf-8')
        results['hex']=decode
    except Exception:
        pass
    try:
        code=codecs.decode(text, 'rot_13')
        results['rot13']=code
    except Exception:
        pass
    return results
def load_patterns(file_path: str) -> list:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Pattern file not found at: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            task=json.load(f)
            return task
        except json.JSONDecodeError:
            raise PatternCompileError(f"Invalid JSON syntax in {file_path}")
        
        
    


