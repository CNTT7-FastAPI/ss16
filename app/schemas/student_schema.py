# pyrefly: ignore [missing-import]
from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    name: str

class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
            from_attributes = True

# Model base dùng chung, muốn dùng cho nhưng tính năng khác thì phải kế thừa rồi viết lại
class StudentBase(BaseModel):
    name: str
    age: int
    

class StudentCreateDTO(StudentBase):
    department_id: int

class StudentPutDTO(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    department: Optional[DepartmentResponse]
    class Config:
        from_attributes = True