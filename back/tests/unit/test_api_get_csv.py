import csv

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.database import get_db_engine
from app.main import app
from app.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_csv.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_engine():
    return engine


app.dependency_overrides[get_db_engine] = override_get_engine
client = TestClient(app)


def test_get_calculations_history_csv():
    response = client.get(
        "/v0/calculationsHistory",
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv; charset=utf-8"
    assert response.headers["content-disposition"] == "attachment;filename=rpn_history_table.csv"

    csv_content = response.content.decode("utf-8")
    csv_reader = csv.reader(csv_content.splitlines())

    expected_data = [
        ["time_executed", "expression", "result"],
        ["2023-12-02 23:27:09", "1 2 +", "3.0"],
        ["2023-12-02 23:27:10", "3 5 +", "8.0"],
        ["2023-12-02 23:27:10", "5.98 flr", "5.0"],
    ]

    for expected_row, actual_row in zip(expected_data, csv_reader):
        assert expected_row == actual_row
