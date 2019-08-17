def mul_by_three(arg):
    return arg * 3


def mul_by_two(arg):
    return arg * 2


def div_things(a, b=1):
    print('dělím a / b')
    return a / b


if __name__ == '__main__':
    x = 5
    y = 6
    my_variable = 'tOHle jE prOMěnNá'
    # print(my_variable)
    my_int_variable = 6
    # print(mul_by_three(my_int_variable))
    # print(mul_by_three(5))
    # print(mul_things(4, 5))
    # print(div_things(b=x, a=y))
    # print(div_things(a=2))
    # arr = list((0, 1, 2, 3, 4))
    # my_list = [1, 2, 3, 5, 10]
    # my_tup = (1, 2, 3, 5, 10)

    # print(6 + 4)
    # print(6 - 4)
    # print(6 * 4)
    # print(6 ** 4)
    # print(6 / 4)
    # print(6 // 4)
    # print(6 % 4)
    # print(divmod(6, 5))
    #

    my_number = -84
    is_even = (my_number % 2) == 0  # zbytek po dělení 2 je 0
    is_divisible_by_five = (my_number % 5) == 0
    is_positive = my_number > 0
    is_divisible_by_ten = is_even and is_divisible_by_five
    if is_even:
        print('is even')
    if is_divisible_by_five:
        print('is divisible by five')
    if is_divisible_by_ten:
        print('is divisible by 10')
    if is_even or is_divisible_by_five:
        print('is divisible by 2 or 5')
    if is_positive and (is_even or is_divisible_by_five):  # zkratka pro else if
        print('is positive and divisible by (2 or 5)')
    # else:
    #     print('is not divisibe by two nor five')
    # #
    # if my_variable == 'tohle je proměnná':
    #     print('tohle je proměnná')
    # elif my_variable == 5:
    #     print('tohle je pětka')
    # else:
    #     print('tohle není šestka')


    # for i in range(15, 5, -3):
    #     print(i)
    # print(type(my_list))
    # print(type(my_tup))
    # print('printing my_list')
    # for k, i in enumerate(my_list):
    #     print(k, i)
    # print(my_variable[0])
    # print(my_variable[-1])

    # my_list_2 = my_list.copy()
    #
    # my_outputs = []
    # for pozice, hodnota in enumerate(my_list):
    #     my_list_2[pozice] = mul_by_two(hodnota)
    #     print(type(pozice), type(str(pozice)))
    #     # what_im_doing = 'zapisuju na pozici' + str(pozice) + ' hodnotu ' + str(hodnota) + ' vynasobenou 2'
    #     what_im_doing = f'zapisuju na pozici {pozice} hodnotu {hodnota} vynasobenou 2'
    #     # print(what_im_doing)
    #     my_outputs.append(what_im_doing)

    # my_list_2 = [mul_by_two(i) for i in my_list]

    # print(my_list_2)
    # print(my_outputs)
    # print(my_variable)
    # print(len(my_variable), type(len(my_variable)))
    # len_half = len(my_variable) / 2
    # print(len_half, type(len_half))
    # print(int(len_half), type(int(len_half)))
    # print(0.7, int(0.7))
    # print(my_variable[2], type(my_variable[2]))
    # print(my_variable.lower())
    # print(my_variable.endswith('ná'))
    # print(my_variable.upper())
    # print(my_variable.capitalize())
    # print('printig my_tup')
    # for i in my_tup:
    #     print(i)
    # my_list.append(11)
    # print('printing my_list')
    # for i in my_list:
    #     print(i)

    # todo: vlastní třídy, magické proměnné
    # todo: vysvětlit globální/lokální proměnné
    # todo: probrat booleovské výrazy a not
    # for i in my_variable:
    #     print(i)
