import logging
from abc import ABC, abstractmethod

from config.constants import BS_LOGGER
from models.linear_programming import LinearProgrammingProblem
from models.energy_demand import EnergyDemand


class LinearProgrammingProblemBuilderImpl(ABC):
    def __init__(self):
        self._logger = logging.getLogger(BS_LOGGER)

    def from_energy_demand(self, demand: EnergyDemand) -> LinearProgrammingProblem:
        pass