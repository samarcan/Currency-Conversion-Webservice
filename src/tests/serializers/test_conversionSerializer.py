import pytest
from app.serializers.conversionSerializer import ConversionSerializer
from schematics.exceptions import DataError

testIncorrectData = [
    {"initial_currency": "CZK", "final_currency": "EUR", "amount": -2.9},
    {"initial_currency": "JKL", "final_currency": "EUR", "amount": 2.9},
    {"initial_currency": "CZK", "final_currency": "JKL", "amount": 2.9},
    {"initial_currency": 2, "final_currency": "EUR", "amount": 2.9},
    {"initial_currency": "CZK", "final_currency": 2, "amount": 2.9},
    {"final_currency": "EUR", "amount": 2.9},
    {"initial_currency": "CZK", "amount": 2.9},
    {"initial_currency": "CZK", "final_currency": "EUR"},
]


def test_correct_conversion_serializer():
    testInput = {"initial_currency": "CZK", "final_currency": "EUR", "amount": 2.9}
    conversionSerializer = ConversionSerializer(testInput)
    assert conversionSerializer.validate() is None


@pytest.mark.parametrize("testInput", testIncorrectData)
def test_fail_conversion_serializer(testInput):
    conversionSerializer = ConversionSerializer(testInput)
    with pytest.raises(DataError):
        assert conversionSerializer.validate()
