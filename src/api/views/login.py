from typing import Optional
from jose import JWTError, jwt
from datetime import datetime, timedelta, UTC
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas import Token, OfficialSchema, OFFICIAL_COLLECTION
from settings import config as cfg
from api import mongodb


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()


def get_official(number: str):
    official_col = mongodb.mydb[OFFICIAL_COLLECTION]
    return official_col.find_one({"number": number})


def validate_official_password(name: str, password: str):
    official_col = mongodb.mydb[OFFICIAL_COLLECTION]
    official = official_col.find_one({"name": name})
    return official if official is not None and official["password"] == password else None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:

        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(days=1.)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, cfg.SECRET_KEY, algorithm=cfg.ALGORITHM)
    return encoded_jwt


async def get_current_account(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, cfg.SECRET_KEY, algorithms=[cfg.ALGORITHM])
        number: str = payload.get("number")
        if number is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    official = get_official(number=number)
    if official is None:
        raise credentials_exception
    return OfficialSchema(**official)


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    official = validate_official_password(form_data.username, form_data.password)  # use username as official number
    if not official:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect number or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=cfg.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"number": official["number"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/actual_token")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.get("/current_account")
async def read_accounts_me(current_account = Depends(get_current_account)):
    return current_account
