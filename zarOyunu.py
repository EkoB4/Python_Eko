Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> import time
>>> while True:
	zar_1 = random.randint(1, 6)
	zar_2 = random.randint(1, 6)
	if zar_1==6 and zar_2==6:
		print("""Deneme{}:\t({},{}) geldi tebrikler !*** """.format(i, zar_1, zar_2))
		time.sleep(2)
		break
	print("""Deneme{}:\t({},{}))""".format(i,zar_1, zar_2))
	i+=1
	time.sleep(0.5)
	print("""\n*** {}. denemede (6,6) geldi mi? ***""".format(i))
