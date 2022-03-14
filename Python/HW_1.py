# 1) Создать переменную типа String

VarString = "A sort of string"

# 2) Создать переменную типа Integer

VarInt = 15

# 3) Создать переменную типа Float

VarFloat = 17.2

# 4) Создать переменную типа Bytes

VarBytes = b'somebytes'

# 5) Создать переменную типа List

VarList = [1, 3, 17.2, "string", [13, "Andrey"]]

# 6) Создать переменную типа Tuple

VarTuple = (1, 2, 3, 45, 5, "s",)

# 7) Создать переменную типа Set

VarSet = set("hello")

# 8. Создать переменную типа Frozen set

VarFrozenset = frozenset("hayushki")

# 9) Создать переменную типа Dict

VarDict = {1: 2, 2: 4, 3: "not this time"}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

print('Task 10:')
print(VarString, ': ', 'This is a ', type(VarString), sep='')
print(VarInt, ': ', 'This is a ', type(VarInt), sep='')
print(VarFloat, ': ', 'This is a ', type(VarFloat), sep='')
print(VarBytes, ': ', 'This is a ', type(VarBytes), sep='')
print(VarList, ': ', 'This is a ', type(VarList), sep='')
print(VarTuple, ': ', 'This is a ', type(VarTuple), sep='')
print(VarSet, ': ', 'This is a ', type(VarSet), sep='')
print(VarFrozenset, ': ', 'This is a ', type(VarFrozenset), sep='')
print(VarDict, ': ', 'This is a ', type(VarDict), sep='', end='\n\n')

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.

VarString1 = 'first string'
VarString2 = 'second string'
FinalString = VarString1 + ' and ' + VarString2
print('Task 11: ' + 'Final string is: ', FinalString, end='\n\n')

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.

VarInt1, VarInt2 = 54, 32
VarSum = VarInt1 + VarInt2

print('For Tasks 13 - 16: First integer = ', VarInt1, ', Second integer = ', VarInt2, sep='', end='\n\n')

print('Task 12: ', 'First Integer=', VarInt1, '; Second Integer=', VarInt2, '; Sum = First Integer + Second Integer',
      '; Sum=', VarSum, sep='')

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.

VarDiv = VarInt1 / VarInt2
print('Task 13: ', 'Divident=', VarInt1, '; Divider=', VarInt2, '; Qotient = Divident / Divider', '; Qotient=', VarDiv,
      sep='')

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.

VarMult = VarInt1 * VarInt2
print('Task 14: ', 'Multiplicator_1 = ', VarInt1, '; Multiplicator_2 = ', VarInt2,
      '; Result_of_Multiply = Multiplicator_1 * Multiplicator_2', '; Result_of_Multiply = ', VarMult, sep='')

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.

VarIntDiv = VarInt1 // VarInt2
print('Task 15: ', 'Int_Divident = ', VarInt1, '; Int_Divider = ', VarInt2, '; Int_Div = Int_Divident // Int_Divider',
      '; Int_Div=',
      VarIntDiv, sep='')

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.

VarDivRemainder = VarInt1 % VarInt2
print('Task 16: ', 'Rem_Divident = ', VarInt1, '; Rem_Divider = ', VarInt2,
      '; Div_Remainder = Rem_Divident % Rem_Divider',
      '; Div_Remainder=', VarDivRemainder, sep='', end='\n\n')

# 17) (7 + 12)**3 + 7 * 4 - 44 / 2**4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.

print('Task 17: correct expression is "(7 + 12)**3 + 7 * 4 - 44 / 2**4" = ', (7 + 12) ** 3 + 7 * 4 - 44 / 2 ** 4)
