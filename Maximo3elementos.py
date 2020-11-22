def maximo (x, y, z):
  
  if x >= y and x >= z:
         aux = x

  if y >= x and y >= z:
         aux = y
   
  if z >= x and z >= y:
         aux = z
        

         
  return aux
 


print (maximo (72, 72, 73))