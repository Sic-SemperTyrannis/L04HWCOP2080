
def letter_to_number(grades):
    number_list = []
    for grade in grades:    
        if grade == 'A':
            number_list.append(4)
        elif grade == 'A-':
            number_list.append(3.7)
        elif grade == 'B+':
            number_list.append(3.3)
        elif grade == 'B':
            number_list.append(3)
        elif grade == 'B-':
            number_list.append(2.7)
        elif grade == 'C+':
            number_list.append(2.3)
        elif grade == 'C':
            number_list.append(2)
        elif grade == 'C-':
            number_list.append(1.7)
        elif grade == 'D+':
            number_list.append(1.3)
        elif grade == 'D':
            number_list.append(1)
        elif grade == 'F':
            number_list.append(0)       
    return number_list


def remove_lowest_grade(gradestoremove):
    gradestoremove.remove(min(gradestoremove))
    return gradestoremove

def check_user_input(userInput):
    #Check if user entered a Q to quit
    for letter in userInput:
        if letter == 'Q':
            exit(0)
            return
    
    allowed_symbols = set("+,-")
    for char in userInput:
        if not (char.isalpha() or char in allowed_symbols):
            print("Invalid Entry")
            exit(0)


def lowest_grade_to_remove(grades):
    lowestGrade = min(grades)
    return lowestGrade

def avergae_grades(grades):
    averageGrades = sum(grades) / len(grades)
    for num in grades:
        if num > 2.7: 
            return averageGrades # Found a non-B- grade     
    return averageGrades + .25 # All grades were less then B-

def number_to_grade(grade):
    if grade > 3.7:
        return 'A'
    elif grade > 3.3 :
        return 'A-'
    elif grade > 3 :
        return 'B+'
    elif grade > 2.7:
        return 'B'
    elif grade > 2.3:
        return 'B-'
    elif grade > 2:
        return 'C+'
    elif grade > 1.7:
        return 'C'
    elif grade > 1.3:
        return 'C-'
    elif grade > 1:
        return 'D+'
    elif grade > 0:
        return 'D'
    elif grade == 0:
        return 'F'
    
