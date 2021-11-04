# file=open("data.txt",mode="w",encoding="UTF-8")
# file.write("hello file\nSecond Line\n")
# file.write("測試中文\n好棒棒")
# file.close()

# with open("data.txt",mode="w",encoding="utf-8") as file:
#     file.write("測試中文\n好棒棒")

# with open("data.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
# print(data)

# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
#     for line in file:
#         sum=sum+int(line)
# print(sum)
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data)   #data是一個字典
print("name:",data["name"])
print("version:",data["version"])
