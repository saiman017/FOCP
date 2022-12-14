#
slices = int(input('How many slices of spam: '))

if slices == 1:
    print('Egg with spam coming up!')
else:
    print(f'Egg with {"spam, " * (slices - 1)}and spam coming up!')