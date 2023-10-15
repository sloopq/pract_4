def men_mest(number):
    if len(number) < 2:
        return number
    
    min_i = number.index(min(number))
    max_i = number.index(max(number))

    number[min_i],  number[max_i] = number[max_i], number[min_i]
    

    return number

number = input().split()

result = men_mest(number)
print(*result)