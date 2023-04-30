"""KPI Database models."""

# django
from django.db import models
from django.utils.translation import gettext_lazy as _


class Organization(models.Model):
    name = models.CharField(max_length=255)


class Department(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, models.CASCADE)


class DataType(models.Model):
    """Data types for the indicators"""

    class AggregationType(models.TextChoices):
        """Valid tipes of data aggregation."""

        COUNT = "COUNT", _("Conteo")
        SUM = "SUM", _("Suma")
        PRODUCT = "PRODUCT", _("Producto")
        AVERAGE = "AVERAGE", _("Promedio")
        LAST_VALUE = "LAST_VALUE", _("Ultimo Valor")
        LAST_RESULT = "LAST_RESULT", _("Ultimo Resultado")
        CONSTANT = "CONSTANT", _("1")

    class ValueType(models.TextChoices):
        """Valid value tipes for the data."""

        MONEY = "MONEY", _("Unidades Monetarias")
        HOURS = "HOURS", _("Horas")
        EVENTS = "EVENTS", _("Eventos")
        UNITS = "UNITS", _("Unidades")
        PERCENTAGE = "PERCENTAGE", _("Porcentaje")

    name = models.CharField(max_length=255)
    aggregation_type = models.CharField(
        max_length=16,
        choices=AggregationType.choices,
        default=AggregationType.COUNT,
    )
    value_type = models.CharField(
        max_length=16,
        choices=ValueType.choices,
        default=ValueType.UNITS,
    )


class DataPoint(models.Model):
    """Individual data points"""

    data_type = models.ForeignKey(DataType, models.CASCADE)
    department = models.ForeignKey(Department, models.CASCADE)
    value = models.IntegerField()
    date = models.DateField()


class Indicator(models.Model):
    """Indicators, can be used on diferent deparments"""

    class TendencyType(models.TextChoices):
        """Valid value tipes for the tendency."""

        GT = ">", _("Creciente")
        EQ = "=", _("Ninguna")
        LT = "<", _("Decreciente")

    department = models.ManyToManyField(Department)
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    desired_tendency = models.CharField(
        max_length=1,
        choices=TendencyType.choices,
        default=TendencyType.EQ,
    )
    numerator = models.ForeignKey(
        DataType,
        models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )
    denominator = models.ForeignKey(
        DataType,
        models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )
