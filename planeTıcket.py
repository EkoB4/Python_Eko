Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class uçak_bilet:
	def kontrol_işlemleri(adsoyad, yas, yer, tarih,):
		ad = str(input"""İsminiz ve soyadınız? : """)
		#Uyarı isim soyad yazarken (İsim Soyad) şeklinde boşlukla yazınız.#
		tarih input("""Gideceğiniz Tarihi ve yeri yazınız""")
		#Uyarı Tarih yazarken örn(2020 Mart ) şeklinde boşlukla yazınız.#
		yer str(input"""Gideceğiniz yeri yazın: """)
		
		yas=int(input"""Yaşınız? : """)
		if yas > 17:
			print(,yer," Biletiniz",tarih,"tarihine",adsoyad,"ismine verilmiştir")
		else:
			print("Yaşınız gereği bilet alamamakasınız",adsoyad,)
			
			#First Original project JREkin#
