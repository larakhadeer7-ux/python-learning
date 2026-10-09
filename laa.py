Quiz=float(input("Enter grade quiz: "))
MTA=float(input("Enter grade MTA: "))
final=float(input("Enter grade final: "))
score=Quiz+MTA+final
print("score: ",score)
if score>=90:
    print("grade=A")
elif score>=70:
    print("grade=B")
elif score>=50:
    print("grade=c")
else:
    print("grade=f")
