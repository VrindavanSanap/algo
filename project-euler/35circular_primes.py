import sympy


def get_number_rotations(number):
    number_str = str(number)
    rotations = []

    for i in range(len(number_str)):
        rotated_str = number_str[i:] + number_str[:i]
        rotations.append(int(rotated_str))

    return rotations
def are_all_numbers_in_list_prime(numbers):
    for i in numbers:
        if not sympy.isprime(i):
            return False
    return True
counter = 0
for i in range(10**6):
    if sympy.isprime(i):
          if are_all_numbers_in_list_prime(get_number_rotations(i)):
              counter+=1
              print(i,counter)
          
          