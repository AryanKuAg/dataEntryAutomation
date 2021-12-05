import re

# opening the file
fs = open("extraction1.txt", "r")

allDataInOneList = []

for i in fs.readlines():
    for j in i.split(' '):
        allDataInOneList.append(j)

# allDataInOneList contains each work separately
# now its time to manipulate the data with regex
# print(allDataInOneList)

listOfListWithEachEntry = []
dateRepetitionTracker = 0
EntryRepetitionTracker = 0
name  = '' #to track name of a person
phoneConflictWithCodeTracker = 0 # Track that if code joints and make 10 digits number then it won't be conflict by phone numbers
splittedEmailTracker = '' # To Track Splitted Email

for index,i in enumerate(allDataInOneList):
    if len(allDataInOneList) -1 == index: # This protect me from list out of bound error
        continue
    

    #11111111111111111111111111111111111111111111111111111111111111111111111111111111

# Adding dates here with regex ----------------------------------------------------
    pattern1 = re.compile("\d\d-\w\w\w-\d\d")  # 33-Mar-43
    pattern2 = re.compile("\d-\w\w\w-\d\d")  # 5-Jul-34
    pattern3 = re.compile("\d-\w\w\w\d")  # 6-Mar6
    pattern4 = re.compile("\d-\w\w\w-\d")  # 4-mar-3

    previousElement = allDataInOneList[index -1]
    nextElement = allDataInOneList[index +1]

    # Right Code : it will add a new list or entry
    if (dateRepetitionTracker == 0) :
        
        listOfListWithEachEntry.append([])
        


    if pattern1.match(i) or pattern2.match(i) or pattern3.match(i) or pattern4.match(i):
        dateRepetitionTracker = dateRepetitionTracker + 1 #tracker
        listOfListWithEachEntry[EntryRepetitionTracker].append(i) #adding to list
        continue
    # End of adding date with regex-----------------------------------------------------

    #111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    #2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3


    jointMistakePattern1 = re.compile("\d\d\d\d\d\d\d\d\d\d")  # 3942270482
    if jointMistakePattern1.match(i):
        if phoneConflictWithCodeTracker == 0 :

            listOfListWithEachEntry[EntryRepetitionTracker].append(i[0:4])
            listOfListWithEachEntry[EntryRepetitionTracker].append(i[4:-1])
        else:
            listOfListWithEachEntry[EntryRepetitionTracker].append(i)

        phoneConflictWithCodeTracker = phoneConflictWithCodeTracker + 1
        if phoneConflictWithCodeTracker == 3:
            phoneConflictWithCodeTracker = 0

        continue

    else:

        # 2. number 4 digit ( 2324 ) --------------------------------------------------------
        numPattern1 = re.compile("\d\d\d\d")  # 1234
        # numPattern2 = re.compile("\d\d\d") # 123

        if numPattern1.match(i) and (len(i) == 3 or len(i) == 4):
            listOfListWithEachEntry[EntryRepetitionTracker].append(i)
            phoneConflictWithCodeTracker = phoneConflictWithCodeTracker + 0.5
            continue

        # End of number 4 digits adding ....................................................

        # 3. Adding number 6 digit (343423)
        sixPattern1 = re.compile("\d\d\d\d\d\d")  # 123445
        # sixPattern2 = re.compile("\d\d\d\d\d") # 12344

        if sixPattern1.match(i) and (len(i) == 5 or len(i) == 6):
            listOfListWithEachEntry[EntryRepetitionTracker].append(i)
            phoneConflictWithCodeTracker = phoneConflictWithCodeTracker + 0.5
            continue

    # End of number 6 digit (343423) -----------------------------------------------------

    #2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3 2 3

    #4444444444444444444444444444444444444444444444444444444444444444444444444444444444

    namePattern = re.compile("[a-zA-Z]")  # anyname
    
    if namePattern.match(i) and sixPattern1.match(previousElement):
        name =  i
        
    
    elif (namePattern.match(i)) and (pattern1.match(nextElement) or pattern2.match(nextElement) or pattern3.match(nextElement) or pattern4.match(nextElement)):
        name = name + ' ' + i 
        listOfListWithEachEntry[EntryRepetitionTracker].append(name)
        
        name = ''
       
        continue
    else:
        
        name = name + ' ' + i 

    #4444444444444444444444444444444444444444444444444444444444444444444444444444444444
    #5555555555555555555555555555555555555555555555555555555555555555555555555555555555555

    #SO ITS A DATE THAT WILL FILLED UP BY SECTION 1 

    #55555555555555555555555555555555555555555555555555555555555555555555555555555555555
    #66666666666666666666666666666666666666666666666666666666666666666666666666666666666

    if ("OPEN" in i) or ("open" in i):
        listOfListWithEachEntry[EntryRepetitionTracker].append("OPEN")
        continue
    elif ("CLOSED" in i) or ("closed" in i):       
        listOfListWithEachEntry[EntryRepetitionTracker].append("CLOSED")
        continue

    #66666666666666666666666666666666666666666666666666666666666666666666666666666666666
    #77777777777777777777777777777777777777777777777777777777777777777777777777777777777

    if (previousElement == "OPEN") or (previousElement == "CLOSED") or not (splittedEmailTracker == ''):
        if not (splittedEmailTracker == '') and '@' in i:
            splittedEmailTracker = splittedEmailTracker + i
            listOfListWithEachEntry[EntryRepetitionTracker].append(i)
            splittedEmailTracker = ''
            continue
        elif namePattern.match(i) and '@' in nextElement:
            splittedEmailTracker = i
            continue    
        elif namePattern.match(i) and '@' in i:
            listOfListWithEachEntry[EntryRepetitionTracker].append(i)
            continue
        
    #777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    #888888888888888888888888888888888888888888888888888888888888888888888888888888888

    # phoneNumberPattern = re.compile("\d\d\d\d\d\d\d\d\d\d")  # 3942270482
    # THIS IS COVERED BY 2 3 2 3 2 3 2 3 2 3

    #8888888888888888888888888888888888888888888888888888888888888888888888888888888888
    #99999999999999999999999999999999999999999999999999999999999999999999999999999999999

    # DATE IS COVERED BY ABOVE CODE

    #99999999999999999999999999999999999999999999999999999999999999999999999999999999999
    #101010101010101010101010101010101010101010101010101010101010101010101010101010101010

    # THIS IS COVERED BY 2 3 2 3 2 3 2 3 2 3

    #101010101010101010101010101010101010101010101010101010101010101010101010101010101010
    #11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11

    capitalCodePattern = re.compile("[A-Z]") # ABX, NO

    if capitalCodePattern.match(i):
        listOfListWithEachEntry[EntryRepetitionTracker].append(i)



    #11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11
    #12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12
    #12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12
    #13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13
    #13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13
    #14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 
    #14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 14 
    #15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15
    #15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15











    

    # Resetting the repetition date data & incrementing field list
    if dateRepetitionTracker == 3 and pattern1.match(nextElement) or pattern2.match(nextElement) or pattern3.match(nextElement) or pattern4.match(nextElement):
        dateRepetitionTracker = 0
        EntryRepetitionTracker = EntryRepetitionTracker + 1
        

print('listoflistwitheachentry : ', listOfListWithEachEntry)
print('daterepetitiontracker', dateRepetitionTracker)
print('entryrepetitiontraker', EntryRepetitionTracker)
