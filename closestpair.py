import math as m
from ast import literal_eval
def find_closest():
    inputs = input("Enter the ship locations : ").split()
    a = [literal_eval(i) for i in inputs]
    ax = sorted(a, key=lambda p: p[0])
    ay = sorted(a, key=lambda p: p[1])
    p1, p2, mi = closest_pair(ax, ay)
    print("The closest ship locations are : ",p1," and ",p2," distance between them is: ",mi)
def closest_pair(ax, ay):
    ln_ax = len(ax)  # It's quicker to assign variable
    if ln_ax <= 3:
        return brute(ax)  # A call to bruteforce comparison
    mid = ln_ax // 2  # Division without remainder, need int
    Lx = ax[:mid]  # Two-part split
    Rx = ax[mid:]
    midpoint = ax[mid][0]  
    Ly = list()
    Ry = list()
    for p in ay:  # split ay into 2 arrays using midpoint
        if p[0] <= midpoint:
           Ly.append(p)
        else:
           Ry.append(p)
    # Call recursively both arrays after split
    (p1, q1, mi1) = closest_pair(Lx, Ly)
    (p2, q2, mi2) = closest_pair(Rx, Ry)
    # Determine smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)
    # Call function to account for points on the boundary
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
    # Determine smallest distance for the array
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3    
def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    elif ln_ax == 3:
        p3 = ax[2]
        d1 = dist(p1,p3)
        d2 = dist(p2,p3)
        if d1<mi and d1<d2:
            return p1,p3,d1
        elif d2<mi and d2<d1:
            return p2,p3,d2
        return p1, p2, mi
def dist(p1, p2):
    return m.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array
    # Create a subarray of points not further than delta from
    # midpoint on x-sorted array
    s_y = [p for p in p_y if mx_x - delta <= p[0] <= mx_x + delta]
    best = delta  # assign best value to delta
    ln_y = len(s_y)  # store length of subarray for quickness
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best   
find_closest()