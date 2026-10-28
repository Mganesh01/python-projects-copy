import requests  # requests library ni import chestunnam

# Server nundi contestants list fetch cheyyadam
response = requests.get(
    "https://api.biggboss.com/contestants"
)

# Response data ni print cheyyadam
print(response.json())



[
    {
        "id": 1,
        "name": "Trigun",
        "age": 30
    },
    {
        "id": 2,
        "name": "Temper Vamsi",
        "age": 28
    },
    {
        "id": 3,
        "name": "Rohit",
        "age": 31
    },
    {
        "id": 4,
        "name": "Ram Prasad",
        "age": 35
    }
]



import requests

# Kotha contestant details
new_contestant = {
    "name": "Temper Vamsi",
    "age": 28
}

# Server lo new contestant create cheyyadam
response = requests.post(
    "https://api.biggboss.com/contestants",
    json=new_contestant
)

# Created data ni print cheyyadam
print(response.json())



import requests

# Complete profile details
updated_profile = {
    "name": "Rohit",
    "age": 30,
    "city": "Hyderabad"
}

# Existing profile ni complete ga replace cheyyadam
response = requests.put(
    "https://api.biggboss.com/contestants/1",
    json=updated_profile
)

# Updated profile ni print cheyyadam
print(response.json())




import requests

# Age maatrame update cheyyadam
response = requests.patch(
    "https://api.biggboss.com/contestants/1",
    json={"age": 31}
)

# Updated response ni print cheyyadam
print(response.json())