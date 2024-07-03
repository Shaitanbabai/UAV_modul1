# with open("bpla_storage_info.csv", "r", encoding="utf-8") as file:
#     title = file.readline()
#     content = file.readlines()
# print(title)
# print(content)

with open("bpla_storage_warehouse.csv", "r", encoding="utf-8") as file:
    title = file.readline()
    content = file.read()
    content = content.split("\n")

for i in range(len(content)):
    content[i] = content[i].split(",")

print(content)