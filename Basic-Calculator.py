
def add(x, y):
    z = x + y
    return z

def subtract (x, y):
    z = x - y
    return z
    
def multiply(x, y):
    z = x * y
    return z
def divide (x, y):
    z = x / y
    return z    

print("Select Operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4. divide")

choice = input("Enter choice(1/2/3/4:")
while True:
    num1 = input("Enter First number: ")
    num2 = input("Enter seconed number:")
    try:
        num1 = int(num1)
        num2 = int(num2)
        break
    except:
        continue
if choice == "1":
    print(str(num1) + "+" + str(num2) + "=" + str(add(num1,num2)))
    input("")
else:
    if choice == "2":
        print(str(num1) + "-" + str(num2) + "=" + str(subtract(num1,num2)))
        input("")
    else:
        if choice == "3":
            print(str(num1) + "*" + str(num2) + "=" + str(multiply(num1,num2)))
            input("")
        else:
            if choice == "4":
                print(str(num1) + "/" + str(num2) + "=" + str(divide(num1,num2)))
                input("")
            else:
                print("Invalid Option")
                input("")