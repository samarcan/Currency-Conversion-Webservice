import pytest
from app.shared.logger import getAppLogger


def test_SingletonLogger():
    logger11 = getAppLogger("Uno")
    logger12 = getAppLogger("Uno")
    logger2 = getAppLogger("Dos")
    assert id(logger11) == id(logger12)
    assert id(logger11) != id(logger2)
