from typing import List
from fastapi import File, UploadFile
import os 
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import crud
import model2
import schemas, uploadfile
from database2 import SessionLocal, engine
from uploadfile import upload_image_to_cloudinary
model2.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return "HELLO, Welcome!"


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile,watermark, db:Session =  Depends(get_db)):
    if not file:
        return {"message": "No upload file sent"}
    else:
    
        base_url = os.getcwd()+ "/images/"
        filename = base_url + file.filename
        print(watermark)
        #print(filename)
        srcURL = upload_image_to_cloudinary(filename,watermark)
        srcURL = srcURL.strip('<img src="').strip('"/>')
        db_image = model2.Image(name=file.filename,url = srcURL)
      

        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        print({"srcURL":srcURL})

        return {"srcURL":srcURL}


@app.get("/images",response_model=List[schemas.ImageCreate])
async def get_images(db: Session = Depends(get_db)):

    images = db.query(model2.Image)

    return [jsonable_encoder(image) for image in images]

   

