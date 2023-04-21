import requests

data = {"entry": {
  "name": "Jakob Rolandsson",
  "number": "0725080995",
  "address": "Häraldsvägen 3B"
}}


#r = requests.post("http://127.0.0.1:5000/phonebook", json=data)

check = True
while check:

  print(
    "Menu:\n",
    "1. Get all entries\n",
    "2. Get by name\n",
    "3. Get by address\n",
    "4. Get by rows\n",
    "5. Delete Full name\n",
    "0 to exit\n"
  )

  query = input("Enter a number: ")

  while query != 0:

    if query == "1":
      
      r = requests.get("http://127.0.0.1:5000/phonebook")
      n = 0
      limit = len(r.json())
      print(limit)
      for entry in r.json():
        print(n, entry["name"], entry["number"], "-", entry["address"], "\n")
        n += 1
        if n == limit:
          break
      break

    elif query == "2":
      name = input("Enter name: ").capitalize()
      r = requests.get("http://127.0.0.1:5000/phonebook/name/"+name)
      print("\n")
      for entry in r.json():
        if name in entry["name"]:
          print(entry["name"], entry["number"], "-", entry["address"], "\n")
      break

    elif query == "3":
      adress = input("Enter adress: ").capitalize()
      r = requests.get("http://127.0.0.1:5000/phonebook/adress/"+adress)
      print("\n")
      for entry in r.json():
        if adress in entry["address"]:
          print(entry["name"], entry["number"], "-", entry["address"], "\n")
        else:
          print("No match")
      break


    elif query == "4":
      rows = input("Enter number of rows: ")
      r = requests.get("http://127.0.0.1:5000/phonebook/"+str(rows))
      print("\n")
      for entry in r.json():
        print(entry["name"], entry["number"], "-", entry["address"], "\n")
      break

    #elif query == "5":
    #  name = input("Enter name: ")
    #  name = name.split()
    #  name = name[0].capitalize() + "%20" + name[1].capitalize()
    #  r = requests.get("http://127.0.0.1:5000/phonebook/del/"+name)
    #  break

    elif query == "0":
      print("Exiting")
      check = False
      break

    else:
      print("Invalid input")
      break
  
    
