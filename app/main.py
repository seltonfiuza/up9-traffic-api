import requests
import pandas as pd
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import json
from pydantic import BaseModel
from app.util import filter_between_dates, URL_SINGLE_SERVICE_TRAFFIC, HEADER
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',)


app = FastAPI()


@app.on_event("startup")
async def startup():

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


class QueryModel(BaseModel):
    start_date: str
    end_date: str
    service: str
    token: str
    workspace: str


@app.get('/')
def hello():
    return ('Hello', 200)


@app.post("/traffic")
def get_traffic(query: QueryModel):
    try:
        HEADER['authorization'] = query.token
        url = (URL_SINGLE_SERVICE_TRAFFIC +
               f"http://{query.service}").replace('_workspace_', query.workspace)
        data = None
        with requests.get(url, headers=HEADER) as r:
            if r.status_code == 200 and r.text != "[]\n":
                data = pd.DataFrame(r.json())
        if data is not None:
            filtered_data = filter_between_dates(
                start_date=query.start_date, end_date=query.end_date, df=data)
            return json.loads(filtered_data.to_json(orient='records'))
    except Exception as e:
        return {'err': e}
    return {'message': 'Token expired'}
