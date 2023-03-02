def square_num(n):
  return n * n

n = int(input("Enter number of elements to be inserted in List :"))
  
a = list(map(int,input("\nEnter the numbers separated by space :").strip().split()))[:n]
  
print("\nSample List is - ", a)

result = map(square_num, a)
print("Square the elements of the list:")
print(list(result))
