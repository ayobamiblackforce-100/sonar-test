#/usr/bin/bash

apt install python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install pip-audit
pip-audit -r requirements.txt > pip-audit-ouput.txt
