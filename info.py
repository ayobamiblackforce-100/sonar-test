import requests
import subprocess
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


r = subprocess.run(['hostname -i && curl ifconfig.me'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
a = r.stdout.decode()
# url = 'https://142.93.36.242:8082/connections'
# res = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data), verify=False)
print(a)
