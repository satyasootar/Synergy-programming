#WAP to calculate the sum of total marks obtained by a student of five different subjects & find their average marks. 

marks = []


subjects = 5

for i in range(subjects):

    mark = int(input(f"Enter your marks for subject {i+1}: "))
    marks.append(mark)

total_sum = sum(marks)

average = total_sum / subjects


print(f"The total marks is {total_sum}")
print(f"The average marks is {average:.2f}") 
