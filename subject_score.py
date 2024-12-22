#  Ask the user for a subject score. If it's above 90, congratulate him. If it's between 50 and 90, suggest improvement. Otherwise, advise on retaking the course.
subj_score=eval(input("Enter your subject score out of [100]: "))
if subj_score>90:
    print("Congratulations!")
elif subj_score>=50 and subj_score<=90:
    print("Improve a bit more")
else:
    print("Retake the course")