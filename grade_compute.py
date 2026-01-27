#letter = ['A', 'B','C','D',]
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
#print(letter_to_number(letter))

def remove_lowest_grade(gradestoremove):
    gradestoremove.remove(min(gradestoremove))
    return gradestoremove

def lowest_grade_to_remove(grades):
    return min(grades)

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
        return 'D-'
    elif grade == 0:
        return 'F'
    
