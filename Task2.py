# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите логическое значение переменной "X" (true или false): '))
y = bool(input('Введите логическое значение переменной "Y" (true или false): '))
z = bool(input('Введите логическое значение переменной "Z" (true или false): '))


result = bool((not (x or y or z)) == (not x and not y and not z))
print('')
print(f'При вышезаданных значениях переменных, предикат (утверждение): "¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z" - {result}')

# /\ - AND, &, И, логическое умножение, коньюкция
# \/ - OR, |, ИЛИ, логическое сложение, дизьюкция
# ¬ - NOT, !,~, НЕ, отрицание, инверсия

# X	     Y	     Z	  ¬(X⋁Y⋁Z) ¬X⋀¬Y⋀¬Z result
# true	true	true	false	false	true
# true	true	false	false	false	true
# true	false	true	false	false	true
# true	false	false	false	false	true
# false	true	true	false	false	true
# false	true	false	false	false	true
# false	false	true	false	false	true
# false	false	false	true	true	true