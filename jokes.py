import requests

# print(response.json())

print("want to hear a joke,type 'yes' every time and type 'exit'to quit")
while True:
    asking = input("type ;").strip().lower()

    if asking == "exit":
        print("goodbye")
        break
    elif asking == "yes":
        response = requests.get(
            "https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke = response.json()
            print(f"{joke['setup']} - {joke['punchline']}")
        else:
            print("couldn't fetch a joke right now. Try again later.")
    else:
        print("type 'yes' to hear a joke or 'exit' to quit")
