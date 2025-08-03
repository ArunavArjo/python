def inverted_half_piramid(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print("\r")
n = 10
inverted_half_piramid(n)
