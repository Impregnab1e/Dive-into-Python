def reverse_kwargs(**kwargs):
    reversed_dict = {}
    for key, value in kwargs.items():
        reversed_dict[value] = key
    return reversed_dict


kwargs_dict = reverse_kwargs(rev=True, acc="YES", stroka=4)
print(kwargs_dict)
