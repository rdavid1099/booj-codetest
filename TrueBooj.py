def truebooj(number):
    result = ''
    if number % 10 == 0:
        result += 'TrueBooj '
    if number % 3 == 0:
        result += 'True '
    if number % 5 == 0:
        result += 'Booj'
    result = str(number) if result == '' else result
    return result
