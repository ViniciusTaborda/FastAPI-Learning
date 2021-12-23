from fastapi import APIRouter

from apis.version1 import route_user, route_jobs

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.router, prefix="/job", tags=["jobs"])
