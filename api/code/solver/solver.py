import logging
from abc import ABC, abstractmethod

from config.constants import BS_LOGGER
from models.energy_demand import EnergyDemand
from models.production_plan import ProductionPlanItem


class Solver(ABC):
    def __init__(self):
        self._logger = logging.getLogger(BS_LOGGER)

    @abstractmethod
    def production_plan(self, demand: EnergyDemand) -> list[ProductionPlanItem] :
        """Abstract"""
        raise NotImplementedError("Subclasses should implement this!")
