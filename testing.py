import requests

# define the endpoint URL
url = "http://127.0.0.1:7000/template"

# define the data to be sent to the API endpoint
data = {"mid_score": 90, "overall_mid_weight": 50, "mid_weight": 25,
        "final_score": 80, "overall_final_weight": 50, "final_weight": 10}

# send a POST request to the API endpoint
response = requests.post(url, json=data)

# check if the request was successful
if response.status_code == 200:
    # print the response content
    print(response.content)
else:
    # handle the error
    print(f"Error: {response.status_code}")
