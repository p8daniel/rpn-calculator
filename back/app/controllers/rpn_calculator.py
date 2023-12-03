import pandas as pd
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from app import models
from app.errors.app_errors import BadRequestError
from app.rpn_calculator import rpn_calculator


async def get_rpn_result(db_session: Session, expression: str) -> float | None:
    """Get the result of the rpn calculation and save it to the database"""
    try:
        result = rpn_calculator(expression=expression)
    except ValueError as error:
        raise BadRequestError(message=error.__repr__())
    except IndexError:
        raise BadRequestError(message="Invalid expression")

    db_rpn = models.RpnCalculations(expression=expression, result=result)
    db_session.add(db_rpn)
    db_session.commit()

    return result


async def get_rpn_results_history(db_engine: Engine) -> pd.DataFrame:
    """Get all the calculations history from the database in a pandas dataframe"""

    sql_query = "SELECT * FROM rpn_calculations"

    dataframe = pd.read_sql(sql_query, db_engine)
    dataframe.drop(columns=["id"], inplace=True)
    return dataframe
