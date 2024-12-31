import time
import os
default = '\033[0m'
yellow= '\033[33m'
green= '\033[32m'

print("Contact Card Generator")
print()
time.sleep(1)
print("We will now ask you some questions to create your contact card.")
print()
time.sleep(1)

name = input("What is your Name?: ").strip().title()
print()
dob = input("What is your Date of Birth?: ").strip()
print()
telephone = input("What is your Telephone Number? ").strip()
print()
email = input("What is your Email Address?: ").strip()
print()
address = input("What is your Home Address?: ")
print()
time.sleep(2)
os.system("clear")

userInfo = {"name": name, "dob": dob, "tel": telephone, "email": email, "address": address}

print("Please be patient while I prepare your Contact Card")
time.sleep(3)
os.system("clear")
print()
print(f"{green}Contact Card{default}")
print()
time.sleep(1)

print(f"{yellow}Name: {userInfo['name']}\nDOB: {userInfo['dob']}\nTel: {userInfo['tel']}\nEmail: {userInfo['email']}\nAddress: {userInfo['address']}")
