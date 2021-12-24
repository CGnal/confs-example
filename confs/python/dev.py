from cgnal.config.domain import Credentials, AppConfig, MongoDb, Models

path = "/this/is/the/path/to/model"

# import os
# path = os.path.join("this", "is", "the", "path","to","model")

credentials = Credentials(user="user", pwd="password")

collections = ["users", "transactions"]

mongoDb = MongoDb(
    host="localhost", port=27017,
    credentials=credentials, collections=collections
)

dataConfig = AppConfig(mongoDb=mongoDb, models=Models(path=path))
