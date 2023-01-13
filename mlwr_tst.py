# Requirements: Python3
# This script will run a HTTP Request, please use Python 3 to run it.
# Date of Change: 13 Jan 2023

import requests


print("""\
______  ___      ______                                  ________           _____ 
___   |/  /_____ ___  /__      _______ ____________      ___  __/_____________  /_
__  /|_/ /_  __ `/_  /__ | /| / /  __ `/_  ___/  _ \     __  /  _  _ \_  ___/  __/
_  /  / / / /_/ /_  / __ |/ |/ // /_/ /_  /   /  __/     _  /   /  __/(__  )/ /_  
/_/  /_/  \__,_/ /_/  ____/|__/ \__,_/ /_/    \___/      /_/    \___//____/ \__/  
                                                                                  
01001101 01100001 01101100 01110111 01100001 01110010 01100101  01010100 01100101 01110011 01110100 

***DISCLAIMER***
This script is for Malware Simulation Test...
Running in background...
                    """)

urls = ["http://malware.wicar.org/data/eicar.com", "http://malware.wicar.org/data/ms14_064_ole_xp.html", "http://malware.wicar.org/data/ms14_064_ole_not_xp.html", "http://malware.wicar.org/data/java_jre17_exec.html", "http://malware.wicar.org/data/ms03_020_ie_objecttype.html", "http://malware.wicar.org/data/ms05_054_onload.html", "http://malware.wicar.org/data/ms09_002_memory_corruption.html", "http://malware.wicar.org/data/ms09_072_style_object.html", "http://malware.wicar.org/data/ms10_090_ie_css_clip_ie6.html", "http://malware.wicar.org/data/firefox_proto_crmfrequest.html", "http://malware.wicar.org/data/vlc_amv.html", "http://malware.wicar.org/data/adobe_flash_hacking_team_uaf.html"] 

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'}

for url in urls:
    response = requests.get(url, headers=headers)
    print(f'{url} - {response.status_code}')
