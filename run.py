from cgnal.logging import configFromFile, getLogger

configFromFile("logging.yaml")

from process import Process

logger = getLogger("runner")

if __name__ == "__main__":

    from confs.python.dev import dataConfig

    logger.info(f"The mongoDb host is: {dataConfig.mongoDb.host}")

    process = Process(dataConfig)

    process.printCollections(level="INFO")