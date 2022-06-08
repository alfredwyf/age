driving = input('do you have driving experience?' )
if driving != 'yes' and driving != 'no':
	print('please input your answer with yes or no only')
	raise SystemExit
	
age = input('What is your age? ')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('you have passed this exam')
	else:
		print('why you have tried to drive? so weird')
elif driving == 'no':
	if age >= 18:
		print('you can go learn how to drive now')
	else:
		print('you can start learning how to drive at your 18')

else:
	print('please input yes or no only')