

def hailstone(num):
    seq = []
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        seq.append(num)
    return seq
def hailstone(num):
    seq = [num]
    while num - 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        seq.append(num)
    return seq
def hailstonerecursive(num):
    if num == 1:
        return []
    if num % 2 == 0:
        num /= 2
    else:
        num = 3 * num + 1
    return [num].__add__(hailstonerecursive(num))
def hailstonerecursive(num):
    if num == 1:return []
    num = 3 * num + 1 if num % 2 else num / 2
    return [num].__add__(hailstonerecursive(num))

def hailstone(a):
 if a==1:return[]
 a=3*a+1if a%2else a/2;return[a]+(hailstone(a))
# def hailstone(a):
#     b=3*a+1if a%2else a/2;return[a]+(hailstone(b),[])[a<2]
def hailstone(a):
 if a==1:return[a]
 b=(a/2,3*a+1)[int(a%2)];return[a]+(hailstone(b))

def hailstone(a):return[1]if a<2else[a]+hailstone((a/2,3*a+1)[int(a%2)])
def hailstone(a):return[1]if a<2else[a]+hailstone((3*a+1,a/2)[a%2<1])
hailstone=n=lambda a:a<2and[1]or[a]+n((a//2,3*a+1)[a%2])


print(hailstone(5))
print(hailstone(6))

print(hailstonerecursive(5))
print(hailstonerecursive(6))