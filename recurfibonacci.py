def recur_fibo(n):
  if nterms <= 0:
    print("Plese enter a positive integer")
  else:
    print("Fibonacci sequence:")
    for i in range(nterms):
       print(recur_fibo(i))
