

print("Welcome to Credit Card Validator")

#Checksum
def checker(val):
	cardArr = [int(d) for d in str(val)]
	checkNum = cardArr[len(cardArr)-1]
	cardArr.pop()
	#double every other
	for i in range(len(cardArr)):
		if i == 0 or i % 2 == 0:
			cardArr[i] = cardArr[i]*2

	#If double digit add digits together
	def adder(x):
		if x > 10:
			return sum([int(d) for d in str(x)])
		return x

	cardArr = map(adder,cardArr)

	return "Valid Credit Card Number" if (sum(cardArr) + checkNum) % 10 == 0 else "Not a valid Credit Card Number"


#Start the Check
while True:
	try:
		creditCard = int(input("Please enter your card number with no dashes or spaces please: "))
	except:
		print("Only numbers please")
		continue
	else:
		if len(str(creditCard)) == 16:
			print("Thank you now checking")
			break
		else:
			print("Not 16 digits")
			continue

print(checker(creditCard))

