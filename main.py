name=input("Enter your name:")

print("Welcome",name,"to this adventure!")

answer=input("Your on a mud road,it has come to an end and you have can go left or right.Which way would you like to go?").lower()


if answer=="left":

    answer=input("you come to river,you can walk around it or swim accross? type walk to walk around & swim to swim accross:")


    if answer=="swim":

        print("you swam accross & wer eaten by an alligator.")


    elif answer=="walk":
        print("you have to walk safely")


    else:

        print("Not a valid option,you lose.")


print("Thank you for trying",name)