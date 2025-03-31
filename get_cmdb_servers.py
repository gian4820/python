import requests

# Set up authentication
username = 'admin'
password = 'Ovofn$T6I*B9'
auth = (username, password)

# Set up the API endpoint
instance = 'dev175451'
url = f'https://{instance}.service-now.com/api/now/table/cmdb_ci_server'

# Make the GET request
response = requests.get(url, auth=auth)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the list of CMDB servers
    servers = data['result']
    # Print or process the list of servers as needed
    for server in servers:
        print(server)
else:
    print("Failed to retrieve CMDB servers:", response.text)
