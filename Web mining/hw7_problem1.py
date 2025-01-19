import random
def mean(x):
    return sum(x)/len(x)
def median(x):
    if len(x)%2==0:
        return (x[(len(x)//2)-1]+x[(len(x)//2)+1])/2
    else:
        return x[len(x)//2]
def mode(x):
    a,k={},[]
    for i in x:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    for i,j in a.items():
        if j==max(a.values()):
            k.append(i)
    return k[0]
def variance(x):
    a=mean(x)
    b=0
    for i in x:
        b+=(i-a)**2
    return (b/(len(x)-1))
def std(x):
    return variance(x)**(1/2)
def summary(n):
    global x
    x=[]
    f = open("numbers.txt", "w")
    for i in range(0, n):
        x.append(random.randint(0, 100))
    x.sort()
    f.write("x=" + str(x) + "\n")
    f.write("mean of the numbers list is " + str(mean(x)) + "\n")
    f.write("median of the numbers list is " + str(median(x)) + "\n")
    f.write("mode of the numbers list is " + str(mode(x)) + "\n")
    f.write("variance of the numbers list is " + str(variance(x)) + "\n")
    f.write("standard deviation of the numbers list is " + str(std(x)) + "\n")
n=50
summary(n)
