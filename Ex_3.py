# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

def find_factors(x):
    factors=[]
    for i in range(1,x+1):
        if x%i==0:
            factors.append(i)
    print(f"All factors of {x}:", factors)

for x in l:
    find_factors(x)

