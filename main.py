import requests
from datetime import date
USERNAME = "shreyaa"
TOKEN = "heusjsiekowlqke"
GRAPHID = "mygraph1"

# Making a post request to create a pixela user account
pixela_endpoint = "https://pixe.la/v1/users"

# a token is like a API key that you make up yourself
user_params = {
    "token": "heusjsiekowlqke",
    "username": "shreyaa",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
#We have now created a new user account in pixela with a secret token

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Creating a graph definition-need to paste in a url at the end to get the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "mygraph1",
    "name": "Minutes Spent Coding",
    "unit": "minute",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


requests.post(url=graph_endpoint,json=graph_params, headers=headers)

#Posting a value to my graph

value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

value_params = {
   "date": "20220609",
    "quantity": "300",
}

requests.post(url=value_endpoint,json=value_params, headers=headers)

#Updating a value on graph-using a put request
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20220611"

put_params = {
    "quantity": "500"
}

requests.put(url=put_endpoint,json=put_params, headers=headers)