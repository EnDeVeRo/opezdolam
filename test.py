from BaseReuests.Base_Requests import Base

base = Base()
filters = dict(user_id=1)
params = dict(user_id=1, times=13131, balance=3)
a = base.creater(filters, params)
print(a)