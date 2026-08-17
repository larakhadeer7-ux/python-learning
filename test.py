#ask user for  their name
#name = input("what's your name? ")
#تنظيف المسافات وتكبير الحروف
#name = name.strip().title()
#say hello to user
#print(f"hello, {name}")
#first, last = name.split(" ")
#print(f"hello, {first}")
def hello(to="world"):
    print(f"hello, {to}")

name = input("what's your name? ")
hello(name)
# 1. بنعرف الدالة الرئيسية
def main():
    name = input("What's your name? ")
    hello(name)

# 2. بنعرف دالة الترحيب
def hello(to="world"):
    print("hello,", to)

# 3. بننادي الدالة الرئيسية في آآآآخر سطر خالص بعد ما بايثون حفظ كل شيء
main()