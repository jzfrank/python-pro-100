import requests 
import datetime as dt 
import math
import os 

TOKEN = os.environ.get("API_KEY") 
USER_NAME = "frankjinzhang"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"


# params = {
# 	'token': TOKEN,
# 	'username': USER_NAME,
# 	'agreeTermsOfService': "yes",
# 	'notMinor': 'yes'
# }

# graph_config = {
# 	"id": GRAPH_ID,
# 	"name": "Cycling Graph",
# 	"unit": "Km",
# 	"type": "float",
# 	"color": "ajisai"
# }
DATE = dt.datetime.today().strftime("%Y%m%d")

headers = {
	"X-USER-TOKEN": TOKEN
}

today = dt.datetime.today()
graph_post_config = {
	'date': today.strftime("%Y%m%d"),
	'quantity': '14'
}

print(today.strftime("%Y%m%d"))

response = requests.post(
	url=graph_endpoint + "/" + GRAPH_ID, 
	json=graph_post_config, headers=headers)

graph_put_config = {
	'quantity': f"{math.pi}"
}

print("DATE:", DATE)

# response = requests.put(
# 	url=f"{graph_endpoint}/{GRAPH_ID}/{DATE}", 
# 	json=graph_put_config, headers=headers)

# response = requests.delete(
# 	url=f"{graph_endpoint}/{GRAPH_ID}/{DATE}",
# 	headers=headers)

print(response.text)


