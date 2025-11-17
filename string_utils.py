def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
    digit_location = -1

    for i in range(len(formula)):
        if formula[i].isdigit:
            digit_location = i
            break
    if digit_location == -1:
        return formula, 1

    prefix = formula[:digit_location]
    num = int(formula[digit_location])
    return prefix, num
