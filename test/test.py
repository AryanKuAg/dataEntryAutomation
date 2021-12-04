import re

the = "The police loves nothing but police"
x = re.search("police", the)
print(x)
# fs = open("extraction1.txt", "r")

# def giveList(text):
#     print(text)
#     return []

# # print(giveList(fs.readlines()))
# giveList(fs.read())
# # f = open("demofile2.txt", "a")
# # f.write(fs.read())
# # f.close()
# # fs.close()