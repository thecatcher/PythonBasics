xiaoming={"name":"xiaoming",
          "age":18,
          "genger":"male",
          "hight":1.75}

print(xiaoming)


# 1.get vlaue
print(xiaoming["name"])
print(xiaoming.get("name"))
# 2.add and modify

xiaoming["weight"] = 90
xiaoming["name"] = "xiaoxiaoming"
print(xiaoming)


# 3.delete
print(xiaoming.pop("weight"))


print(xiaoming)