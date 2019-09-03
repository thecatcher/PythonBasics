i = 0

while i < 10:
    if i == 7:
        print("continue is triggered! i = %d" % i)
        i = i + 1
        continue
    print("i = %d " % i)
    i = i + 1
print("continue and pass")
