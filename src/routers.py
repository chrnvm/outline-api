from fastapi import APIRouter
from fastapi import Response
from outline_api import *


all_keys_router = APIRouter(
    prefix="/api/keys",
    tags=["All keys"]
)


key_router = APIRouter(
    prefix="/api/key",
    tags=["Single key"]
)


server_router = APIRouter(
    prefix="/api/server",
    tags=["Server"]
)


@all_keys_router.get("/")
def get_keys(response: Response):
    try:
        return get_all_keys()
    except Exception as e:
        response.status_code = 500
        return {"Error": str(e)}
    

@all_keys_router.delete("/")
def delete_keys(response: Response):   
    try:
        delete_all_keys()
        response.status_code = 204
    except Exception as e:
        response.status_code = 500
        return {"Error": str(e)}
    

@key_router.get("/{id}")
def get_key(id: str, response: Response):
    try:
        return get_key_by_id(id)
    except Exception as e:
        response.status_code = 500
        return {"Error": str(e)}


@key_router.post("/add")
def add_key(response: Response):
    try:
        return create_key()
    except Exception as e:
        response.status_code = 500
        return {"Error": str(e)}


@key_router.put("/rename")
def rename_key(id: str, new_name: str, response: Response):
    status = rename_key_by_id(id, new_name)
    if status:
        return get_key_by_id(id)
    else:
        response.status_code = 500
        return {"Error": "Failed to rename"}


@key_router.delete("/delete/{id}")
def delete_key(id: str, response: Response):
    status = delete_key_by_id(id)
    if status:
        response.status_code = 204
    else:
        response.status_code = 500
        return {"Error": "Failed to delete"}


@key_router.put("/limit")
def set_key_limit(id: str, new_limit: int, response: Response):
    status = set_limit_by_key_id(id, new_limit)
    if status:
        return get_key_by_id(id)
    else:
        response.status_code = 500  
        return {"Error": "The limit could not be set"} 


@key_router.delete("/limit/{id}")
def reset_key_limit(id: str, response: Response):
    status = reset_limit_by_key_id(id)
    if status:
        return get_key_by_id(id)
    else:
        response.status_code = 500
        return {"Error": "The limit could not be deleted"} 


@server_router.get("/info")
def get_server_info(response: Response):
    try:
        return get_server_information()
    except Exception as e:
        response.status_code = 500
        return {"Error": str(e)}


@server_router.put("/name")
def edit_name(name: str, response: Response):
    status = edit_server_name(name)
    if status:
        return get_server_information()
    else:
        response.status_code = 500
        return {"Error": "Failed to rename the server"} 


@server_router.put("/hostname")
def edit_hostname(hostname: str, response: Response):
    status = edit_server_hostname(hostname)
    if status:
        return get_server_information()
    else:
        response.status_code = 500
        return {"Error": "Failed to change the hostname"} 


@server_router.put("/metrics")
def edit_metrics(metrics: bool, response: Response):
    status = enable_server_metrics(metrics)
    if status:
        return get_server_information()
    else:
        response.status_code = 500
        return {"Error": "Unable to enable/disable access to metrics"} 


@server_router.put("/port")
def edit_port(port: int, response: Response):
    status = edit_server_port(port)
    if status:
        return get_server_information()
    else:
        response.status_code = 500
        return {"Error": "The port could not be changed"} 


@server_router.put("/limit")
def edit_limit(limit: int, response: Response):
    status = edit_server_data_limit(limit)
    if status:
        return get_server_information()
    else:
        response.status_code = 500
        return {"Error": "The limit for the server could not be changed"} 


@server_router.delete("/limit")
def reset_limit(response: Response):
    status = delete_server_data_limit()
    if status:
        return get_server_information()
    else:
        response.status_code = 500
        return {"Error": "Failed to disable the limit for the server"} 
