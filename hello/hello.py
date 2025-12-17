import sys

print("Hello from module!")
print("Args:", sys.argv[1:])

a = True

while a:
    b = input(">")
    if b == "close":
        a = False