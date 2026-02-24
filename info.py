import json
import time
import requests
import subprocess
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = 'https://142.93.36.242:8082/connections?status=test'
res = requests.get(url, headers={'Content-Type': 'application/json'}, verify=False, timeout=3)
if res.status_code==200:
  time.sleep(10)
  server = res.json()['data'][-1][1].strip()
  status = requests.get(f'http://{server}:8501', timeout=3)
  print(status.status_code)
