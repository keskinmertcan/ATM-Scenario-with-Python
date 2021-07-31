import random

ikiyuzluk = 100
yuzluk = 100
ellilik = 100
yirmilik = 100
onluk = 100

dakika = 0
saat = 8
sirano = 0

liste = ['Mehmet','Fatma','Mertcan','Fatih','Cihan','Emine','Servet','Müge','Berk']

z = ikiyuzluk+yuzluk+ellilik+yirmilik+onluk



while saat < 17:
    if (z != 0):
        r = random.randint(1, 11)
        if (r != 4):
            
            p = random.randint(1, 200)*10
            
            v = 200*ikiyuzluk
            h = 100*yuzluk
            n = 50*ellilik
            m = 20*yirmilik
            k = 10*onluk
            atm = v+h+n+m+k
            
            if p<atm:
                
                a=int(p/200)
                if ikiyuzluk>=a:
                    ikiyuzluk=ikiyuzluk-a
                    u=200*a
                    p1=p-u
                else :
                    p1=p
                    
                b=int(p1/100)
                if yuzluk>=b:
                    yuzluk=yuzluk-b
                    u1=100*b
                    p2=p1-u1
                else :
                    p2=p1
                    
                c=int(p2/50)
                if ellilik>=c:
                    ellilik=ellilik-c
                    u2=50*c
                    p3=p2-u2
                else :
                    p3=p2
                    
                d=int(p3/20)
                if yirmilik>=d:
                    yirmilik=yirmilik-d
                    u3=20*d
                    p4=p3-u3
                else :
                    p4=p3
                    
                e=int(p4/10)
                if onluk>=e:
                    onluk=onluk-e
                    u4=10*e
                    p5=p4-u4

                    sure = random.randint(5, 30)
                    dakika=dakika+sure
                    if dakika >= 59:
                        saat=saat+1
                        dakika=dakika-59
                        
                    sirano = sirano+1
                    kisi = random.choice(liste)
                    
                    print ()
                    print ("Hoşgeldin",kisi)
                    print ("İşlem Saati:",saat,":",dakika)
                    print ("Sıra No:",sirano)
                    print (p , "TL Para Çekildi")
                    print (a,"adet 200,",b,"Adet 100,",c,"Adet 50,",d,"Adet 20,",e,"Adet 10 Banknot çekildi" )
                    print ("ATM'de", ikiyuzluk,"adet 200,",yuzluk,"Adet 100,",ellilik,"Adet 50,",yirmilik,"Adet 20,",onluk,"Adet 10 Banknot kaldı" )
                    print ("Sağlıklı Günler", kisi)
                    print ()
            else:
                sure = random.randint(5, 30)
                dakika=dakika+sure
                if dakika >= 59:
                    saat=saat+1
                    dakika=dakika-59
                sirano = sirano+1
                kisi = random.choice(liste)
                print ()
                print ("Hoşgeldin",kisi)
                print ("İşlem Saati:",saat,":",dakika)
                print ("Sıra No:",sirano)
                print ("Bankamatik",p,"'yi karşıyalamadı. Önerilen",atm,"TL parayı kabul ettiniz.")
                print (a,"adet 200,",b,"Adet 100,",c,"Adet 50,",d,"Adet 20,",e,"Adet 10 Banknot çekildi" )
                print ("ATM'de Banknot Kalmadı.")
                ikiyuzluk = 0
                yuzluk = 0
                ellilik = 0
                yirmilik = 0
                onluk = 0
                break
        else :
            p = random.randint(1, 200)*10
            a=int(p/200)
            if a < 11:
                ikiyuzluk=ikiyuzluk+a
                u=200*a
                p1=p-u
            else :
                p1=p
            b=int(p1/100)
            if b < 11:
                yuzluk=yuzluk+b
                u1=100*b
                p2=p1-u1
            else :
                p2=p1
            c=int(p2/50)
            if c < 11:
                ellilik=ellilik+c
                u2=50*c
                p3=p2-u2
            else :
                p3=p2
            d=int(p3/20)
            if d < 11:
                yirmilik=yirmilik+d
                u3=20*d
                p4=p3-u3
            else :
                p4=p3
            e=int(p4/10)
            if e < 11:
                onluk=onluk+e
                u4=10*e
                p5=p4-u4

                sure = random.randint(5, 30)
                dakika=dakika+sure
                if dakika >= 59:
                    saat=saat+1
                    dakika=dakika-59
                sirano = sirano+1
                kisi = random.choice(liste)
                print ()
                print ("Hoşgeldin",kisi)
                print ("İşlem Saati:",saat,":",dakika)
                print ("Sıra No:",sirano)
                print (p , "TL Para Yatırıldı")
                print (a,"adet 200,",b,"Adet 100,",c,"Adet 50,",d,"Adet 20,",e,"Adet 10 Banknot yatırıldı" )
                print ("ATM'de", ikiyuzluk,"adet 200,",yuzluk,"Adet 100,",ellilik,"Adet 50,",yirmilik,"Adet 20,",onluk,"Adet 10 Banknot var" )
                print ("Sağlıklı Günler",kisi)
                print ()
        
    else :
        print ("ATM'de Banknot Bulunamaktadir.")
        print ("En Yakın ATM'yi www.scaryfox.com/atm adresinden bulabilirsiniz")

print ("ScaryFox ATM şu anda çevrimdışıdır.")
