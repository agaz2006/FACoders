s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
name=input("Enter the name of student : ")
if name in s1 :
    print( name,"  ",sum(s1[1:]))
elif name in s2 :
    print( name,"  ",sum(s2[1:]))
elif name in s3 :
    print( name,"  ",sum(s3[1:]))
else :
    print ("Student is not recorded 0")
