test_dict = {'0': 'AA', 
             '1': 'BB', 
             '2': 'CC',
             '3': 'DD'}
print([k for k, v in test_dict.items() if v == 'CC'])