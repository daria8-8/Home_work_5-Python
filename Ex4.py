# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('string.txt', 'w') as data:
   data.write('AAABBBBBDDDDCCCCCCCC')
with open('string.txt', 'r') as data:
    txt = data.readline()

encoded_string = ''
prev_char = ''
count = 1
for i in txt:
    if i != prev_char:
            if prev_char:
                encoded_string += str(count) + prev_char
            count = 1
            prev_char = i
    else:
            count += 1
else:
        encoded_string += str(count) + prev_char
print(f'Закодированный текст: {encoded_string}')
with open('file_encode.txt', 'w') as data:
    data.write(encoded_string)

decoded_string = ''
char = ''
for i in encoded_string:
        if i.isdigit():
            char+=i
        else:
            decoded_string += i* int(char)
            char = ''
print(f'Раскодированный текст: {decoded_string}')
with open('file_decoded.txt', 'w') as data:
    data.write(decoded_string)