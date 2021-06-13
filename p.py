print('enter your name, then press enter')
name = input()
if name == 'Preethi':
    print('Hi Dr.Preethi!')
else:
    print('hi! {}'. format(name))
print('enter your age,  then press enter')
age = input()
int_age = int(age)
if int_age < 18:
    print('{} not eligible to vote '.format(name))
else:
    print('{} is eligible to vote'.format(name))
