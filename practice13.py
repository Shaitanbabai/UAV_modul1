with open("bpla_storage_info.csv", "r", encoding="utf-8") as file:
    title = file.readline()
    content = file.readlines()
print(title)
print(content)
