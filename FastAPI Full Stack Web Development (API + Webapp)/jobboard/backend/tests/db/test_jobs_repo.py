from sqlalchemy.orm import Session

from db.repository.jobs import create_new_job

from schemas.jobs import JobCreate
from db.repository.jobs import create_new_job, retreive_job
from tests.utils.user import create_random_owner


def test_retrieve_job_by_id(db_session: Session):
    title = "Test title"
    company = "Test company"
    company_url = "testcompany.com"
    location = "BR, PR"
    description = "Test description"
    owner = create_random_owner(db=db_session)
    job_schema = JobCreate(
        title=title,
        company=company,
        company_url=company_url,
        location=location,
        description=description,
    )
    job = create_new_job(job=job_schema, db=db_session, owner_id=owner.id)
    retreived_job = retreive_job(id=job.id, db=db_session)
    assert retreived_job.id == job.id
    assert retreived_job.title == "Test title"
