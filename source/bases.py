#!python
import string

def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    assert 2 <= base <= 36
    # TODO: Decode number
    # Anything Base 10 or smaller uses digits
    # Anything base 11 or larger uses alpha numeric chrs
    # Handles Binary
    str_num = str_num.lower()
    conversions = []
    if str_num.isdigit() and base < 11:
        for num, exponent in zip(str_num, reversed(range(len(str_num)))):
            value = int(num) * (2 ** exponent)
            conversions.append(value)
        decoded = sum(conversions)
        print(decoded)
    else:
        alphabet = list(string.ascii_lowercase)
        for num, exponent in zip(str_num, reversed(range(len(str_num)))):
            if num in alphabet:
                letter_value = 10 + alphabet.index(num)
                conversions.append(letter_value)
            else:
                value = int(num) * (2 ** exponent)
                conversions.append(value)
        decoded = sum(conversions)
        print(decoded)

    return decoded

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    assert 2 <= base <= 36
    # TODO: Encode number
    # Handles Binary
    conversion = []
    while num is not 0:
        remainder = num % base
        conversion.append(str(remainder))
        num = num / base
    conversion = conversion[::-1]
    conversion = "".join(conversion)
    return conversion

def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number
    converted = decode(str_num, base1)
    converted = encode(converted, base2)
    print(converted)
    return converted

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    # main()
    decode('10', 2)
    # encode(10, 2)
    # convert('1010', 2, 3)
