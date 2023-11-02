""" if condition"""
# age = int(input('Enter your Age : '))
# if age >= 18:
#     print('you can vote...!')
# else:
#     print("sorry you can't vote...!")

"""find the grade of a student"""

mark = int(input("enter the mark you obtained in exam : "))
if mark >= 90:
    print('you obtained A')
elif mark >= 80:
    print('you obtained B')
elif mark >= 70:
    print('you obtained C ')
elif mark >= 60:
    print("you obtained D")
elif mark < 60:
    print('sorry failed..!')
else:
    print('invalid input...!')
