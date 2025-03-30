"""
Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов:
+7<код><номер>, 8<код><номер>, <номер>, где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых скобках.
Если код не указан, то считается, что он равен 495. Кроме того, в записи телефонного номера может стоять знак “-”
между любыми двумя цифрами. На данный момент в адресной книге телефона Васи записано всего три телефонных номера,
и он хочет записать туда еще один. Но он не может понять, не записан ли уже такой номер в телефонной книге. Помогите ему!
Два телефонных номера совпадают, если у них равны коды и равны номера. Например, +7(916)0123456 и 89160123456 — это один и тот же номер.
"""

global_num = input()
makeform = str.maketrans('()+-', '    ')
global_num = global_num.translate(makeform).replace(' ', '').replace(' ', '')
if len(global_num) == 7:
	global_num = '8495' + global_num

for _ in range(3):
    local_num = input().translate(makeform).replace(' ', '').replace(' ', '')
    if len(local_num) == 7:
        local_num = '8495' + local_num
    if (len(global_num) in [10, 11]) and (len(local_num) in [10, 11]):
        min_len = min(len(global_num), len(local_num))
        if min_len == 11:
            min_len -= 1
        print('YES' if global_num[-min_len:] == local_num[-min_len:] else 'NO')
        continue
    print('NO')