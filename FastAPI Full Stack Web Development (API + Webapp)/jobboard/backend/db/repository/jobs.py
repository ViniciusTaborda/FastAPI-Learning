from sqlalchemy.orm import Session, session

from schemas.jobs import JobCreate
from db.models.jobs import Job


def create_new_job(job: JobCreate, db: Session, owner_id: int):
    job = Job(**job.dict(), owner_id=owner_id)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def retreive_job(id: int, db: Session):
    return db.query(Job).filter(Job.id == id).first()


def delete_job(id: int, db: Session):
    return db.query(Job).filter(Job.id == id).delete()


def list_jobs(db: Session):
    return db.query(Job).filter(Job.is_active == True).all()


def update_job(id: int, job: JobCreate, db: Session, owner_id: int):
    existing_job = db.query(Job).filter(Job.id == id)
    if not existing_job.first():
        return 0
    job.__dict__.update(owner_id=owner_id)
    existing_job.update(job.__dict__)
    db.commit()
    return 1
