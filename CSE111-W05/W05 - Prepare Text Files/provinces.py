provinces_list = []
count = 0

with open("provinces.txt", "rt") as provinces:
    for i in provinces:
        clean_line = i.strip()
        provinces_list.append(clean_line)
        if clean_line == "Alberta":
            count += 1
    print(provinces_list)

print(count)
