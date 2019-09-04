name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引
print(name_list[2])

# 知道数据内容，确定索引值
print(name_list.index("lisi"))

# 2.修改
name_list[1] = "李四"

# 3.增加数据
# 在指定的索引位置插入数据
name_list.insert(1, "zhaoliu")
# 在列表末尾增加数据
name_list.append("xiaoqi")
# 追加一个列表到该列表之后
name_list.extend(["孙悟空", "猪八戒", "沙师弟"])

print(name_list)

# 4.删除

# 删除指定的元素
# name_list.remove("李四")
# print("after remove method:")
# print(name_list)

# 不解释，就是pop方法
# tmp = name_list.pop()
# print(tmp)
# print(name_list)

# # 清空列表
# name_list.clear()
# print("after clear method")
# print(name_list)

# del的本质是讲一个变量从内存中删除
# del name_list[1]
# print("after del keyword:")
# print(name_list)

# 统计相关
# print(len(name_list))
#
# name_list.append("zhaoliu")
#
# print(name_list.count("zhaoliu"))

number_list = [1, 2, 3, 2, 5, 4, 3, 1, 7]

print(number_list)

number_list.reverse()

print(number_list)

number_list.sort(reverse=True)

print(number_list)