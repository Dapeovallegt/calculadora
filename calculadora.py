def suma(): 
	A=input("ingrese su primer numero: ")
	B=input("ingrese su segundo numerio: ")
	print A+B

def resta():
	a=input("ingrese el primer numero: ")
	b=input(" ingrese el segundo balor: ")
	print a-b

def divi():
	a=input("ingrese el primer numero: ")
	b=input("ingrese el segundo numero: ")
	print a/b
def mult():
	a=input("ingrese su primer valor: ")
	b=input("ingrese el segundo numero: ")
	print a*b

def potencia():
	a=input("ingrese su valor: ")
	print a*a 

def menu():
	print"-------------------HOLA ELIGE UNA OPSION-----------------------------------"
	print "1 suma"
	print "2 resta"
	print "3 division"
	print "4 multi"
	print "5 potencias"
	opcion=raw_input("ingrese su numero de opcion: ")
	if opcion.isalpha()==False:
		if opcion=="1":
			print "-----------------ha elegido suma -------------"
			suma()
		if opcion=="2":
			print "------------------------ha elegido resta---------"
			resta()
		if opcion=="3":
			print"-----------------------ha elegidodivicion----------"
			divi()
		if opcion=="4":
			print "-------------------------ha elegido multi-----------"
			mult()
		if opcion=="5":
			print "---------------------------ha elegido una potencia------------"
			potencia()
	else:
		print"ingrese solo numeros porfavor"
		menu()

menu()
