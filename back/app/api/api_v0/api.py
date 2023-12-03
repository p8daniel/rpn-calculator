from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from app.api.api_v0.schemas import RpnExpression
from app.controllers.rpn_calculator import get_rpn_result, get_rpn_results_history
from app.core.database import get_db_engine, get_db_session

api_router = APIRouter(prefix="/v0")


@api_router.post("/rpnCalculate")
async def calculate_rpn(expression: RpnExpression, db_session: Session = Depends(get_db_session)):
    """Calculate the result of an rpn expression and save it to the database"""
    result = await get_rpn_result(db_session=db_session, expression=expression.expression)
    return {"data": result}


@api_router.get("/calculationsHistory")
async def get_csv_calculations_history(db_engine=Depends(get_db_engine)):
    """Get the history of all the calculations in a csv file"""

    df_history = await get_rpn_results_history(db_engine=db_engine)

    return StreamingResponse(
        iter([df_history.to_csv(index=False).encode()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment;filename=rpn_history_table.csv"},
    )
