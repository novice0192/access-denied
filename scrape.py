import certifi
import requests
from time import sleep

base_url = r'https://ceodaman.nic.in/ElectoralRoll/PhotoER2022_F/pdf/English/A001'
end_url = r'.PDF'
for x in range(1, 100):
    url = base_url + "{:04}".format(x) + end_url
    r = requests.get(url, allow_redirects=True, verify=False)
    file = open("andaman\\" + "{:03}".format(x) + '.PDF', 'wb')
    file.write(r.content)
    file.close()
    print(x, "done")
for x in range(100, 153):
    url = base_url + "{:05}".format(x) + end_url
    r = requests.get(url, allow_redirects=True, verify=False)
    file = open("andaman\\" + "{:03}".format(x) + '.PDF', 'wb')
    file.write(r.content)
    file.close()
    print(x, "done")
print("done")
