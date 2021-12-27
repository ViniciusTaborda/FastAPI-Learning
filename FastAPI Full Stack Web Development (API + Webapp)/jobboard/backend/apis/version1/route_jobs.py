from os import stat
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.jobs import Job
from db.models.users import User
from schemas.jobs import JobCreate, ShowJob
from db.repository.jobs import (
    create_new_job,
    list_jobs,
    retreive_job,
    update_job,
    delete_job,
)
from apis.version1.route_login import get_current_user_from_token

router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    owner_id = current_user.id
    job = create_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.delete("/delete/{id}")
def delete_job_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    owner_id = current_user.id
    job = delete_job(id=id, owner_id=owner_id, db=db)
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
def update_job_by_id(
    id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    owner_id = current_user.id
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
