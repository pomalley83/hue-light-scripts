import requests

ip_input = input("Please enter the IP Address of your Hue Bridge: ")
ip_adress = str(ip_input)

user_input = input("Please enter your user: ")
user = str(user_input)

light_id_input = input("Please enter your light id: ")
light_id = str(light_id_input)

state_input = input("Please enter if the light should be switched on or off: ")
state = str(state_input)

if state == "on":
    state = "true"
elif state == "off":
    state = "false"
else:
    state = "false"

url = "http://" + ip_adress + "/api/" + user + "/lights/" + light_id + "/state"
data = '''{
    "on":''' + state + '''
}'''

response = requests.put(url, data=data)

print(response.json())
