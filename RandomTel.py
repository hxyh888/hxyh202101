import random
#随机生成一个手机号码
list_num = [130,131,132,133,134,135,136,126,138,139,147,150,151,152,153,155,156,157,158,159,166,177,173,176,180,181,183,184,185,186,187,188,189,199,170,171]
num1 = []
falg = True
while falg:
    for i in range(8):
        num = str(random.randint(0, 9))
        num1.append(num)
        if i == 7:
            falg = False

start_tel = random.choice(list_num)
tel = str(start_tel)+("".join(num1))
print(tel)
