import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input("Enter the URL: ")
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip, api_key='free')

print(f"IP: {ip}")
print(f"City: {response.city}")
print(f"Region: {response.region}")
print(f"Country: {response.country}")