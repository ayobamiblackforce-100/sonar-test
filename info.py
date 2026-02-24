import json
import time
import requests
import subprocess
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = 'https://142.93.36.242:8082/connections?status=test'
res = requests.get(url, headers={'Content-Type': 'application/json'}, verify=False)
if res.status_code==200:
  time.sleep(10)
  print(res.json()['data'][-1][1])
