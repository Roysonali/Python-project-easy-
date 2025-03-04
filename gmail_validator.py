#conditions to check valid email
''' 
eg: a@a.in
It should be 
1. minm length of 6
2. 1st letter should be in alphabet
3. contain exactly one @
4. postion of "." should be 3rd or  4th from last
5. lower case
*  no space, no special character other than "@, _, ."

'''
#email validation using string function
email = input("Enter your email: ")
k,j,d=0,0,0
if len(email) >=6: #1
    if email[0].isalpha():#2
        if ("@" in email) and (email.count("@") ==1):#3
            if (email[-3]==".") ^ (email[-4]=="."):#4
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i=="@" or i=="_" or i==".":
                        continue
                    elif i.isdigit():
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("Right email")
            
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
      
    else:
        print("wrong email 2")

else:
    print("wrong email 1")
