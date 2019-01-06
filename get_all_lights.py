import requests

ip_input = input("Please enter the IP Address of your Hue Bridge: ")
ip_address = str(ip_input)

user_input = input("Please enter your user: ")
user = str(user_input)

url = "http://" + ip_address + "/api/" + user + "/lights"

response = requests.get(url)

print(response.json())