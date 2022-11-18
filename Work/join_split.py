from ntpath import join
from posixpath import split
from art import tprint
tprint('SPLIT_JOIN') #font='bulbhead')

# a = "1,2,3,4,5,6"
# print(a.split(','))
# ['1', '2', '3', '4', '5', '6']

# a = "Ivan Ivan Inwn"
# print(a.split('I'))
# ['', 'van ', 'van ', 'nwn']

# a = input().split('')
# print(a)
# 12 43 54654 7454563
# ['12', '43', '54654', '7454563']

######### JOIN ########

# a = ['12', '43', '54654', '7454563']
# b = '_'.join(a)
# print(b)
# 12_43_54654_7454563

# a = [12, 43, 54654, 7454563] # int - ОШИБКА
# print('_'.join([str(i) for i in a])) # Обход системы через генератор

# a = [12, 43, 54654, 7454563]
# print('\n'.join([str(i) for i in a]))
# 12
# 43
# 54654
# 7454563

# a = "+79963416344"
# print(['|'.join(i for i in a)])
# ['+|7|9|9|6|3|4|1|6|3|4|4']
