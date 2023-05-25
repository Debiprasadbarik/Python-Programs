print("enter your data:")
roll_no=int(input("enter your roll.no:"))
redg_no=int(input("enter your redg number:"))
name=input("enter your name:")
branch=input("enter your branch name")
stream=input("enter your stream:")
sem=int(input("enter your sem:"))
phone_number=int(input("enter your phone_number:"))
address=input("enter your address")

#dictionary
thisdict={
    'roll_no':roll_no,
    'redg_no':redg_no,
    'name':name,
    'branch':branch,
    'stream':stream,
    'sem':sem,
    'phone_number':phone_number,
    'address':address
}
print("your cv is")
print(thisdict)