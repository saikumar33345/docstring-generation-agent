from pydantic import BaseModel

class DocstringRequest(BaseModel):
    file_path: str

class DocstringResponse(BaseModel):
    updated_code: str
