a = {1,2,3,4,5,6,3,4,4}


#  >>>2 in a
#  >>>True

b = {3,4,5,1,8,2}

#list

people = {'bob':'blue', 'sara':'green'}

print people

var = 6
print var

def recur_fact(x):
   """This is a recursive function
   to find the factorial of an integer"""

   if x == 1:
       return 1
   else:
       return (x * recur_fact(x-1))


num = int(input("Enter a number: "))
if num >= 1:
   print("The factorial of", num, "is", recur_fact(num))
   
