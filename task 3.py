x= int(input("enter ur num1"))
y= int(input("enter ur num2"))
number=[]

def  perfect_square(number):
    square=[]
    for number in range(x,y):
        if number**2 <=y:
            square.append(number**2)
        else:
            break

    return square
print(perfect_square(number))





