def b_element(number):
    result = []
    for i in range(1, len(number)):
        if number[i] > number[i-1]:
            result.append(number[i])
    return result
    

number = input().split()
result = b_element(number)
print(result)



