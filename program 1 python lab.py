name=input("enter your name:")
dob=input("enter your DOB:")
reg_no=input("enter your registration number:")
dept=input("enter your department:")
m1=float(input("enter marks for subject1 out of 100:"))
m2=float(input("enter marks for subject2 out of 100:"))
m3=float(input("enter marks for subject3 out of 100:"))
m4=float(input("enter marks for subject4 out of 100:"))
m5=float(input("enter marks for subject5 out of 100:"))

total=m1+m2+m3+m4+m5
percentage=total/5

print("\n-------Student details------")
print("name:",name)
print("DOB:",dob)
print("reg no:", reg_no)
print("department:",dept)
print("total marks:", total)
print("percentage:",percentage)
