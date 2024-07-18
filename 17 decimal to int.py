def base17_to_decimal(number):
    decimal_value = 0
    base = 17

    # Iterate through each digit of the number
    for i, digit in enumerate(reversed(number)):
        # Convert alphabetic characters to their decimal equivalents
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit.upper()) - ord('A') + 10

        # Calculate the contribution of this digit to the decimal value
        decimal_value += digit_value * (base ** i)

    return decimal_value
number=input()
print(base17_to_decimal(number))