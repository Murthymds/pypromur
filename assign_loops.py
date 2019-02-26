"""
__author__ = 'Murthy'
"""

"""25. take a number from the user and check whether it is prime?"""
# Take input from the user
# Prime numbers are always greater than 1
# Prime numbers are only divisible by 1 and itself

"""print("Welcome")
n=int(input("Enter any number greater than 1:"))
if n>1:
    # check for factors
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            print(i,"times",n//i,"is",n)
            break
    else:
        print(n,"is a prime number")
             
     #if entered number is less then 1
else:
    print(n,"is not a prime number")
print("Thank you!!")    """

"""26. take a string from the user and check contains only digits or not?"""
"""# Take input from the user
print("Welcome")
s=input("Enter any string:")
#loop all the characters from the string
for i in s:
#check for any digit in the string
        if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            print("Entered string contains digits")
#break the loop once you found atleast one string
            break
else:
    print("Entered string doesn't contain any digits")
       
print("Thank you!!") """       
    
"""26. take a string from the user and check contains only digits or not?"""
"""# Take input from the user
print("Welcome")
s=input("Enter any string:")
#loop all the characters from the string
for i in s:
#check for any digit in the string
        if i in ["0","1","2","3","4","5","6","7","8","9"]:
            print("Entered string contains digits")
#break the loop once you found atleast one string
            break
else:
    print("Entered string doesn't contain any digits")
       
print("Thank you!!")"""

"""26. take a string from the user and check contains only digits or not?"""
"""# Take input from the user
print("Welcome")
s=input("Enter any string:")
#loop all the characters from the string
for i in s:
#check for any digit in the string
        if ord(i) in [48,49,50,51,52,53,54,55,56,57]:
            print("Entered string contains digits")
#break the loop once you found atleast one string
            break
else:
    print("Entered string doesn't contain any digits")
       
print("Thank you!!")"""

"""26. take a string from the user and check contains only digits or not?"""
"""# Take input from the user
print("Welcome")
s=input("Enter any string:")
#loop all the characters from the string
for i in s:
#check for any digit in the string
        if ord(i) in range(48,57):
            print("Entered string contains digits")
#break the loop once you found atleast one string
            break
else:
    print("Entered string doesn't contain any digits")
       
print("Thank you!!")"""

"""27. take a string from the user and check contains only  alphabets or not?"""
"""print("Welcome")
# Take input from the user
s=input("Enter any string:")
#loop all the characters from the string
for i in s:
    #check for any alphabet in the string
    if ord(i) in range(65,122):
        print("Entered string contains alphabet")
        break
else:
   print("Entered string does not contain alphabet")
print("Thank you!!")""" 

"""28. take a string from the user and check contains only  special chars or not?"""

"""print("Welcome")
# Take input from the user
s=input("Enter any string:")
#loop all the characters from the string
for i in s:
    #check for any special character in the string
    if not (ord(i) in range(65,122) or ord(i) in range(49,57)) :
        print("Entered string does contains special characters")
        break
   
else:
   print("Entered string does not contain special characters")
print("Thank you!!")"""

"""29.take a string from the user and check contains only  capital letters or not?"""
"""print("Welcome")
#Take input from the user
s=input("Enter any string:")
#loop all the characters from the string
for i in s:
    #check for any capital letter
    if ord(i) in range(65,90):
        print("Entered string contains capital letters")
        break
else:
    print("Entered string does not contain any capital letter")
print(Thank you!!)    """

"""30.take a string from the user and check contains only  small letters or not?"""

"""print("Welcome!")
s=input("Enter any string:")
for i in s:
    if ord(i) in range(97,122):
        print("Entered string contains small letters")
        break
else:
    print("Entered strings doesn't contain small letters")
print("Thank you!!")"""    

"""31. WAP to replace last n occurrence."""

"""33. Convert the total string in to lower case. Without using lower() function."""
"""print("Welcome")
#Take input from user
s=input("Enter any string:")
for i in s:
    if ord(i) in range(65,90):
        x=ord(i)
        y=x+32
        print(chr(y),end='')"""
    
"""34. Convert the total string in to upper case. Without using upper() function."""       
              
"""#Take user input
s=input("Enter any string:")
for i in s:
    x=ord(i)
    y=x-32
    print(chr(y),end='')"""

"""35. Show the below menu to the user until and until user select quit and display corresponding os message

'''
Menu:
1. windows
2. Linux
3. Mac
4. quit
'''"""
"""while True:
#Enter the menu
    print("Menu:\n1. Windows\n2. Linux\n3. Mac\n4. quit")
#Take user input
    s=input("Enter an option:")
    if s=="4":
        break

#print for diff options
    if s=="1":
        print("Windows selected")
    elif s=="2":
        print("Linux selected")
    elif s=="3":
        print("Mac selected")
    else:
        print("Wrong option selected")"""
"""32. WAP to check given string contains numbers or not. it should consider float numbers also."""
"""#Take the input from the user
s=input("Enter a string:")
asci_0=ord("0")
asci_9=ord("9")
for i in s:
    asc_i=ord(i)
    if asc_i>=asci_0 and asc_i<=asci_9:
        print("Entered string contains numbers")
        break
else:
    print("Entered string doesn't contain numbers")"""

"""33. Convert the total string in to lower case. Without using lower() function."""
"""#Take user input
s=input("Enter a string:")
asci_A=ord("A")
asci_Z=ord("Z")
res=''
for i in s:
    asc_i=ord(i)
    if asc_i>=asci_A and asc_i<=asci_Z:
        res=res+chr(asc_i+32)
    else:
        res=res+i
print(res) """       
        
"""33. Convert the total string in to upper case. Without using upper() function."""
"""#Take user input
s=input("Enter a string:")
asci_a=ord("a")
asci_z=ord("z")
res=''
for i in s:
    asc_i=ord(i)
    if asc_i>=asci_a and asc_i<=asci_z:
        res=res+chr(asc_i-32)
    else:
        res=res+i
print(res)"""

"""36. take a string from the user and check contains at least one digit or not?"""
"""#take user input
s=input("Enter any string:")
asci_0=ord("0")
asci_9=ord("9")
for i in s:
    asc_i=ord(i)
    if asc_i>=asci_0 and asc_i<=asci_9:
        print("Entered string contains atleast one string")
        break
else:
    print("Entered string doesn't contain any digit")"""

"""26. take a string from the user and check contains only digits or not?"""
"""#Take user input
s=input("Enter any string:")
asci_0=ord("0")
asci_9=ord("9")
for i in s:
    asc_i=ord(i)
    if asc_i not in range(asci_0,asci_9):
        print("Entered string contains atlest one non digit")
        break
else:
    print("Entered string contains only digits")"""
        
"""37. take a string from the user and check contains at least one alphabets or not?"""
"""#Take user input
s=input("Enter any string:")
asci_a=ord("a")
asci_z=ord("z")    
asci_A=ord("A")
asci_Z=ord("Z")
for i in s:
    asc_i=ord(i)
    if asc_i not in range(asci_a,asci_z) and asc_i not in range(asci_A,asci_Z):
        print("Entered string contains alteast one non alphabet")
        break
else:
    print("Entered stings contains alphabets only")"""

"""38. take a string from the user and check contains at least one chars or not?"""
"""#Take user input
s=input("Enter any string:")
asci_0=ord("0")
asci_9=ord("9")
for i in s:
    asc_i=ord(i)
    if asc_i not in range(asci_0,asci_9):
        print("Entered string contains atlest one non digit")
        break
else:
    print("Entered string contains only digits")"""
        
"""37. take a string from the user and check contains at least one alphabets or not?"""

"""#Take user input
s=input("Enter any string:")
asci_a=ord("a")
asci_z=ord("z")    
asci_A=ord("A")
asci_Z=ord("Z")
asci_0=ord("0")
asci_9=ord("9")
for i in s:
    asc_i=ord(i)
    if asc_i not in range(asci_a,asci_z) and asc_i not in range(asci_A,asci_Z) and asc_i not in range(asci_0,asci_9):
        print("Entered string contains alteast one char")
        break
else:
    print("Entered stings doesn't contain any char")"""
        
"""39. take a string from the user and check contains at least one capital letter or not?"""
"""#Take user input
s=input("Enter any string:")
asci_A=ord("A")
asci_Z=ord("Z")
for i in s:
    asc_i=ord(i)
    if asc_i in range(asci_A,asci_Z):
        print("Entered string contains atleast one capital letter")
        break
else:
    print("Entered string doesn't contain any capital letter")"""

"""40. take a string from the user and check contains at least one small letter or not?"""
"""#Take user input
s=input("Enter any string:")
asci_a=ord("a")
asci_z=ord("z")
for i in s:
    asc_i=ord(i)
    if asc_i in range(asci_a,asci_z):
        print("Entered string contains atleast one small letter")
        break
else:
    print("Entered string doesn't contain any small letter")"""

"""41. Print the first 100 odd numbers"""
n=0
for i in range(n,100)







    
    
    
    



