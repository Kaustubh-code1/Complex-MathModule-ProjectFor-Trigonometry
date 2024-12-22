# Project so that Harina(or whatever that name was) doesn't have to have a headache. I do.
try:
    import math
    n=str(input("Enter a for area and b for perimeter or circumference: "))
    m=str(input("Enter a for triangle and b for circle: "))
    if n=="a" and m=="a":
        tr_b,tr_h=eval(input("Enter base and height separated by comma. "))
        tr_ar=0.5*tr_b*tr_h
        print("The area of given triangle is",tr_ar)
    elif n=="b" and m=="a":
        trs_1=int(input("Enter 1st side "))
        trs_2=int(input("Enter 2nd side "))
        trs_3=int(input("Enter 3rd side "))
        tr_pm=trs_1+trs_2+trs_3
        print("Perimeter of Given triangle is",tr_pm)
    elif n=="a" and m=="b":
        cr=int(input("Enter radius: "))
        c_ar=3.14*(cr**2)
        print("Area of given circle is",c_ar)
    elif n=="b" and m=="b":
        cr=int(input("Enter radius: "))
        c_circ=2*3.14*cr
        print("The circumference of given circle is",c_circ)
    else:
        raise ValueError
    
except ValueError:
    print("Wrong input")
except SyntaxError:
    print("Separate with comma")
except NameError:
    print("Wrong input")

