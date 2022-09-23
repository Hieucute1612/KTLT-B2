import math;
x1=int(input("nhập x1--->"))
y1=iny(input("nhập y1---> "))

x2=int(input("nhập x2---> "))
y2=int(input("nhập y2---> "))

d1=(x2-x1)*(x2-x1);
d2=(y2 - y1)*(y2 - y1);
res=math.sqrt(d1+d2)
print ("distance between two points:",res);
