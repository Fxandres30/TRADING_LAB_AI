from fastapi import APIRouter

from app.services.broker_service import broker_service

router = APIRouter(
    prefix="/broker",
    tags=["Broker"]
)


@router.get("/status")
def status():

    return broker_service.status()


@router.get("/connect")
def connect():

    return broker_service.connect()


@router.get("/disconnect")
def disconnect():

    return broker_service.disconnect()