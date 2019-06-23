Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class uçak_bilet:
	def kontrol_işlemleri(adsoyad, yas):
		ad = str(input"""İsminiz ve soyadınız? : """)
		#Uyarı isim soyad yazarken (isim soyad) şeklinde boşlukla yazınız.#
		yas=int(input"""Yaşınız? : """)
		if yas > 17:
			print("Biletiniz hazır",adsoyad,"efendim bizi tercih etiğiniz için teşşekkürler")
		else:
			print("Yaşınız gereği bilet alamamakasınız",adsoyad,)
			#First Original project JREkin#
