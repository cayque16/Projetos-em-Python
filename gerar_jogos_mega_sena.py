import random

def gera_jogo_mega():
    nums = []
    while len(nums) < 6:
        num = random.randint(1,60)
        if not num in nums:
            nums.append(num)
    nums.sort()
    nums = list(map(lambda num: '0'+str(num) if num < 10 else str(num),nums))
    return ' '.join(nums)

for i in range(int(input('Quantos jogos voce quer gerar? '))):
    print(gera_jogo_mega())