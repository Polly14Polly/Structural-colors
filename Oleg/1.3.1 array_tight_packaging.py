import math
def s(x):
    return math.sin(x)
def c(x):
    return math.cos(x)
size_x=1000
size_y=1000
r = 10
N_2k_x=size_x//(2*r)
N_2kp1_x=(size_x-r)//(2*r)
N_y=size_y/(r*math.sqrt(3)+2*r)

dx = r*1
dy = r*math.sqrt(3)
x0=r
y0=r
a=[]

for i in range(0, N_y):
    y=y0+dy*i
    arr=[]
    if i%2==0:
        t=N_2k_x
    else:
        t=N_2kp1_x
    for j in range(t):





