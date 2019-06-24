

print("\n\nWelcome! To Ticket Booking System\n")
restart = ('Y')

while restart != ('H','HAYIR','hayır','h'):
	print("1.Çıkmak İçin")
	print("2.Bilet rezervasyonu")
	option = int(input("Tercihinizi girin : "))

	if option == 1:
		print("Tekrar Görüşürüz")
		exit(0)

	elif option == 2:
		insan = int(input("Kaç bilete ihtiyacınız var : "))
		isim_l = []
		yas_l = []
		cinsiyet_l = []
		for p in range(insan):
			isim = str(input("İsim : "))
			isim_l.append(isim)
			yas = int(input("Yaş  : "))
			yas_l.append(yas)
			cinsiyet  = str(input("Erkek veya Kadın mısınız? : "))
			cinsiyet_l.append(cinsiyet)

		restart = str(input("Birilerini unuttun : "))
		if restart in ('E','EVET','ok','Evet'):
			restart = ('E')
		else :
			x = 0
			print("Toplam : ",insan)
			for p in range(1,insan+1):
				print("Bilet : ",i)
				print("İsim : ", isim_l[x])
				print("Yas  : ", yas_l[x])
				print("Cinsiyet : ",cinsiyet_l[x])
				x += 1



	
