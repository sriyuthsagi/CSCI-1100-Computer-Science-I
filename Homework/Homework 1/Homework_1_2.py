first = input('First => ')
print(first)
second = input('Second => ')
print(second)
print('Example variable names')

lowercase = first.lower() + '_' + second.lower()
print('Lower case:', lowercase)

constant = first.upper() + '_' + second.upper()
print('For constants:', constant)

camel = first.capitalize() + second.capitalize()
print('Camel case:', camel)

system = '_' + lowercase
print('System variables:', system)

silly = first + '_' + second
silly = silly.replace('a','_')
silly = silly.replace('e','_')
print('Silly variable:', silly)