import re

#opening the file
fs = open("extraction1.txt", "r")

allDataInOneList = []

for i in fs.readlines():
    for j in i.split(' '):
        allDataInOneList.append(j)

# allDataInOneList contains each work separately 
# now its time to manipulate the data with regex


listOfListWithEachEntry = []
dateRepetitionTracker = 0
EntryRepetitionTracker = 0

for i in allDataInOneList:
    pattern1 = re.compile("\d\d-\w\w\w-\d\d") # 33-Mar-43
    pattern2 = re.compile("\d-\w\w\w-\d\d") # 5-Jul-34
    pattern3 = re.compile("\d-\w\w\w\d") # 6-Mar6
    pattern4 = re.compile("\d-\w\w\w-\d") # 4-mar-3

    if dateRepetitionTracker == 0:
        listOfListWithEachEntry.append([])
    if pattern1.match(i) or pattern2.match(i) or pattern3.match(i) or pattern4.match(i):
        dateRepetitionTracker = dateRepetitionTracker + 1
        listOfListWithEachEntry[EntryRepetitionTracker].append(i)


        # Resetting the repetition date data & incrementing field list
        if dateRepetitionTracker == 3:
            dateRepetitionTracker = 0
            EntryRepetitionTracker = EntryRepetitionTracker + 1

print('listoflistwitheachentry : ', listOfListWithEachEntry)
print('daterepetitiontracker', dateRepetitionTracker)
print('entryrepetitiontraker', EntryRepetitionTracker)