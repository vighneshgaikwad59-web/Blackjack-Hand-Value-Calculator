def Black_jacked(a,b,c):
    total=(a+b+c)
    if total<=21:
        return total
    elif total>=21 and 11 in [a,b,c]:
        total=-10
        if total<=21:
         return total
        else:
           return 'BLAST'
    else:
       return'Blast'
print(Black_jacked)