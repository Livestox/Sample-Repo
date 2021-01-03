import math
import sys
from os import rename

import requests


print(sys.api_version)
# print(sys.executable)
def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("http://localhost/poultry/api/partners.php")
# print(r.text)
