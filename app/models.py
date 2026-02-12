from pydantic import BaseModel
from typing import Optional

class DocstringRequest(BaseModel):
    file_path: Optional[str] = None
    message: Optional[str] = None

class DocstringResponse(BaseModel):
    updated_code: str
