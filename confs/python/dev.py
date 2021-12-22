from cgnal.config.data import Credentials, DataConfig, MongoDb

a=1

credentials = Credentials(user="user", pwd="password")

collections = ["users", "transactions"]

mongoDb = MongoDb(host="localhost", port=27017, credentials=credentials, collections=collections)

dataConfig = DataConfig(mongoDb)

