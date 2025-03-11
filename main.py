from flask import Flask, jsonify, request
import requests, random

base_url = "https://dev.api.gabriel.money/backend-challenge/"
userID = '375b799c-d2d4-4290-ba8a-3f32d4f5ca92'
aggregated = {"userInfo" : "", "accountsInfo" : "", "cardsInfo" : "", "transactionsInfo" : ""}
#userInfo = [{}]

app = Flask(__name__)

clients = [{"userId": "1234", "first_name": " John", "last_name": "Doe", "email": "john.doe@example.com", "phone_number": "+19709456544"},
          {"userId": "5678", "first_name": " Timothy", "last_name": "Cook", "email": "tim.cook@example.com", "phone_number": "+19709758544"}
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
    newId = random.randint(1000, 9999)
    new_client = {"userId": newId, "first_name": request.json["first_name"], "last_name": request.json["last_name"], "email": request.json["email"], "phone_number": request.json["phone_number"]}
    clients.append(new_client)
    return {"userID" : newId}


#Updates client information
@app.route('/users/<int:id>', methods = ['PUT'])
def updateClient(id):
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

#Gets info from third-party API
@app.route('/users/<int:id>/aggregated-info', methods = ['GET'])
def getUserInfo(id):
    getUser()
    getAccounts()
    getCards()
    getTransactions()

    return aggregated

#Gets user info from third-party API
def getUser():
    url = f'{base_url}/users/{userID}'
    response = requests.get(url)

    if response.status_code == 200:
        aggregated.update({"userInfo" : response.json()})
    else:
        print(f"Failed to retrieve data {response.status_code}")

#Gets accounts info from third-party API
def getAccounts():
    url = f'{base_url}/accounts/{userID}'
    response = requests.get(url)

    if response.status_code == 200:
        aggregated.update({"accountsInfo" : response.json()})
    else:
        print(f"Failed to retrieve data {response.status_code}")

#Gets cards info from third-party API
def getCards():
    url = f'{base_url}/cards/{userID}'
    response = requests.get(url)

    if response.status_code == 200:
        aggregated.update({"cardsInfo" : response.json()})
    else:
        print(f"Failed to retrieve data {response.status_code}")

#Gets transactions info from third-party API
def getTransactions():
    url = f'{base_url}/transactions/{userID}'
    response = requests.get(url)

    if response.status_code == 200:
        aggregated.update({"transactionsInfo" : response.json()})
    else:
        print(f"Failed to retrieve data {response.status_code}")


#Runs the Flask app
if __name__ == '__main__':
    app.run(debug = True)