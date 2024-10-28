import logging

from config.constants import BS_LOGGER
from planner.planner import Planner
from solver.solver import Solver
from models.energy_demand import EnergyDemand
from models.production_plan import ProductionPlanItem
from models.linear_programming import LinearProgrammingProblem, ProblemResult

from builders.production_plan_builder import ProductionPlanBuilder


class ProductionPlanBuilderImpl(ProductionPlanBuilder):
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(BS_LOGGER)

    def from_problem_result(self, problem_result: ProblemResult) -> list[ProductionPlanItem]:
        ##
        ppi1 = ProductionPlanItem(name="gasolinera", p=130)
        productionPlan = [ppi1]
        return productionPlan