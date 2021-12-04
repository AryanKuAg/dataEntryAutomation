import re

# opening the file
fs = open("extraction1.txt", "r")

allDataInOneList = []

for i in fs.readlines():
    for j in i.split(' '):
        allDataInOneList.append(j)

# allDataInOneList contains each work separately
# now its time to manipulate the data with regex
print(allDataInOneList)

listOfListWithEachEntry = []
dateRepetitionTracker = 0
EntryRepetitionTracker = 0

for i in allDataInOneList:
    # Right Code : it will add a new list or entry
    if dateRepetitionTracker == 0:
        listOfListWithEachEntry.append([])


    #11111111111111111111111111111111111111111111111111111111111111111111111111111111
    #111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    #2222222222222222222222222222222222222222222222222222222222222222222222222222222222
    #222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333
    #4444444444444444444444444444444444444444444444444444444444444444444444444444444444
    #4444444444444444444444444444444444444444444444444444444444444444444444444444444444
    #5555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    #55555555555555555555555555555555555555555555555555555555555555555555555555555555555
    #66666666666666666666666666666666666666666666666666666666666666666666666666666666666
    #66666666666666666666666666666666666666666666666666666666666666666666666666666666666
    #77777777777777777777777777777777777777777777777777777777777777777777777777777777777
    #777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888
    #8888888888888888888888888888888888888888888888888888888888888888888888888888888888
    #99999999999999999999999999999999999999999999999999999999999999999999999999999999999
    #99999999999999999999999999999999999999999999999999999999999999999999999999999999999
    #101010101010101010101010101010101010101010101010101010101010101010101010101010101010
    #101010101010101010101010101010101010101010101010101010101010101010101010101010101010
    #11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11
    #11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11
    #12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12
    #12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12
    #13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13
    #13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13
    #14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 
    #14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 
    #15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15
    #15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15











    # Adding dates here with regex ----------------------------------------------------
    pattern1 = re.compile("\d\d-\w\w\w-\d\d")  # 33-Mar-43
    pattern2 = re.compile("\d-\w\w\w-\d\d")  # 5-Jul-34
    pattern3 = re.compile("\d-\w\w\w\d")  # 6-Mar6
    pattern4 = re.compile("\d-\w\w\w-\d")  # 4-mar-3

    if pattern1.match(i) or pattern2.match(i) or pattern3.match(i) or pattern4.match(i):
        dateRepetitionTracker = dateRepetitionTracker + 1
        listOfListWithEachEntry[EntryRepetitionTracker].append(i)
    # End of adding date with regex-----------------------------------------------------

    jointMistakePattern1 = re.compile("/d/d/d/d/d/d/d/d/d/d")  # 3942270482
    if jointMistakePattern1.match(i):
        listOfListWithEachEntry[EntryRepetitionTracker].append(i)
        print('333333333333333333333333333333333333333333333333333333333333333333')
    else:

        # 2. number 4 digit ( 2324 ) --------------------------------------------------------
        numPattern1 = re.compile("\d\d\d\d")  # 1234
        # numPattern2 = re.compile("\d\d\d") # 123

        if numPattern1.match(i) and (len(i) == 3 or len(i) == 4):
            listOfListWithEachEntry[EntryRepetitionTracker].append(i)

        # End of number 4 digits adding ....................................................

        # 3. Adding number 6 digit (343423)
        sixPattern1 = re.compile("\d\d\d\d\d\d")  # 123445
        # sixPattern2 = re.compile("\d\d\d\d\d") # 12344

        if sixPattern1.match(i) and (len(i) == 5 or len(i) == 6):
            listOfListWithEachEntry[EntryRepetitionTracker].append(i)

    # End of number 6 digit (343423) -----------------------------------------------------
    # Resetting the repetition date data & incrementing field list
    if dateRepetitionTracker == 3:
        dateRepetitionTracker = 0
        EntryRepetitionTracker = EntryRepetitionTracker + 1

print('listoflistwitheachentry : ', listOfListWithEachEntry)
print('daterepetitiontracker', dateRepetitionTracker)
print('entryrepetitiontraker', EntryRepetitionTracker)
