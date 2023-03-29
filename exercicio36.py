prod = 0

for c in range (1, 51):
   print (c, end = " ")
   print("-" * 20, end = " ")
   prod = prod + 0.18
   print(f"{prod: .2f}")