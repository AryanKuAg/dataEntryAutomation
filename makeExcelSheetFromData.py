from openpyxl import Workbook
wb = Workbook()

try:
  for i in range(1, 100):
    f = open("extraction" + str(i) +".txt", "r")
    # print(f.read())


    ws = wb.active

    # OUR MAIN ISSUE
    for j in f.readlines():
        ws.append([i.split(' ')[0],i.split(' ')[1],i.split(' ')[2],i.split(' ')[3],i.split(' ')[4]])

    # ws.append([1,3,5,43])

    wb.save('result' + str(i)+'.xlsx')
    f.close()
except Exception as e:
  print("An exception occurred: ", e) 

# def giveListData(text):
#     return text.split(' ')