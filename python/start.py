s1 = int(input("請輸入數字1："))
s2 = int(input("請輸入數字2："))
op = input("請輸入運算符 +，-，*，/ ：")
if op == "+":
    print(s1+s2)
elif op == "-":
    print(s1-s2)
elif op == "*":
    print(s1*s2)
elif op == "/":
    print(s1/s2)
else:
    print("不支援")