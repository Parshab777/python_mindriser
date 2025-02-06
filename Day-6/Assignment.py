# Exam mark evaluator
# ask user for the exam mark
# if mark is greater than 90 and smaller than 100 then print excellent
#  if mark is greater than 80 and smaller than 90 then print Very good
#  if mark is greater than 70 and smaller then 80 then print good
#  if mark is greater than 60 and smaller then 70 then print fair
# if mark is greater than 50 and samller than 60 then print could have been better
#  if mark is greater then 40 and smaller then 50 then print pass
#  if mark is less than 40 oprint fail


a = int(input("Enter the marks you obtain in exam"))
if a > 90 and a < 100:
    print("Excellent")
elif a > 80 and a < 90:
    print("Very good")
elif a > 70 and a < 80:
    print(" good")
elif a > 60 and a < 70:
    print("Fair")
elif a > 50 and a < 60:
    print("Could have been better")
elif a > 40 and a < 50:
    print("Pass")
else:
    print("fail")
