listOfTasks = []
usrInput = ''
numOfTasks = 0
usrChoice = ''
changesDone = 0
tasksDone = []
numOfTasksDone = 0

while usrInput != 'q' and usrInput != 'Q':
    print("Enter " + str(numOfTasks + 1) + " task((M)odify, (D)one, (R)emove, show (L)ist, show list of done (T)asks or (Q)uit): ", end='')
    usrInput = input()
    if usrInput != 'q' and usrInput != 'Q' and usrInput != 'm' and usrInput != 'M' and usrInput != 'l' and usrInput != 'L' and usrInput != 'r' and usrInput != 'R' and usrInput != 'd' and usrInput != 'D' and usrInput != 't' and usrInput != 'T':
        numOfTasks += 1
        listOfTasks.append(usrInput)
    elif usrInput == 'l' or usrInput == 'L':
        if numOfTasks == 0:
            print("You didn't enter any task yet!")
        else:
            for index, item in enumerate(listOfTasks):
                print('Task ' + str(index + 1) + ' is: ' + item)
    elif usrInput == 'm' or usrInput == 'M':
        if numOfTasks == 0:
            print("You didn't enter any task yet!")
        else:
            print("Which task to modify?: ", end = '')
            selectedTaskIndex = input()
            print("Enter the new task's value: ", end='')
            taskNewValue = input()
            listOfTasks[int(selectedTaskIndex)-1] = taskNewValue
    elif usrInput == 'r' or usrInput == 'R':
        if numOfTasks == 0:
            print("You didn't enter any task yet!")
        else:
            print("Which task to remove?: ", end = '')
            selectedTaskIndex = input()
            del listOfTasks[int(selectedTaskIndex)-1]
            numOfTasks -= 1
    elif usrInput == 'd' or usrInput == 'D':
        if numOfTasks == 0:
            print("You didn't enter any task yet!")
        else:
            print("Which task is done already?: ", end = '')
            selectedTaskIndex = input()
            taskDone = listOfTasks[int(selectedTaskIndex)-1]
            tasksDone.append(taskDone)
            numOfTasksDone += 1
            del listOfTasks[int(selectedTaskIndex)-1]
            numOfTasks -= 1
    elif usrInput == 't' or usrInput == 'T':
        if numOfTasks == 0 and numOfTasksDone == 0:
            print("You didn't enter any task yet!")
        elif numOfTasksDone == 0:
            print("You didn't complete any task yet!")    
        else:
            for index, item in enumerate(tasksDone):
                print(str(index + 1) + ' Task done already is: ' + item)            