# Find the all factors of x using a loop and the operator %
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1

x=52633
factors=[]
for i in range(1,x+1):
   if x%i==0:
      factors.append(i)
print("All factors of "+str(x)+":")
print(factors)
