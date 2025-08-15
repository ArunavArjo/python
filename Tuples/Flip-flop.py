def flip_flop(tuple):
    l = len(tuple )-1
    f = 0
    while(f<l):
            if (tuple[l] != tuple[f]):
                  return False
            f +=1
            l-+1
            return True
yu = (1,2,3,4,3,2,1)
if(flip_flop(yu)):
    print("The tuple is Flip_flop")
else:
      print("The tuple is not Flip_flop")
