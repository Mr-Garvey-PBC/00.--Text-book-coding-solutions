# This is a very long way of doing this program as we havent covered ideas such as functions which would make this a lot easier

subject_a=int(input('How many students take subject_a: '))
subject_b=int(input('How many students take subject_b: '))
subject_a_grades=[]
subject_b_grades=[]

user_choice=str(input('Which subject do you want to deal with (a) or (b): '))

if user_choice=='a':
    student_count=1
    student_grade=int(input(f'Please enter the grade for student {student_count} in subject A: '))
    
    while (student_grade!=0) and (student_count<subject_a):
        student_count+=1
        subject_a_grades.append(student_grade)
        student_grade=int(input(f'Please enter the grade for student {student_count} in subject A: '))
          
    print(f'\nThe max value scored in subject a is {max(subject_a_grades)} and the min was {min(subject_a_grades)}.')
    
 
 
elif user_choice=='b':
    student_count=1
    student_grade=int(input(f'Please enter the grade for student {student_count} in subject B: '))
    
    while (student_grade!=0) and (student_count<subject_b):
        student_count+=1
        subject_b_grades.append(student_grade)
        student_grade=int(input(f'Please enter the grade for student {student_count} in subject B: '))
          
    print(f'\nThe max value scored in subject a is {max(subject_b_grades)} and the min was {min(subject_b_grades)}.')
    