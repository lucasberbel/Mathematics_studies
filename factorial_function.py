def factorial(integer):
        """ calculates the factorial of a number and shows it formatted"""
        numbers = [x for x in range(1, integer+1)]
        number = abs(integer)
        factor = number
        while factor != 1:
                number *= (factor - 1)
                factor -= 1

       	for x in range(1, len(numbers) +1):
                if x >= 1 and x != len(numbers):
                        print(f'{numbers[-(x)]} x ' , end='  ', flush=True)
                elif (x == len(numbers)):
                        print(f'{numbers[- (x)]}', end= ' ', flush=True)
                        print(f'= {number}') 
