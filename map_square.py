n = int(input("Enter number of elements to be inserted in List : "))
  
a = list(map(int,input("\nEnter the numbers giving space : ").strip().split()))[:n]
  
print("\nSample list is :", a)

triple = map(lambda x: x + x + x, a) 
print("\nTriple of list numbers:")
print(list(triple))