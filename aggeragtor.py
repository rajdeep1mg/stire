from sanic import Blueprint
from torpedo import Request,send_response
from app.models.db import Service

aggregator = Blueprint(name="aggregator", version=1)


@aggregator.get("/find-aggregator")
async def find_aggegator(request:Request):
    param = request.request_params()
    tag = param.get('tags')

    document = await Service.aggregate([{"$match":{"openapi.path":"/end_user/v7/pharmacy_home"}}]).to_list()
    print(document)
    return send_response({"ping":"pong"})



