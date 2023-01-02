from typing import Optional
from fastapi import FastAPI
import uvicorn
from tortoise import Tortoise
from Base_Model.Model_Users import Users
import json
from loguru import logger as log

app = FastAPI()

@app.on_event("startup")
async def a():
    log.info('Tortoise is running')
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['Base_Model.Model_Users']}
    )
    await Tortoise.generate_schemas()


@app.get('/{user_id}')
async def getter(filters: Optional[str]) -> Optional[dict]:
    filters: Optional[dict] = json.loads(filters)
    Object = Users.filter(**filters)
    if await Object is None:
        return {'running': False, 'data': None}
    else:
        return {'running': True, 'data': await Object.first()}

@app.get('/creaters/')
async def creater(filters: Optional[str], params: Optional[str]) -> dict:
    filters: Optional[dict] = json.loads(filters)
    params: Optional[dict] = json.loads(params)
    Object = Users.filter(**filters)
    if await Object.first() is None:
        await Users.create(**params)
        return {'running': True, 'data': await Object.first()}
    else:
         return {'running': False, 'data': await Object.first()}

    


@app.get('/updater/')
async def updater(filters: Optional[str], params: Optional[str]) -> dict:
    filters: Optional[dict] = json.loads(filters)
    params: Optional[dict] = json.loads(params)
    Object = Users.filter(**filters)
    if await Object.first() is None:
        return {'running': False, 'data': None}
    else:
        await Object.update(**params)
        return {'running': True, 'data': await Object.first()}
        
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info')
