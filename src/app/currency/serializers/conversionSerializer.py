import settings
from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import DateTimeType, DecimalType, StringType


class ConversionSerializer(Model):
    initial_currency = StringType(required=True, choices=settings.ALLOWED_CURRENCIES)
    final_currency = StringType(required=True, choices=settings.ALLOWED_CURRENCIES)
    amount = DecimalType(required=True, min_value=0.0)
