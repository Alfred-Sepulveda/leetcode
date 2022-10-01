nterms = int(input("how many terms?"))

n1, n2 = 0,1
count = 0

if nterms <= 0:
    print("please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci Sequence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# // count < nterms //0<15  0 1 2 3 4 5 6
# // print(n1)      // n1 = 0 1 1 2 3 5 8
# //nth = n1 + n2   // nth= 1 2 3 5 8 13
# //n1 = n2         // n1 = 1 1 2 3 5 8
# //n2 = nth        // n2 = 1 2 3 5 8 13
# //count += 1      //cnt = 1 2 3 4 5 6
