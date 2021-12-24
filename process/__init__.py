from cgnal.config.domain import AppConfig
from cgnal.logging import WithLogging, levels


class Process(WithLogging):

    def __init__(self, dataConfig: AppConfig):
        self.logger.info("Inizializing Process")
        self.dataConfig = dataConfig

    def printCollections(self, level="INFO"):
        log_level = int(levels[level])
        self.logger.log(log_level, "====================")
        self.logger.log(log_level, "Printing collections")
        self.logger.log(log_level, "====================")
        [self.logger.log(log_level, f" => {name}")
         for name in self.dataConfig.mongoDb.collections]
