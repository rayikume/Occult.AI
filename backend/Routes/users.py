from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from Common.Database.database import get_db_connection as get_db
from Common.Database.models import UserActivity
from Schemas.user import UserSchema, TokenSchema, UserActivitySchema, LoginRequest
from Middleware.auth import create_access_token, get_current_user, admin_required
from Common.Services.userServices import get_user_by_username, create_user, authenticate_user
from Middleware.logger import log_user_activity

router = APIRouter()

@router.post("/register", response_model=UserSchema, tags=["Users"])
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db, user)
        log_user_activity(db, user.username, "User registration")
        return UserSchema(username=new_user.username, password="", role=new_user.role)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenSchema, tags=["Users"])
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    log_user_activity(db, user.username, "User login")
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserSchema, tags=["Users"])
def read_users_me(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    user = get_user_by_username(db, current_user['username'])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    log_user_activity(db, current_user['username'], "User profile view")
    return UserSchema(username=user.username, password="", role=user.role)

@router.get("/admin/activities", response_model=List[UserActivitySchema], tags=["Admin"])
def get_user_activities(db: Session = Depends(get_db), current_user: dict = Depends(admin_required)):
    activities = db.query(UserActivity).all()
    return activities