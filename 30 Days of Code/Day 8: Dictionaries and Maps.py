n=int(input())
dict={}
for i in range(0,n):
    contact=str(input()).split(" ")
    name=contact[0]
    phone=int(contact[1])
    dict[name]=phone
while True:
    name=input()
    if name in dict:
        phone = dict[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
