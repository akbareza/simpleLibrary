import os
import math as mt
import time
import datetime

def clear_screen():
    if os.name == "nt":    #"posix" is for MacOS, Linux, etc
        os.system("cls")   # for Windows
    else:
        os.system("clear") # for Linux and Mac OS

def inputNumber(text,output='outInt'): #output -> Format output
    while True:
        try:
            inputVar = input(f'{text} : ')
            cekFloat = float(inputVar)
            if cekFloat.is_integer():
                #print('Input is an integer')
                break
            else:
                #print('Input is a float')
                break
        except ValueError:
            print('Please input a valid number!')
            
    if output == 'outInt':
        return int(cekFloat)
    else:
        return inputVar

def chooseYesNo (text):
    while True:
        inputVar = input(f'{text} : ')
        if inputVar.upper() in ('Y', 'N'):
            break
        else:
            print('Please input Y / N!')
            continue
    return inputVar.upper()

def printSeparator(type='-'):
    separator = type * 180 #+ "\n"
    print(separator)

def printMenu(): #dibutuhkan validasi kembali untuk menu
    menu = '''
    MENU

    [1] Show Data
    [2] Add Data
    [3] Update Data
    [4] Delete Data
    [5] Exit

    '''
    while True:
        printSeparator('=')
        print(menu)
        inputMenu = inputNumber('Input Menu','outInt')
        if inputMenu in [1,2,3,4,5]:
            break
        else:
            print('Number is invalid!')
            time.sleep(1)
            clear_screen()
            continue
            
    return inputMenu

def printHeader():
    print('Index\t|Book ID\t|\t\t\tBook Name\t\t\t|\tBook Author\t|\tYear\t|\tPublisher\t|\tISBN\t|\tCategory')
    printSeparator('=')

def printBooks():
    for i in range(len(dataBase)):

        bookID = dataBase[i][0] + '\t'

        if len(dataBase[i][3]) >= 45:
            bookName = dataBase[i][3] + '\t'
        elif len(dataBase[i][3]) >= 30:
            bookName = dataBase[i][3] + '\t\t\t'
        elif len(dataBase[i][3]) >= 15:
            bookName = dataBase[i][3] + '\t\t\t\t\t'
        elif len(dataBase[i][3]) >= 8:
            bookName = dataBase[i][3] + '\t\t\t\t\t\t'
        else:
            bookName = dataBase[i][3] + '\t\t\t\t\t\t\t'

        if len(dataBase[i][1]) >= 15:
            bookAuthor = dataBase[i][1] + '\t'
        elif len(dataBase[i][1]) >= 7:
            bookAuthor = dataBase[i][1] + '\t\t'
        else:
            bookAuthor = dataBase[i][1] + '\t\t\t'

        bookYear = '\t' + dataBase[i][2] + '\t'

        if len(dataBase[i][5]) >= 15:
            bookPublisher = dataBase[i][5] + '\t'
        else:
            bookPublisher = dataBase[i][5] + '\t\t'

        isbn = dataBase[i][6] + '\t'

        bookCategory = '\t' + dataBase[i][7] + '\t'

        print(f'{i}\t|{bookID}|{bookName}|{bookAuthor}|{bookYear}|{bookPublisher}|{isbn}|{bookCategory}')
        printSeparator('-')

def printPaket():
    clear_screen()
    printHeader()
    printBooks()

def sortItem(index,reverseVal):
    dataBase.sort(key=lambda x: x[index], reverse=reverseVal)

def filterItem(database, type,coloumn,textFilter):
    filteredList = []
    finalList = []
    if type == 1:
        filteredList = set() # use a set to avoid the duplicate
        for item in dataBase:
            for element in item:
                if str(textFilter).upper() in str(element).upper():
                    filteredList.add(tuple(item))  #set cannot be added by list type, so we choose to use tuple instead

        finalList = []
        for item in filteredList:
            finalList.append(list(item))

        #dataBase = finalList.copy

        #print(finalList)
    elif type == 2:
        for item in dataBase:
            if str(textFilter).upper() in str(item[coloumn]).upper(): # check if the year is 2019 (the third item in the sublist)
                finalList.append(item) # add the item to the filtered list if it matches the condition

        #dataBase = finalList.copy
        #print(filteredList)
    return finalList

def addBook(curSCBook, curSOBook, curOTBook):
    clear_screen()
    printSeparator('=')
    print(f'\n\t[2] Add Data | Date Now = {formattedDate}\n')
    printSeparator('=')
    print('\n')
    bookAuthor = input('Please input author\t\t : ')
    while True:
        year = inputNumber('Please input released year\t')
        if year >= 0:
            year = str(year)
            break
        else:
            print('Please input the right year format!')
    #year = input('Please input released year\t : ')
    bookTitle = input('please input book title\t\t : ')
    city = input('Please input published city\t : ')
    publisher = input('Please input publisher\t\t : ')
    while True:
        ISBN = input('Please input ISBN\t\t : ')
        try:
            ISBNCheck = int(ISBN)
            if len(ISBN) == 13:
                break
            else:
                print('Please enter 13 digits of ISBN!')
                continue
        except:
            print('Please enter with numerical format!')
            continue
    bookCategory = inputNumber('Please choose book category!\n[1] Science\n[2] Social\n[3] Others\nInput','outInt')
    while True:
        if bookCategory == 1:
            bookCategory = 'Science'
            formattedNumber = '{:04d}'.format(curSCBook)
            stringNumber = str(formattedNumber)
            bookID = 'SC' + str(formattedDate) + stringNumber
            global SCBook
            SCBook +=1
            break
        elif bookCategory == 2:
            bookCategory = 'Social'
            formattedNumber = '{:04d}'.format(curSOBook)
            stringNumber = str(formattedNumber)
            bookID = 'SO' + str(formattedDate) + stringNumber
            global SOBook
            SOBook +=1
            break
        elif bookCategory == 3:
            bookCategory = 'Others'
            formattedNumber = '{:04d}'.format(curOTBook)
            stringNumber = str(formattedNumber)
            bookID = 'OT' + str(formattedDate) + stringNumber
            global OTBook
            OTBook +=1
            break
        else:
            print('Category is not found!')

    while True:
        clear_screen()
        print(f'SUMMARY\n\nBook ID\t\t: {bookID}\nAuthor\t\t: {bookAuthor}\nYear\t\t: {year}\nTitle\t\t: {bookTitle}\nCity\t\t: {city}\nPublisher\t: {publisher}\nISBN\t\t: {ISBN}\nCategory\t: {bookCategory}\n\n')
        submitBook = chooseYesNo('Are you sure want to add this book? [Y]/[N]')
        if submitBook == 'Y':
            dataBase.append([bookID, bookAuthor, year, bookTitle,city,publisher,ISBN,bookCategory])
            print('Data Successfully Added!')
            time.sleep(1)
            break
        else:
            break

def dateCheck(formattedDate):
    nowNew = datetime.datetime.now()
    formattedDateNew = nowNew.strftime("%Y%m%d")
    if formattedDateNew != formattedDate:
        formattedDate = formattedDateNew
        global SCBook, SOBook, OTBook
        SCBook = SOBook = OTBook = 1
    else:
        pass
    return formattedDate    
        
def deleteBook(dataBase):
    jumlahBuku = len(dataBase)
    print(f'jumlah Buku = {jumlahBuku}')
    
    while True:
        try:
            printPaket()
            tempBook = []
            delBook = int(input('Masukkan nomor index buku yang ingin dihapus: '))
            if delBook in range(0,jumlahBuku):
                tempBook.append(dataBase[delBook])
                while True:
                    print(f'{tempBook[0][0]} - {tempBook[0][1]} - {tempBook[0][3]}')
                    submitBook = chooseYesNo('Are you sure want to delete this book? [Y]/[N]')
                    if submitBook == 'Y':
                        print('Data Successfully Deleted!')
                        time.sleep(2)
                        break
                    else:
                        break
                del dataBase[delBook]
                break
            else:
                print('Index tidak ditemukan')
        except:
            print('Masukkan angka!')

def updateBook(dataBase):
    jumlahBuku = len(dataBase)
    print(f'jumlah Buku = {jumlahBuku}')
    
    printPaket()
    while True:
        try:
            
            tempBook = []
            updateBook = int(input('Masukkan nomor index buku yang ingin diubah: '))
            if updateBook in range(0,jumlahBuku):
                tempBook.append(dataBase[updateBook])
                while True:
                    clear_screen()
                    print('Book Detail')
                    print(f'[1] Book ID\t\t: {tempBook[0][0]}')
                    print(f'[2] Author\t\t: {tempBook[0][1]}')
                    print(f'[3] Year\t\t: {tempBook[0][2]}')
                    print(f'[4] Title\t\t: {tempBook[0][3]}')
                    print(f'[5] City\t\t: {tempBook[0][4]}')
                    print(f'[6] Publisher\t\t: {tempBook[0][5]}')
                    print(f'[7] ISBN\t\t: {tempBook[0][6]}')
                    print(f'[8] Category\t\t: {tempBook[0][7]}')
                    #print(dataBase[updateBook])
                    updateField = inputNumber('Masukkan nomor kolom yang ingin diubah:','outInt')
                    if updateField in range(1,9):
                        if updateField == 1:
                            print('Book ID cannot be changed!')
                            time.sleep(1)
                            continue
                        else:
                            updateValue = updateFieldFunc(updateField)
                        
                        print(f'\n!!! {tempBook[0][updateField-1]} -> {updateValue} !!!')
                        submitBook = chooseYesNo('Are you sure want to update this field? [Y]/[N]')
                        if submitBook == 'Y':
                            tempBook[0][updateField-1] = updateValue
                            dataBase[updateBook][updateField-1] = updateValue
                            print('Data Successfully updated!')
                            time.sleep(2)
                            break
                        else:
                            break
                    else:
                         print('Index field tidak ditemukan')
                         time.sleep(1)
                         continue
                break
            else:
                print('Index book tidak ditemukan')
                time.sleep(1)
                continue
        except:
            print('Masukkan angka!')
            time.sleep(1) 

def updateFieldFunc(field):
    if field == 2:
        output = input('Please enter new Author: ')
        return output
    elif field == 3:
        while True:
            output = inputNumber('Please input new year\t')
            if output >= 0 :
                output = str(output)
                break
            else:
                print('Please input the right year format!')
        # output = input('Please enter new Year: ')
        return output
    elif field == 4:
        output = input('Please enter new Title: ')
        return output
    elif field == 5:
        output = input('Please enter new City: ')
        return output
    elif field == 6:
        output = input('Please enter new Publisher: ')
        return output
    elif field == 7:
        while True:
            output = input('Please input ISBN\t\t : ')
            try:
                ISBNCheck = int(output)
                if len(output) == 13:
                    break
                else:
                    print('Please enter 13 digits of ISBN!')
                    continue
            except:
                print('Please enter with numerical format!')
                continue
        # output = input('Please enter new ISBN: ')
        return output
    else:
        while True:
            output = input('Please enter new Category: ')
            if output.capitalize() in category:
                break
            else:
                print('Category is not found. The available categories are: ' + ', '.join(category))
        return output.capitalize()

### MAIN PROGRAM ###

category = ['Social', 'Science', 'Others']
dataBase = [['SC202304090001','Stephen Hawking','2019', 'Brief Answers to the Big Questions', 'London', 'John Murray Press', '9781473695986', 'Science'],
            ['SO202304090001','Sigmund Freud','1995', 'The Freud Reader', 'New York', 'W. W. Norton & Company', '9780393314038', 'Social'],
            ['OT202304100001','Mark Blake','2008', 'Comfortably Numb: The Inside Story of Pink Floyd', 'New York', 'Hachette Books', '9780786727087', 'Others'],
            ['OT202304100002','Emha A. Najib','2018', 'Daur I', 'Sleman', 'Penerbit Bentang', '9786022913979', 'Others'],
            ['SO202305020001','Jason Barron','2019', 'The Visual MBA', 'London', 'Penguin Business', '9780241386682', 'Social']]
SCBook = 1
SOBook = 1
OTBook = 1
formattedDate = '19700101'

clear_screen()
while True:
    clear_screen()
    now = datetime.datetime.now()
    formattedDate = dateCheck(formattedDate)

    inputMenu = printMenu()
    if inputMenu == 1: #SHOW
        dataBaseBU = dataBase.copy()
        while True:
            printPaket()
            while True:
                printPaket()
                subMenuShow = inputNumber('All data is displayed!\n[1] Filter\n[2] Sort\n[3] Remove filter and sort\n[4] Back\nInput','outInt')
                print(subMenuShow)
                if subMenuShow == 1:
                    #print('THIS IS FILTER')
                    #print(dataBase)
                    while True:
                        printPaket()
                        subMenuFilter = inputNumber('Select filter type!\n[1] All Field\n[2] Selected Field\n[3] Back\nInput','outInt')
                        if subMenuFilter == 1:
                            textFilter = input('Please input text:')
                            dataBase = filterItem(dataBase, subMenuFilter,0,textFilter)
                            printPaket()
                            break

                        elif subMenuFilter == 2:
                            while True:
                                printPaket()
                                kolomFilter = inputNumber('Select filter coloumn!\n[1] Book Author\n[2] Year\n[3] Book Name\nInput','outInt')
                                if kolomFilter in range(1,4):
                                    textFilter = input('Please input text:')
                                    dataBase = filterItem(dataBase, subMenuFilter,kolomFilter,textFilter)
                                    printPaket()
                                    break
                                else:
                                    continue

                        elif subMenuFilter == 3:
                            break

                        else:
                            print('Input is not found')
                            time.sleep(1)
                elif subMenuShow == 2:
                    #print('THIS IS SORT')
                    while True:
                        printPaket()
                        subMenuSort = inputNumber('Select sort parameter!\n[1] Book Author\n[2] Year\n[3] Book Name\n[4] Back\nInput','outInt')
                        if subMenuSort in range(1,4):
                            while True:
                                printPaket()
                                sortCond = inputNumber('Select sort type!\n[1] Ascending\n[2] Descending\n\nInput','outInt')
                                if sortCond in range(1,3):
                                    if sortCond == 1:
                                        sortCond = False
                                        break
                                    elif sortCond == 2:
                                        sortCond = True
                                        break
                                    else:
                                        print('Input is not found!')

                            sortItem(subMenuSort,sortCond)
                            printPaket()
                            continue
                        elif subMenuSort == 4:
                            break
                        else:
                            print('Parameter is not found! Please enter the correct input!')
                            time.sleep(1)
                            continue
                    break
                elif subMenuShow == 3:
                    dataBase = dataBaseBU.copy()
                    continue
                elif subMenuShow == 4:
                    break
                else:
                    print('Sub Menu is not found! Please enter the correct input!')
                    time.sleep(1)
            if subMenuShow == 4:
                dataBase = dataBaseBU.copy()
                break
            else:
                continue
    elif inputMenu == 2: #ADD
        addBook(SCBook,SOBook,OTBook)
    elif inputMenu == 3: #UPDATE
        updateBook(dataBase)
    elif inputMenu == 4: #DELETE
        deleteBook(dataBase)
    else:
        clear_screen()
        printSeparator('=')
        print('\nTHANK YOU FOR VISITING')
        print('Akbareza Muhammad | 2023\n')
        printSeparator('=')
        break