#للارقام العشرية اما intللارقام الصحيحة
#x = float(input("what's x? "))
#y = float(input("what's y? "))
#للتقريب الاعداد بدل العشر
#z = round(x + y)
#للفواصل للارقام الكبيرة والتنظيم
#print(f"{z:,}")
#z = x / y
#print(f"{z:.3f}")
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()