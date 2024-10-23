"""
    This module defines the main POST endpoint for the Powerplan Coding Challenge API.
    It includes functions to handle the primary data submission operation.

    Endpoints:
    - POST /productionplan: Handle the productionplan request according with the energy demand provided


"""

import logging
from typing import List

from fastapi import HTTPException

from config.constants import BS_CORRELATION_LOGGER
from config.traceability import generate_correlation_id
from models.energy_demand import EnergyDemand
from models.production_plan import ProductionPlanItem
from fastapi import APIRouter

productionplan_router = APIRouter()


@productionplan_router.post("/productionplan", status_code=200)
def post_production_plan(payload: EnergyDemand):
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
        ppi1 = ProductionPlanItem(name="gasolinera",p=130)
        productionPlan = [ppi1]
        return productionPlan

    except TypeError as te:
        logging.getLogger(BS_CORRELATION_LOGGER).error(f"TypeError {te}")
        raise HTTPException(
            status_code=400,
            detail=f"BadRequest Typerror!! {te}",
        )

    except Exception as e:
        logging.getLogger(BS_CORRELATION_LOGGER).error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
