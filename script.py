import requests

r = requests.get("http://localhost/poultry/api/partners.php")
print(r.ok)
print(r.text)