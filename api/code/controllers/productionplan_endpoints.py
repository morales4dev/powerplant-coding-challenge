"""
    This module defines the main POST endpoint for the Powerplan Coding Challenge API.
    It includes functions to handle the primary data submission operation.

    Endpoints:
    - POST /productionplan: Handle the productionplan request according with the energy demand provided


"""
import logging

from fastapi import HTTPException, APIRouter, Depends

from config.constants import BS_CORRELATION_LOGGER
from config.traceability import generate_correlation_id
from models.energy_demand import EnergyDemand
from solver.solver import Solver
from solver.from_scratch_solver_v1_1_0 import FromScratchSolver


productionplan_router = APIRouter()

solver = FromScratchSolver()

# Dependency injection with FastAPI using Depends
def get_solver() -> Solver:
    return solver

@productionplan_router.post("/productionplan", status_code=200)
def post_production_plan(energy_demand: EnergyDemand, solver = Depends(get_solver)):
    """
    This code defines a FastAPI endpoint that returns a ProductionPlan 
    according to the EnergyDemand.

    :param payload:
    :return:
    """

    try:
        correlation_id = generate_correlation_id()

        logging.getLogger(BS_CORRELATION_LOGGER).info(
            f"Processing event with correlation ID {correlation_id}"
        )

        # Create response
        production_plan = solver.production_plan(energy_demand)
        return production_plan

    except TypeError as te:
        logging.getLogger(BS_CORRELATION_LOGGER).error(f"TypeError {te}")
        raise HTTPException(
            status_code=400,
            detail=f"BadRequest Typerror!! {te}",
        )

    except Exception as e:
        logging.getLogger(BS_CORRELATION_LOGGER).error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
