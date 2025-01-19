from math import sqrt
def pp():
    f = open('points.txt', 'r')
    qp=[]
    for i in f:
        q=i.split(",")
        for i in range(1,len(q)-1):
            q[i]=float(q[i])
        q[3]=q[3].rstrip("\n")
        q[3]=float(q[3])
        qp.append(q)
    return qp

def euclidean_distance(points):
    fi = []
    s = 0
    for j in range(len(points)):
        for k in range(j + 1, len(points)):
            for i in range(1, len(points[k])):
                if points[j][i] != 0 and points[k][i] != 0:
                    a = (points[j][i] - points[k][i]) ** 2
                    s += a
                elif points[j][i] == 0.0 and points[k][i] != 0.0:
                    a = (points[k][i]) ** 2
                    s += a
                elif points[j][i] != 0.0 and points[k][i] == 0.0:
                    a = (points[j][i]) ** 2
                    s += a
                s = sqrt(s)
            fi.append(s)
    return fi

def closest_to_origin(points):
    orgi,q=[],0
    for j in range(0, len(points)):
        for i in range(1, len(points[j])):
            sqr_org = (points[j][i]) ** 2
            q += sqr_org
        sqrt_org = sqrt(q)
        orgi.append(sqrt_org)
    return orgi

oye=[]
points=pp()
#print(points)
fi,orgi=euclidean_distance(points),closest_to_origin(points)
final_min=min(fi)
for i in range(len(points)):
    for j in range(i+1,len(points)):
        ol=str(i+1)+str(j+1)
        oye.append(ol)
org_min=min(orgi)
for i in range(len(orgi)):
    if org_min in orgi:
        print("Distance from origin to point{} is the shortest = ".format(i+1), org_min)
        break
for o in range(len(fi)):
    if fi[o] == final_min:
        i=int(oye[o][0])
        j=int(oye[o][1])
        print("distance from point{}= ".format(i),points[i-1][1:] ,"to distance from point{}".format(j),points[j-1][1:],"is the shortest distance = ",
              final_min)
        break