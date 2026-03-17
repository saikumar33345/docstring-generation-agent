from pydantic import BaseModel
from typing import Optional, Dict

class DocstringRequest(BaseModel):
    file_path: Optional[str] = None
    message: Optional[str] = None

class DocstringResponse(BaseModel):
    files_processed: int
    results: Dict[str, str]