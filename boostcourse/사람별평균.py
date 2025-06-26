kor = [50,60,70,80,90]
math = [50,60,70,80,90]
eng = [50,60,70,80,90]
midterm_score = [kor, math, eng]

student_score = [0,0,0,0,0]
i=0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else:
    a,b,c,d,e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)