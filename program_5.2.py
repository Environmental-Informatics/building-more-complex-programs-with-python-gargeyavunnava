"""
Created on Fri Jan 31 10:23:13 2020
Purdue account name: vvunnava
Github account name: gargeyavunnava
Exercise 5.2, Part 2, thinkpython 2e

Problem description: function 'user_input' to check if the user given numbers
violate the fermat theorem. fermat theorem is defined in check_fermat function.

Program is valid only for numbers, no strings.
"""


"""
check_fermat function takes in 4 numbers (could be float but converted into int later)
if the theorem is violated, ir prints "Holy smokes, Fermat was wrong!".
if theorem is not violated, it prints "No, that doesn't work."
"""
def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

"""
user_input function helps in taking the 4 user input numbers typed on keyboard
and assigns them to the 4 number variables as an input to check_fermat function
"""
def user_input(a = int(float(input("Enter 'a' value: \n"))), b = int(float(input("Enter 'b' value: \n"))),
               c = int(float(input("Enter 'c' value: \n"))), n = int(float(input("Enter 'n' value: \n")))):
    
    print("\n")
    print("Entered value for 'b' in integer form  is ",a)  #printing what user inputs
    print("Entered value for 'b' in integer form  is ",b)
    print("Entered value for 'c' in integer form  is ",c)
    print("Entered value for 'n' in integer form  is ",n)
    print("\n")
    print("Checking for Fermat's theorem violation...\n")
    check_fermat(a,b,c,n)
    
user_input()
