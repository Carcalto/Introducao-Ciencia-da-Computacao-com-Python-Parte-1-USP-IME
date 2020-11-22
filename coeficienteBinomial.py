def fatorial (x):
    fat = 1
    if x == 0 or x == 1:
       fat = fat
       
    else:
          while x > 1:
              fat = fat * x
              x = x - 1

          
    
    return fat


def coeficiente_Binomial (n, k):
    
    return fatorial (n) / (fatorial (k) * (fatorial (n - k)))

print (coeficiente_Binomial (5,3))