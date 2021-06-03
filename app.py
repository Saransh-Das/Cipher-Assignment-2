#Ques 1
s="Hey i am from New Delhi";
print(len(s));
list=s.split();
print(list);
#Ques 2
S="name is rahul";
print(S.capitalize());
print(S.upper());
print(S.title().replace("N","R"));
#Ques 3
l=input("Enter Length : ");
b=input("Enter Bradth : ");
print("Area of the Rectangle is :",int(l)*int(b));
print("Perimeter of the Rectangle is : ", (2*(int(l)+int(b))));
#Ques 4
d=int(input("Enter an Integer Value : "));
pi=3.14;
print("Circumference of the circle is : ", (2*pi*d/2));
print("Area of the Circle is : ", (pi*d/2*d/2));
#Ques 5
import math
coffA=float(input("Enter the Coefficient a : "));
coffB=float(input("Enter the Coefficient b : "));
coffC=float(input("Enter the Coefficient c : "));
Diss = math.sqrt((coffB**2)-4*coffA*coffC);
alpha=(-coffB + Diss)/2*coffA;
beta=(-coffB - Diss)/2*coffA;
print("The Roots of the Quadratic equation with the above Coefficients are : ", "Alpha = ",alpha, "Beta = ",beta);

#Ques 6
radiusOfSphere=int(input("Enter radius as integer: "));
pi=3.14;
print("Volume of the Sphere with radius ", radiusOfSphere ,"is : ",(4/3*pi*radiusOfSphere**3));
#Ques 7
num=input("Enter the number please : ");
print("The number of digits in the entered number is : ",len(num));
#Ques 8
cap=input("Enter a String : ");
print(cap.upper());

#Ques 10
string="Saransh Is a Magician"
print(string[::-1]);

#Ques 9
q=input("Please Input the String : ");
n=int(input("Please Input the Index : "));
c=input("Please Input the Character : ");
temp=list(q);
temp[n]=c;
q=" ".join(temp);
print(q);