from tortoise.models import Model
from tortoise import fields


class Users(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField()
    times = fields.IntField(default=0)
    balance = fields.IntField(default=0)