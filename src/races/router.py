from fastapi import APIRouter


router = APIRouter(
    prefix="/races",
    tags=["Races"]
)