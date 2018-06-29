import random
游戏机会不超过三次！
print('---------我爱浩浩----------')

times = 3
secret = random.randint(1,10)
guess = 0

print('猜一下浩浩心里想的哪个数')

while (guess != secret) and (times > 0):
	temp = input()
	guess = int(temp)
	if guess == secret:
		print('猜对了')
	else：
		if guess > secret:
			print("大了")
		else:
			print("小了")
		if times > 0:
			print('再试一次吧')
		else:
			print('机会用光了')
print('游戏结束')

游戏机会不超过三次！