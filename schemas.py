from pydantic import BaseModel

# class ImageBase(BaseModel):
#     name: str
#     size: str

class ImageCreate(BaseModel):
    id:int
    name: str
    url: str  


# class Image(ImageBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True 
