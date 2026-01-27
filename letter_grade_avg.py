import grade_compute 

grades = input("Enter Letter Grades with $ in between: ").upper()
gradesParc = grades.split('$')

#Convert Grades to Float numbers
gradesToNumber = grade_compute.letter_to_number(gradesParc)

#Return the three hight grades as Floats
threeHighestGrades = grade_compute.remove_lowest_grade(gradesToNumber)
#Return the lowest float dropped
#gradeDropped = grade_compute.lowest_grade_to_remove(gradesToNumber)

#Return average grade plus curve bonus is needed
#calculatedAverage = grade_compute.avergae_grades(threeHighestGrades)

#Convert Number of grade dropped and averge to letter grade
#letterGradeDropped = grade_compute.number_to_grade(gradeDropped)
#letterAvergae = grade_compute.number_to_grade(calculatedAverage)

print(gradesParc)
print(gradesToNumber)
print(threeHighestGrades)
#print(gradeDropped)
