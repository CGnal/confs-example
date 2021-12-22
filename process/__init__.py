from cgnal.logging import WithLogging, levels
from cgnal.config.data import DataConfig

class Process(WithLogging):

    def __init__(self, dataConfig: DataConfig):
        self.logger.info(f"Inizializing Process")
        self.dataConfig = dataConfig

    def printCollections(self, level="INFO"):
        l = int(levels[level])
        self.logger.log(l, "====================")
        self.logger.log(l, "Printing collections")
        self.logger.log(l, "====================")
        [self.logger.log(l, f" => {name}") for name in self.dataConfig.mongoDb.collections]