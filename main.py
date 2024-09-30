import os

messages = []

name = input("Name: ")

while True:
    os.system('cls')
    
    if len(messages) > 0:
        for i in messages: 
            print(i['name'], "-", i['text'])
    
    print("_________________________________")
    
    text = input("Message: ")
    if text == "end":
        break
    
    messages.append({
        "name": name,
        "text": text
    })