from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from DataBase import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime
from jose import jwt, JWTError

SECRET_KEY = '123rasulQq'  # мой пароль
ALGORITHM = 'HS256'  # алгоритм который мой токен будет шифроваться


class CreateUser(BaseModel):  # модель создания Польвотеля
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str


# ______________________________________________________


aoth2_bear = OAuth2PasswordBearer(
    tokenUrl="token")  # мы собираемся иззвлечь любые данные или что нибудь из заголовка авторизации
# ______________________________________________________


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
models.Base.metadata.create_all(bind=engine)  # это создаёт нашу базу данных и сделает всё необходимое для таблици
app = FastAPI()


def get_db():  # безконечная связь с базой данных
    global db
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):  # хеширует пароль
    return bcrypt_context.hash(password)


def verify_password(plain_password,
                    hashed_password):  # проверяем порольпользователя , сравниваем хешированный пароль с обычным
    return bcrypt_context.verify(plain_password, hashed_password)


def authenticate_user(user: str, password: str,
                      db):  # Авторизацыи пользователя , Это функция проверяет пароль и username
    user = db.query(models.User) \
        .filter(models.User.username == user) \
        .first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int,  # создаём токен из зашифрованного данного
                        expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, 'id': user_id, }
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@app.post("decode/token") #декодировани веб токена JWT
async def get_current_user(token: str = Depends(aoth2_bear)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise get_user_exceptions()
        return {"username": username, "user_id": user_id}
    except JWTError:
        raise HTTPException(status_code=404, detail="not working")


@app.post('/create/user')  # создания пользователя и пушем в таблицу
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = models.User()
    create_user_model.email = create_user.email
    create_user_model.name = create_user.first_name
    create_user_model.surname = create_user.last_name

    hash_password = get_password_hash(create_user.password)

    create_user_model.hashed_password = hash_password
    create_user_model.username = create_user.username
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()


@app.post('/token')  # проверяем пароль и имя пользователя
async def login_for_access_token(from_data: OAuth2PasswordRequestForm = Depends()
                                 , db: Session = Depends(get_db)):
    user = authenticate_user(from_data.username, from_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username,
                                user.id,
                                expires_delta=token_expires)
    return {"token": token}

# Exceptions

def get_user_exceptions():
    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return credential_exceptions


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response
