from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from fastapi import Depends

router = APIRouter()


@router.get("/health/database")
def database_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "database": "healthy"
    }