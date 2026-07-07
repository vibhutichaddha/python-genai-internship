numbers = list(range(1,51))
even=[num for num in numbers if num%2==0]
odd=[num for num in numbers if num%2!=0]
divisible_by_3_and_5=[num for num in numbers if num%3==0 and num%5==0]
print ("Even numbers:",even)
print ("Odd numbers:",odd)
print ("Numbers divisible by both 3 and 5:",divisible_by_3_and_5)