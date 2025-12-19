def decimal_to_binary(decimal_num):
    
    if decimal_num == 0:
        return "0"

    binary_result = ""
    temp_num = decimal_num

    while temp_num > 0:
        remainder = temp_num % 2
        binary_result = str(remainder) + binary_result
        temp_num = temp_num // 2

    return binary_result


number = 45
binary_output = decimal_to_binary(number)

print(f"The decimal number {number} is {binary_output} in binary.")

number_zero = 0
binary_output_zero = decimal_to_binary(number_zero)

print(f"The decimal number {number_zero} is {binary_output_zero} in binary.")
