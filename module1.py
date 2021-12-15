#def Plosad(stor1:float,stor2:float)->float:
#	"""nahosdenie plosadi
#	:param float stor1: pramougolnik pervaja storona
#	:param float stor2: pramougolnik vtoraja storona
#	:rtype:float
#	"""
#	S=stor1*stor2
#	return S


#def arithmetic(chislo1:float, chislo2:float, operacia:str)->float:
#	"""решает задачи с использованием +,-,*,/ при других операциях выводит на экран сообщение о не использовании данных опериций
#	:param float chislo1: chislo pervoja
#	:param float chislo2: chislo vtorojo
#	:param str operacia: operacia
#	:rtype:var
#	"""
#	if operacia in['+','-','*','/']:
#		if operacia=='+':
#			otvet=chislo1+chislo2
#		elif operacia=='-':
#			otvet=chislo1+chislo2
#		elif operacia=='*':
#			otvet=chislo1+chislo2
#		elif operacia=='/':
#			otvet=chislo1+chislo2
#		if operacia=='/' and chislo2==0:
#			otvet='На ноль делить нельзя'
#		return otvet


#def is_year_leap(year:int):
#	"""
#	:param int year: год
#	rtype:bool
#	"""
#	if year%4==0:
#		otvet=True
#	else:
#		otvet=False
#	return otvet


#from math import *
#def square(storona:float):
#	"""
#	:param float storona: сторона квадрата
#	:rtype:float
#	"""
#	P=storona*4
#	S=storona*storona
#	D=round(sqrt(2)*storona,1)
#	return P,S,D


#def season(mesac:int):
#	"""
#	:param int mesac: номер месяца
#	:rtype:str:
#	"""

#	if mesac in[12,1,2]:
#		otvet='зима'
#	elif mesac in[3,4,5]:
#		otvet='весна'
#	elif mesac in[6,7,8]:
#		otvet='лето'
#	elif mesac in[9,10,11]:
#		otvet='осень'
#	return otvet


#def bank(money:int, years:int):
#	"""
#	:param int money: сумма вклада
#	:param int years: срок вклада
#	:rtype:int
#	"""
#	for i in range(years):
#		money*=1.1
#	return money


#def is_prime(num:int):
#	"""
#	:param int num: число
#	:rtype:bool
#	"""
#	count=0
#	if num<0>=1000:
#		for i in range(2,10):
#			if num%i==0:
#				count+=1
#			if num==i:
#				count-=1
#		if count in [0,1]:
#			otvet=True
#		else:
#			otvet=False
#	return otvet


#def date(d:int,m:int,y:int):
#	"""
#	:param int d: день
#	:param int m: месяц
#	:param int y: год
#	:rtype: bool
#	"""
#	import datetime
#	try:
#		data=datetime.date(y,m,d)
#		otvet=True
#	except:
#		otvet=False
#	return otvet


def XOR_cipher(line:str,key:str):
	"""
	:param str line: (не)зашифрованная строка 
	:param str key: ключ шифрования
	:rtype: var
	"""
	if key=='XOR':
		cipher = list(line.strip(" "))
		for i in range(len(cipher)):
			cipher.insert(i,str(ord(cipher[i])))
			cipher.pop(i+1)
	return ''.join(cipher)
	
