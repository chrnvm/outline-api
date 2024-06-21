from outline_vpn.outline_vpn import OutlineVPN
from config import OUTLINE_API_URL, OUTLINE_CERT
from utils import get_format_value, get_unit


outline_client = OutlineVPN(api_url=OUTLINE_API_URL, cert_sha256=OUTLINE_CERT)


def get_all_keys():
    
    keys = outline_client.get_keys()
    keys_list = []
   
    for key in keys:

        usage_value = None
        usage_units = None
        limit_value = None
        limit_units = None

        if (key.used_bytes):
            usage_value = get_format_value(key.used_bytes)
            usage_units = get_unit(key.used_bytes)

        if (key.data_limit):
            limit_value = get_format_value(key.data_limit)
            limit_units = get_unit(key.data_limit)

        key_data = {"id": key.key_id,
                    "name": key.name,
                    "access_url": key.access_url,
                    "used_bytes": key.used_bytes,
                    "usage_value": usage_value,
                    "usage_units": usage_units,
                    "limit_bytes": key.data_limit,
                    "limit_value": limit_value,
                    "limit_units": limit_units}
        keys_list.append(key_data)

    return keys_list


def delete_all_keys():
   
    keys = outline_client.get_keys()
    for key in keys:
        outline_client.delete_key(key.key_id)


def get_key_by_id(id: str):
    
    key = outline_client.get_key(id)

    limit_value = None
    limit_units = None

    if(key.data_limit):
        limit_value = get_format_value(key.data_limit)
        limit_units = get_unit(key.data_limit)    

    return_data = {"id": key.key_id, 
                   "name": key.name, 
                   "access_url": key.access_url,  
                   "usage_bytes": key.used_bytes, 
                   "limit_bytes": key.data_limit,
                   "limit_value": limit_value,
                   "limit_units": limit_units}
    
    return return_data


def create_key():
    new_key = outline_client.create_key()
    return new_key


def rename_key_by_id(id: str, name: str):
    status = outline_client.rename_key(id, name)
    return status


def delete_key_by_id(id: str):
    status = outline_client.delete_key(id)
    return status


def set_limit_by_key_id(id: str, limit: int):
    status = outline_client.add_data_limit(id, limit)
    return status


def reset_limit_by_key_id(id: str):
    status = outline_client.delete_data_limit(id)
    return status


def get_server_information():
    
    info = outline_client.get_server_information()

    if('accessKeyDataLimit' not in info):
        limit = None
        limit_value = None
        limit_units = None
    else:
        limit = info['accessKeyDataLimit']['bytes']
        limit_value = get_format_value(limit)
        limit_units = get_unit(limit)


    transferred_data = outline_client.get_transferred_data()
    total_month_usage = sum(transferred_data['bytesTransferredByUserId'].values())
    usage_value = get_format_value(total_month_usage)
    usage_units = get_unit(total_month_usage)

    return_data = {"name": info['name'], 
                   "port": info['portForNewAccessKeys'], 
                   "host": info['hostnameForAccessKeys'], 
                   "url": OUTLINE_API_URL, 
                   "created_at": info['createdTimestampMs'], 
                   "server_id": info['serverId'], 
                   "version": info['version'], 
                   "limit": limit, 
                   "limit_value": limit_value,
                   "limit_units": limit_units,
                   "metrics": info['metricsEnabled'],
                   "usage_bytes": total_month_usage,
                   "usage_value": float(usage_value),
                   "usage_units": usage_units}
    
    return return_data


def edit_server_name(name: str):
    status = outline_client.set_server_name(name)
    return status


def edit_server_hostname(hostname: str):
    status = outline_client.set_hostname(hostname)
    return status


def enable_server_metrics(metrics: bool):
    status = outline_client.set_metrics_status(metrics)
    return status


def edit_server_port(port: int):
    status = outline_client.set_port_new_for_access_keys(port)
    return status


def edit_server_data_limit(limit: int):
    status = outline_client.set_data_limit_for_all_keys(limit)
    return status


def delete_server_data_limit():
    status = outline_client.delete_data_limit_for_all_keys()
    return status