import os
import requests
from dotenv import load_dotenv
load_dotenv()

# host = os.getenv('host')
# dcom_port = '4001'

host = '192.168.0.102'
dcom_port = '4000'

http_proxy  = f"http://{host}:{dcom_port}"
https_proxy = f"https://{host}:{dcom_port}"
proxyDict = { 
    "http"  : http_proxy, 
    "https" : https_proxy
}
# url = 'https://api.myip.com'
url = 'http://httpbin.org/ip'
res = requests.get(url, proxies=proxyDict).json()
print(res)