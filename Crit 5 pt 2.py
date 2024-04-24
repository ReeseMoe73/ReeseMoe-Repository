#Ask use to enter number of books
number_books = int (input('Enter the number of books purchased this month'))

#If number is 0 or less print message to try again
if number_books < 0:
    note = 'Try again'

else:
    note = 'You are awarded'
#condition statements for books associated with award points
    if number_books >= 0 and number_books <= 1:
        note += '0'
    elif number_books >= 2 and number_books <= 3:
        note += '5'
    elif number_books >= 4 and number_books <=5:
        note += '15'
    elif number_books >= 6 and number_books <= 7:
        note += '30'
    elif number_books >= 8 and number_books >= 8:
        note += '60'

print (note)
