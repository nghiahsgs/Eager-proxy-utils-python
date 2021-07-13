import requests
import os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('host')
port = os.getenv('port')


def get_info_list_dcom():
    url = f'http://{host}:{port}/api/v1/dongles/all'
    data = requests.get(url).json()
    data = [
        {
            'id':e['id'],
            'device_name':e['deviceName'],
            'imei':e['imei'],
            'dcom_port' : e['httpPort'],
            'ipv4' : e['publicIPv4Address'],
            'isp':e['isp'],
            'last_reset' : e['lastReset']
        }for e in data
    ]
    return data
    

# Thay đổi ip theo port
def change_ip_dcom(dcom_port):
    url = f'http://{host}:{port}/reset?proxy={dcom_port}'
    data = requests.get(url).json()
    return data['status'] #True
    

def check_is_ready_dcom(dcom_port):
    url = f'http://{host}:{port}/status?proxy={host}:{dcom_port}'
    data = requests.get(url).json()
    return data['status']


if __name__ =="__main__":
    # data = get_info_list_dcom()
    # print(data)

    # dcom_port = '4000'
    # data = change_ip_dcom(dcom_port)
    # print(data)

    dcom_port = '4000'
    data = check_is_ready_dcom(dcom_port)