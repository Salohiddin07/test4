from database import db

users = []
def add_user(id, name, lastname, age, address, email, phone):
    users.extend([id, name, lastname, age, address, email, phone])
    return users
id = 0

while True:
    id +=1 
    name = input("Name: ")
    last_name = input("Lastname: ")
    age = int(input('Age: '))
    address = input('Address: ')
    email = input("Email: ")
    phone = input("Phone: ")
    db.insert_users(name, last_name, age, address, email, phone)
    command = input("Programmani toxtatmoqchi bo'lsangiz 'stop' deb yozing toxtatmoqchi bo'lmasangiz xoxlagan harifingizni bosib ketavering: ")
    if command == "stop":
        print("Dastur to'xtadi ")
        break
    print(add_user(id, name, last_name, age, address, email, phone))
     


