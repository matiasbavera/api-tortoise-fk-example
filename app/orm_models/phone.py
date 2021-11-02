from tortoise import Tortoise, fields, models, run_async
from tortoise.models import Model


class Phone(Model):
    """
    The User model
    """

    id = fields.IntField(pk=True)
    number = fields.CharField(max_length=20, unique=True)
