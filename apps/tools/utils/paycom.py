from datetime import datetime
from random import randint

from apps.payment.methods import (CHECK_PERFORM_TRANSACTION, CREATE_TRANSACTION,
                                  PERFORM_TRANSACTION, CANCEL_TRANSACTION,
                                  CHECK_TRANSACTION)


def paycom_method(method: str, params: dict) -> dict:
    transaction_id = randint(100_000, 999_999)
    if method == CHECK_PERFORM_TRANSACTION:
        return {
            "result": {
                "allow": True
            }
        }
    elif method == CREATE_TRANSACTION:
        create_time = datetime.now().timestamp()
        return {
            "result": {
                "create_time": create_time,
                "transaction": transaction_id,
                "state": 1
            }
        }
    elif method == PERFORM_TRANSACTION:
        perform_time = datetime.now().timestamp()
        return {
            "result": {
                "transaction": transaction_id,
                "perform_time": perform_time,
                "state": 2
            }
        }
    elif method == CANCEL_TRANSACTION:
        cancel_time = datetime.now().timestamp()
        return {
            "result": {
                "transaction": transaction_id,
                "cancel_time": cancel_time,
                "state": -2
            }
        }
    elif method == CHECK_TRANSACTION:
        return {
            "result": {
                "create_time": datetime.now().timestamp(),
                "perform_time": datetime.now().timestamp(),
                "cancel_time": 0,
                "transaction": transaction_id,
                "state": 2,
                "reason": None
            }
        }
