import requests
from typing import Optional
import json
from loguru import logger as log
base = '127.0.0.1:8000'

class Base:

    def requester(self, url: Optional[str], params: Optional[dict]) -> Optional[dict]:
        try:
            return requests.get(url=url, params=params).json()
        except Exception as error:
            return {'running': False, 'data': error}


    def updates(self, filters: Optional[dict], params: Optional[dict]) -> Optional[dict]:
        log.info(f'Updates -> From[ filter | {filters} params | {params}]')
        data: Optional[dict] = {'filters': json.dumps(filters), 'params': json.dumps(params)}
        url: Optional[str] = f'http://{base}/updater/'
        return self.requester(url, data)



    def getter(self, user_id: Optional[int], filters: Optional[dict]):
        log.info(f'Getter -> From[user_id | {user_id} filter | {filters}]')
        data: Optional[dict] = {'filters': json.dumps(filters)}
        url: Optional[str] = f'http://{base}/{user_id}/'
        return self.requester(url, data)

    def creater(self, filters: Optional[dict], params: Optional[dict]) -> dict:
        log.info(f'creater -> From[ filter | {filters} params | {params}]')
        data: Optional[dict] = {'filters': json.dumps(filters), 'params': json.dumps(params)}
        url: Optional[str] = f'http://{base}/creaters/'
        return self.requester(url, data)
