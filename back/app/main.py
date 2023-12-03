""" main """
from typing import Dict

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

from app import VERSION
from app.api.api_v0.api import api_router
from app.api.exceptions_handler import GLOBAL_EXCEPTIONS_HANDLERS
from app.core.config import settings

app = FastAPI(
    title="API get reports",
    description="",
    version=VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    exception_handlers=GLOBAL_EXCEPTIONS_HANDLERS,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(middleware_class=CorrelationIdMiddleware)
app.add_middleware(
    middleware_class=PrometheusMiddleware, app_name="calculatrice-npi", group_paths=True
)
app.add_route("/metrics", handle_metrics)


@app.get("/ping")
async def ping() -> Dict[str, str]:
    """Ping function"""
    return {"status": "OK"}


app.include_router(api_router, prefix="/api")
