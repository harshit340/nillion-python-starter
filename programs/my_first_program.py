from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    zero = SecretInteger(0) 

    # Perform bitwise addition directly
    while my_int2 != zero:
        carry = my_int1 & my_int2
        my_int1 = my_int1 ^ my_int2
        my_int2 = carry << 1

    # The result is stored in `my_int1` after the loop
    result = my_int1

    # Return the result as output
    return [Output(result, "my_output", party1)]

