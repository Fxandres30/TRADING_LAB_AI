from fastapi import APIRouter

from ..manager.account_manager import AccountManager

router = APIRouter(

    prefix="/accounts",

    tags=["Accounts"],

)

manager = AccountManager()


@router.get("/brokers")
def brokers():

    return manager.brokers()


@router.get("/")
def accounts():

    return manager.accounts()