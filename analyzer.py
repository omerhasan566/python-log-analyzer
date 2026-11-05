#Dosyanın yolunu belirliyoruz
log_dosyasi ="semple_logs.txt"

#Dosyanın okuma modunda ('r' - read) açıyoruz
with open(log_dosyasi, "r") as dosya:

    #Dosyadaki her bir satırı sırayla okuyan bir döngü başlatıyoruz
    for satir in dosya:
        #Eğer okunan satırın içinde "Faild" kelimesi geçiyorsa o satırı yazdır.
        if "Failed" in satir:
            print(satir.strip())