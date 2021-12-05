from openpyxl import Workbook
import dataManipulation




try:
  for i in range(1, 3): #Increase range
    wb = Workbook()
    # f = open("extraction" + str(i) +".txt", "r")
    arrangedData = dataManipulation.dataManipulation('extraction' + str(i) + '.txt') #set file name here
    # print(arrangedData)
    # Get Arranged data in list of list


    ws = wb.active

    # OUR MAIN ISSUE
    for j in arrangedData: # This loop is adding data to worksheet
      lengthOfList = len(j)
      listOfData = []
      for just in range(0, lengthOfList):
        listOfData.append(j[just])
      ws.append(listOfData)
      listOfData = []
    

    # ws.append([1,3,5,43])
    
    wb.save('result' + str(i)+'.xlsx')
    wb.remove()
    
    
    
except Exception as e:
  print("An exception occurred: ", e) 

