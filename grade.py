score=int(input("score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("grade: B")
elif 70 <= score < 80:
    print("grade: c")
elif 60 <= score < 70:
    print("grade: D")
else:
    print("grade: F")