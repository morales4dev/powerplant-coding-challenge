import logging

from config.constants import BS_LOGGER
from solver.solver import Solver
from models.energy_demand import EnergyDemand
from models.production_plan import ProductionPlanItem


class FromScratchSolver(Solver):
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(BS_LOGGER)

    def production_plan(self, demand: EnergyDemand) -> list[ProductionPlanItem] :
        ppi1 = ProductionPlanItem(name="gasolinera", p=130)
        productionPlan = [ppi1]
        return productionPlan