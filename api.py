from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from scanner import PromptScanner
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os 
app=FastAPI()
my_scanner=PromptScanner()
key_header=APIKeyHeader(name="x-api-key")
load_dotenv()
API_KEY=os.getenv("API_KEY")
def verify_key( api_key: str = Depends(key_header)):
    if not api_key==API_KEY:
        raise HTTPException(status_code=403,detail="Invalid API Key")
    else:
        return api_key
class ScanRequest(BaseModel):
    prompt:str
@app.post("/scan")
def scanprompt(request:ScanRequest,api_key: str = Depends(verify_key)):
    scanresult=my_scanner.scan(request.prompt)
    return {"status":"success","result":scanresult}
    
    