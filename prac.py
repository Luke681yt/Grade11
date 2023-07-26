def base10_to_hex(num):
    hex_digits = '0123456789ABCDEF'
    hex_str = ''

    while num > 0:
        # Get the remainder of the division by 16
        remainder = num % 16
        # Get the corresponding hexadecimal digit
        digit = hex_digits[remainder]
        # Prepend the digit to the hexadecimal string
        hex_str = digit + hex_str
        # Divide the number by 16 and floor the result
        num = num // 16

    return hex_str

# Test the function
print(base10_to_hex(255))  # prints 'ff'
print(base10_to_hex(10))   # prints 'a'
print(base10_to_hex(16))   # prints '10'

a=int(input())
print(base10_to_hex(a))