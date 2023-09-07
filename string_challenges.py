print('#####Задача №1#####')
# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

print('#####Задача №2#####')
# Вывести количество букв "а" в слове
word = 'Архангельск'
sum = 0
for a in word.lower():
    if a == 'а':
        sum += 1
print(sum)

print('#####Задача №3#####')
# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
sum_vowels = 0
for v in word.lower():
    if v in vowels:
        sum_vowels += 1
print(sum_vowels)

print('#####Задача №4#####')
# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

print('#####Задача №5#####')
# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
[print(s[0]) for s in sentence.split()]

print('#####Задача №6#####')
# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sum = 0
for s in sentence.split():
    sum += len(s)
avg = sum / len(sentence.split())
print(avg)
