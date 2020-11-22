def fizzbuzz(n):
    if n % 3 == 0 and n % 5 != 0:
        final = "Fizz"
    
    if n % 3 != 0 and n % 5 == 0:
        final = "Buzz"
            
    if n % 3 == 0 and n % 5 == 0:
        final = "FizzBuzz"           
    
    if n % 3 != 0 and n % 5 != 0:
        final = n
    
    return final


print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(4))