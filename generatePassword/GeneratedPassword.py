import random
import re

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
digits = "1234567890"
special = r"`~!@#$%^&*()_+|}{“:?><[]\;',./-="
def weakPass(): # Weak Password
    weak = upper+lower
    length = random.randint(5,7)
    text = ""
    for i in range(length):
        text+=random.choice(weak)
    return text

def moderatePass(): # Moderate Password
    moder = upper+lower+digits
    length = random.randint(8,12)
    text=""
    for i in range(length):
        text+=random.choice(moder)
    return text

def strongPass(): # Strong Password
    strong = upper + lower + digits + special
    length = random.randint(13, 20)
    text = ""
    for i in range(length):
        text += random.choice(strong)
    return text
