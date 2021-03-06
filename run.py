from cgnal.logging import configFromFile, getLogger

configFromFile("logging.yaml")
logger = getLogger("runner")

from typing import Sequence  # noqa: E402
from process import Process  # noqa: E402
from cgnal.config.domain import AppConfig, MongoDb, Credentials, \
    Models  # noqa: E402
from cgnal import union  # noqa: E402
from cgnal.config import merge_confs  # noqa: E402


def read_ini(filenames: Sequence[str]) -> AppConfig:
    from configparser import ConfigParser

    config = ConfigParser()
    config.read(filenames)

    return AppConfig(
        mongoDb=MongoDb(
            host=config["MongoDb"]["Host"], port=config["MongoDb"]["Port"],
            credentials=Credentials(
                user=config["MongoDb"]["CredentialsUser"],
                pwd=config["MongoDb"]["CredentialsPwd"]
            ),
            collections=[
                name.strip()
                for name in config["MongoDb"]["Collections"].split(",")
            ]
        ),
        models=Models(path=config["Models"]["path"])
    )


def read_json(filenames: Sequence[str]) -> AppConfig:
    from json import loads

    def readFile(filename) -> dict:
        with open(filename, "r") as fid:
            return loads(fid.read())

    config = union(*[readFile(filename) for filename in filenames])

    return AppConfig(
        mongoDb=MongoDb(
            host=config["mongoDb"]["host"], port=config["mongoDb"]["port"],
            credentials=Credentials(
                user=config["mongoDb"]["credentials"]["user"],
                pwd=config["mongoDb"]["credentials"]["pwd"]
            ),
            collections=config["mongoDb"]["collections"]
        ),
        models=Models(path=config["models"]["path"])
    )
    # return AppConfig(**config)


def read_yaml(filenames: Sequence[str]) -> AppConfig:
    config = merge_confs(filenames, default=None)

    return AppConfig(**config)


def read_yaml_enhanced(filenames: Sequence[str]):
    from cgnal.config.yaml.domain import AppConfig as EnhancedAppConfig

    config = merge_confs(filenames, default=None)

    logger.info(f"Type of configuration: {config['mongoDb']}")

    return EnhancedAppConfig(
        mongoDb=config["mongoDb"], models=config["models"]
    )


if __name__ == "__main__":
    from confs.python.dev import dataConfig  # type: ignore

    # dataConfig = read_ini(
    #     ['confs/ini/dev.ini', 'confs/ini/credentials.ini']
    # )

    # dataConfig = read_json(
    #     ['confs/json/dev.json', 'confs/json/credentials.json']
    # )

    # dataConfig = read_yaml(
    #     ['confs/yaml/dev.yml', 'confs/yaml/credentials.yml']
    # )

    # dataConfig = read_yaml_enhanced(
    #     ['confs/yaml/dev_enhanced.yml']
    # )

    logger.info(f"The mongoDb host is: {dataConfig.mongoDb.host}")

    process = Process(dataConfig)

    logger.info(f"The user is: {dataConfig.mongoDb.credentials.user}")
    logger.info(f"The secret is: {dataConfig.mongoDb.credentials.pwd}")

    process.printCollections(level="INFO")

    logger.info(f"The path of the model is: {dataConfig.models.path}")
