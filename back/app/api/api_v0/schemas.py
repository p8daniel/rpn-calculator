from pydantic import BaseModel


class RpnExpression(BaseModel):
    """Rpn expression model"""

    expression: str
