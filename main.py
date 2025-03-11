from flask import Flask, jsonify, request

base_url = "https://dev.api.gabriel.money/backend-challenge/"
userID = '375b799c-d2d4-4290-ba8a-3f32d4f5ca92'
userInfo = []

app = Flask(__name__)

clients = [{"userId": "abcd", "first_name": " John", "last_name": "Doe", "email": "john.doe@example.com", "phone_number": "+19709456544"},
          {"userId": "efgh", "first_name": " Timothy", "last_name": "Cook", "email": "tim.cook@example.com", "phone_number": "+19709758544"}
]

#Returns a list with all the clients
@app.route('/users', methods = ['GET'])
def getClients():
    return clients

#Searches for one specific client using its ID
@app.route('/users/<int:id>', methods = ['GET'])
def getClient(id):
    for client in clients:
        if client["userId"] == id:
            return client
        
    return {"error" : "Client ID not found"}

#Adds new client to the list
@app.route('/users', methods = ['POST'])
def addClient():
    new_client = {"userId": "", "first_name": request.json["first_name"], "last_name": request.json["last_name"], "email": request.json["email"], "phone_number": request.json["phone_number"]}
    clients.append(new_client)
    return {"userID" : ""}


#Updates client information
@app.route('/users/<int:id>', methods = ['PUT'])
def getClient(id):
    updates = request.json.keys()
    for client in clients:
        if client["userId"] == id:
            for update in updates:
                client[update] = request.json[update]
            return client
        
    return {"error" : "Client ID not found"}

#Deletes one specific client using its ID
@app.route('/users/<int:id>', methods = ['DELETE'])
def deleteClient(id):
    for client in clients:
        if client["userId"] == id:
            clients.remove(client)
            return {"message" : "User {} deleted successfully".format(id)}
        
    return {"error" : "Client ID not found"}

#Gets user info from third-party API
@app.route('/users/<int:id>/aggregated-info', methods = ['GET'])
def deleteClient(id):
    getUser()
    getAccounts()
    getCards()
    getTransactions()

    return userInfo

    #return {"error" : "Client ID not found"}

def getUser():
    url = f'{base_url}/users/{userID}'
    response = request.get(url)

    if response.status_code == 200:
        userInfo.append(response.json())
    else:
        print(f"Failed to retrieve data {response.status_code}")

def getAccounts():
    url = f'{base_url}/accounts/{userID}'
    response = request.get(url)

    if response.status_code == 200:
        userInfo.append(response.json())
    else:
        print(f"Failed to retrieve data {response.status_code}")

def getCards():
    url = f'{base_url}/cards/{userID}'
    response = request.get(url)

    if response.status_code == 200:
        userInfo.append(response.json())
    else:
        print(f"Failed to retrieve data {response.status_code}")

def getTransactions():
    url = f'{base_url}/transactions/{userID}'
    response = request.get(url)

    if response.status_code == 200:
        userInfo.append(response.json())
    else:
        print(f"Failed to retrieve data {response.status_code}")


#Runs the Flask app
if __name__ == '__main__':
    app.run(debug = True)