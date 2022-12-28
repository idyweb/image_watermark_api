from sqlalchemy.orm import Session

import model2, schemas

def create_image(db: Session, images: schemas.ImageCreate, user_id: int):
    db_item = models.Image(**images.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item