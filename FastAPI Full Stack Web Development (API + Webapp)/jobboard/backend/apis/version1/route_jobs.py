from os import stat
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from starlette.types import Message

from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import (
    create_new_job,
    list_jobs,
    retreive_job,
    update_job,
    delete_job,
)

router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.delete("/delete/{id}")
def delete_job_by_id(id: int, db: Session = Depends(get_db)):

    job = delete_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not-found")
    return job


@router.get("/get/{id}", response_model=ShowJob)
def retreive_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not-found")
    return job


@router.put("/update/{id}")
def update_job_by_id(id: int, job: JobCreate, db: Session = Depends(get_db)):
    owner_id = 1
    message = update_job(id=id, job=job, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not-found")
    return {"detail": "Successfully updated."}


@router.get("/list")
def list_all_jobs(db: Session = Depends(get_db)):
    job = list_jobs(db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not-found")
    return job
