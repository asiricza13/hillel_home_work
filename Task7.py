'''Напишіть програму, яка по даному числу n від 1 до 9 виводить на екран n пінгвінів.
Зображення одного пінгвіна має розмір 5 × 9 символів, між двома сусідніми пінгвінами також є порожній (з пропусків) стовпець.
Дозволяється вивести порожній стовпець після останнього пінгвіна.
Для спрощення малювання скопіюйте пінгвіна з прикладу в середовище розробки.
'''





x= ["   _~_    ",
    "  (o o)   ",
    " /  V  \  ",
    "/(  _  )\ ",
    "  ^^ ^^   "]
n=int(input("Введіть кількість пінгвінів:"))

for i in x:

    print(i * n)