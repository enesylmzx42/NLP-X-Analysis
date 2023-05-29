Bu projede Twitter'dan çekilen verilerle oluşturulan veritabanı kullanılarak, girilen alternatif bir Tweet'in kime ait olabileceği yüzdesel olarak tahmin edilmektedir.

Projenin Kullanım Alanları
- Bir tweetin daha önce birisi tarafından paylaşılmış olma ihtimali hesaplanabilir.
- Daha önce paylaşılmamış bir tweetin hangi kullanıcı tarafından yazılmış olabileceği tahmin edilebilir.



Twitter'dan Veri Çekmek
Veri çekerken pythonda bulunan snscrape kütüphanesi kullanılmıştır.
Bu kütüphane temel olarak Twitter'da bulunana Advanced Search alanının yazılıma implemente edilmiş halidir.

query = "(from:netflixturkiye) until:2023-01-01 since:2021-01-01"
Verilen örnekte netflixturkiye kullanıcı adına sahip twitter hesabından 01.01.2021 - 01.01.2023 tarihleri arasındaki tüm tweetleri görmek isteyeceğimiz bir sorgu gösterilmektedir.
Daha sonrasında çekilen veriler bir csv dosyasına aktarılarak işlenmeye hazır hale getirilmektedir.


Verilerin işlenmesi
Başka bir python dosyasında içeri aktarılan veriler bir temizleme fonksiyonundan geçmektedir. 
Bu temizleme fonksiyonunda verilerin içindeki sayılar ve bazı kelimeler herhangi bir anlam ifade etmediğinden verimizin içinden çıkarılmıştır.
Devamında noktalama işaretlerinden de ayıklanan tweetlerimiz clean sütunu altına yazılmıştır.
Algoritmamızın düzgün çalışabilmesi için tweetleri etiketlememiz gerekmektedir.

* Acun Ilıcalı: 0
* Rasim Ozan Kütahyalı: 1
* Webtekno: 2
* Netflix: 3

Yukarıdaki etiketlemeye sadık kalarak verilerimizi etiketliyoruz.



Verilerden elde edeceğimiz analiz için TF-IDF, Bayes teoremi ve Decision Tree algoritmalarını kullanıyoruz.
Projemiz artık bitmiş durumda verilen bir Tweet'in 4 kullanıcıdan hangilerine ait olabileceğini sağlıklı bir şekilde oransallaştırabilmektedir.

Projemize son olarak Netflix'in eskiden attığı önerdiğim diziyi izledin mi diyorum bana nau nau diyor Tweet'ini veriyoruz ve bize aşağıdaki sonuçları veriyor.

* Acun Ilıcalı: %0.56
* Rasim Ozan Kütahyalı: %6.95
* Webtekno: %4.92
* Netflix: %87.57
