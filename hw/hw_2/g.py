"""
У вас есть список из положительных целых чисел. Вам нужно сжать его в строку следующим образом: все числа должны
идти через запятую, однако, если 3 и более числа идут последовательно их нужно заменить на интервал написанный
через "-".

"1 2" -> "1,2"
"1 2 3" -> "1-3"
"1 2 3 5" -> "1-3,5"

Формат ввода
Положительные целые числа разделенные пробелом

Формат вывода
Сжатая строка
"""

nums = list(map(int, input().strip().split()))


def compress_next(idx):
    if idx == len(nums) - 1:
        return False
    return nums[idx + 1] == nums[idx] + 1


result = []
first, last = None, None

for i, num in enumerate(nums):
    to_compress = compress_next(i)

    if to_compress and not first:
        first = num
    elif not to_compress and not first:
        result.append(str(num))
    elif not to_compress and first:
        last = num
        if first != last - 1:
            result.append(f'{first}-{last}')
        else:
            result.extend([str(first), str(last)])
        first, last = None, None

print(','.join(result))
