# Write a function that prints all factors of the given parameter x
def print_factor(x):
    factors=[]
    for i in range(1,x+1):
        if x%i==0:
            factors.append(i)
    print(f"All factors of {x}:",factors)

#print_factor(65535)
