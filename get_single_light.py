import requests

ip_input = input("Please enter the IP Address of your Hue Bridge: ")
ip_address = str(ip_input)

user_input = input("Please enter your user: ")
user = str(user_input)

light_id_input = input("Please enter your light id: ")
light_id = str(light_id_input)

url = "http://" + ip_address + "/api/" + user + "/lights/" + light_id
response = requests.get(url)

print(response.json())
