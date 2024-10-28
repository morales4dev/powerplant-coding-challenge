import logging

from config.constants import BS_LOGGER
from solver.solver import Solver
from models.linear_programming import LinearProgrammingProblem, ProblemResult


class SolverImpl(Solver):
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(BS_LOGGER)

    def solve(self, problem: LinearProgrammingProblem) -> ProblemResult :
        result = ProblemResult()
        return result