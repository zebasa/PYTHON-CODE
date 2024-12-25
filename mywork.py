while True:
    num=int(input("how many times:  "))
    if num>=5:
        print("maximum amount of times it will iterate is 5 times ")
        continue
    else:
        break
    
for _ in range(num):
    print("meow")

while True:
    num=int(input("add a number "))
    if num<=0:
        print("your number should be higher than 0 ")
        continue
    else:
        print(num)
        break
students=["hermon","tom","jon","michael"]
print(students[0])



password="zebulun"
no=0
print("you were idle for 15 minutes so you have been logged out")
while True:
    p1=input("enter your password:         ")
    if p1==password:
            print("You now have access to your account")
            break
    if p1!=password:
        print("Wrong password")
        no=no+1
        if no==5:
            print("You are locked from the account")
            break
        

names=["jon","michael","judith"]
for name in range(len(names)):
    print(name + 1, names[name])



print("hello\n"*5, end="")
which=input("what name are you looking for")
birthnames={"zebulun":"asante","michael":"anthony","samuel":"john"}
for which in birthnames:
    print(which ,birthnames[which],sep=", ")




def main():
    jump_high(4)

def jump_high(high):
    for _ in range(high):
        print("TO THE SKYYYYYYYYYYY")
main()

def hello():
    que_stion(4)
def que_stion(mark):
    print("?"* mark)
hello()

fullnames=[
    {"name":"zebulun","sirname":"asante"}
    {"name":"judith","sirname":"anthony"}
    {"name":"michael","sirname":"richards"}
]
print(fullnames["name"],fullnames["sirname"])
