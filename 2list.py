products=[]
while True:
    name=input("請輸入商品名：")
    if name== "q":
        break
    n=[]
    price=input("請輸入價格：")
    n.append(name)
    n.append(price)
    products.append(n)
print(products)


for p in products:
    print(p[0],"的價格是",p[1])

with open ("products.csv" , mode="w") as f:
    for p in products:
        f.write(p[0]+","+p[1]+"\n")
