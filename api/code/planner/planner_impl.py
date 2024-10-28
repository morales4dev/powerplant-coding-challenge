import logging

from config.constants import BS_LOGGER
from planner.planner import Planner
from solver.solver import Solver
from models.energy_demand import EnergyDemand
from models.production_plan import ProductionPlanItem
from models.linear_programming import LinearProgrammingProblem, ProblemResult
from builders.lp_problem_builder import LinearProgrammingProblemBuilder
from builders.production_plan_builder import ProductionPlanBuilder


class PlannerImpl(Planner):
    def __init__(self, 
                 lp_problem_builder: LinearProgrammingProblemBuilder, 
                 solver: Solver,
                 production_plan_builder: ProductionPlanBuilder):
        super().__init__()
        self._logger = logging.getLogger(BS_LOGGER)
        self._lp_problem_builder = lp_problem_builder
        self._solver = solver
        self._production_plan_builder = production_plan_builder

    def production_plan(self, demand: EnergyDemand) -> list[ProductionPlanItem] :
        lp_problem = self._lp_problem_builder.from_energy_demand(demand)
        problem_result = self._solver.solve(lp_problem)
        productionPlan = self._production_plan_builder.from_problem_result(problem_result)
        return productionPlan
