# module1.py

print(f'----- Running {__name__} -----')


def pprint_dict(name, d):
    print('\n\n----------------------------------------')
    print(f'***** {name} *****')
    for key, value in d.items():
        print(key, value)
    print('----------------------------------------\n\n')


pprint_dict('module1.globals', globals())

print(f'----- End of {__name__} -----')


