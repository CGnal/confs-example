from typing import List

from pydantic import BaseModel

from cgnal.config import PathLike


# class Credentials(BaseModel):
#     def __init__(self, user: str, pwd: str):
#         self.user = user
#         self.pwd = pwd

class Credentials(BaseModel):
    user: str
    pwd: str


class MongoDb(BaseModel):
    host: str
    port: int
    credentials: Credentials
    collections: List[str]


class Models(BaseModel):
    path: PathLike


class AppConfig(BaseModel):
    mongoDb: MongoDb
    models: Models
