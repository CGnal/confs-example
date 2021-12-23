from typing import List
from pydantic import BaseModel
from yaml import YAMLObject
from cgnal.config import PathLike
from cgnal.config.domain import AppConfig as BaseAppConfig

class Credentials(YAMLObject):
    def __init__(self, user: str, pwd: str):
        self.user = user
        self.pwd = pwd

# class Credentials(YAMLObject, BaseModel):
#     user: str
#     pwd: str

class MongoDb(YAMLObject):
    def __init__(self, host: str, port: int, credentials: Credentials, collections: List[str]):
        self.host = host
        self.port = port
        self.credentials = credentials
        self.collections = collections

class Models(YAMLObject):
    def __init__(self, path: PathLike):
        self.path = path

class AppConfig:
    def __init__(self, mongoDb: MongoDb, models: Models):
        self.mongoDb=mongoDb
        self.models=models