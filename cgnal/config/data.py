from typing import List
from pydantic import BaseModel

class Credentials(BaseModel):
    user: str
    pwd: str

# class Credentials(BaseModel):
#     def __init__(self, user: str, pwd: str):
#         self.user = user
#         self.pwd = pwd

class MongoDb(BaseModel):
    host: str
    port: int
    credentials: Credentials
    collections: List[str]

class DataConfig:

    def __init__(self, mongoDb: MongoDb):
        self.mongoDb = mongoDb