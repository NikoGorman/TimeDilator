#!/usr/bin/python
import math


def menu():
    # main menu area!
    print("All and grav_time are not yet finished")
    in_user = input("what do you want to calculate?:")
    if in_user == "time":
        length()
    if in_user == "length":
        real_length()
    if in_user == "done":
        done()
    if in_user == "mass":
        mass_change()
    if in_user == "all":
        calc_all()
    if in_user() == "Grav_time":
        Grav_time()


def length():
    # length here is talking about time dialation!
    print('how fast are you going? of the speed of light')
    in_speed = int(input())
    in_speeed = in_speed / 100
    print('how long will your trip take in years')
    in_dist = int(input())
    final_speed = in_speeed * in_speeed

    one = 1
    final_one = final_speed
    final_two = one - final_one
    final_three = math.sqrt(final_two)
    final_four = in_dist / final_three

    print("time dialation:")
    print(final_four)
    print(final_four - in_dist)
    fileObj = open("time.txt","w")

    fileObj.write("Time dilation: " + str(final_four))
    fileObj.close()

    menu()


def real_length():
    # this part is sketchy dont use yet!
    # this is the length contraction code!
    print("how fast are you going?:")
    in_speed = int(input())
    print('length of object')
    in_length = int(input())
    in_speeed = in_speed / 100
    final_speed = in_speeed * in_speeed
    one = 1
    final_one = final_speed
    final_two = one - final_one
    final_three = math.sqrt(final_two)
    final_four = in_length * final_three
   # final_five = in_dist / final_four
    print("length contraction:")
    print(final_four)
    fileObj = open("length.txt","w")
    fileObj.write("this is the length of the object at rest!")
    fileObj.write("Length Contraction: " + str(final_four))
    fileObj.close()
    menu()




def mass_change():
    #change in mass calculations
    print("how fast are you going?:")
    in_speed = int(input())
    print('mass of object in grams')
    in_dist = int(input())
    in_speeed = in_speed / 100
    final_speed = in_speeed * in_speeed
    one = 1
    final_one = final_speed
    final_two = one - final_one
    final_three = math.sqrt(final_two)
    final_four = in_dist / final_three
   # final_five = in_dist / final_four
    print("length contraction:")
    print(final_four)
    fileObj = open("mass.txt","w")

    fileObj.write("Mass: " + str(final_four))
    fileObj.close()
    menu()



def Grav_time():
    print("Unfinished. Will solve for time dilation of gravity")

def done():
    print("bye!")


def calc_all():
print ("Will calculate time, length, and mass changes")
menu()


menu()
# what will be added next???
# save data to a file @done
# read data that is saved in the appliocation@notdone
# save the data to cvs file?@notdone
#GUI?
#
#