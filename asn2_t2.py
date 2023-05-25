thisdict={
    0:"maths",
    1:"english",
    2:"dbms",
    3:"python",
    4:"java"
}
num_stu=0
while num_stu!=10:
    num_sub=0; total_marks=0
    print("enter your five subject marks:")
    while num_sub!=5:
        total_marks+=int(input("enter your {} marks:".format(thisdict[num_sub])))
        num_sub+=1
    print("your total marks is:{}".format(total_marks))
    total_marks=0; 
    num_stu+=1