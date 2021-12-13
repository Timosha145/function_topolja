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


