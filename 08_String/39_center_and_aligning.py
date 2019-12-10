prem_str = ["登鹳雀楼", "王之涣", "白日依山尽", "黄河入海流", "欲穷千里目", "更上一层楼"]

# center
for each_str in prem_str:
    print("|%s|" % each_str.center(10, "　"))

# left aligning

for each_str in prem_str:
    print("|%s|" % each_str.ljust(10, "　"))

# right aligning

for each_str in prem_str:
    print("|%s|" % each_str.rjust(10, "　"))
