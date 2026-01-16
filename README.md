# kapıda arac girisi kontrol sistemi

Benim geliştirdiğim projede kapı önünde gelen aracı tespit ediyor. Şimdilik proje daha temel seviyede olduğu için aracı görmek için kamera değil, direkt modele bir aracın fotoğrafını gösteriyoruz. İleri aşamalarda bunu direkt canlı kameraya entegre edebiliriz.

Biz bir aracı gösterdiğimizde aracın türünü biliyor; mesela (araç car, bus, truck). Sonrasında aracın plakasını okuyor.

Okuyan plakayı veri tabanı ile karşılaştırıyor. Eğer okuduğu plaka veri tabanında mevcutsa plakaları eşleşip aracı içeri alıyor, aksi halde aracı içeri izin vermiyor. Ayrıca bunun yanı sıra eğer aracın türü "truck" ise onu da içeri almayıp engelliyor.

Ve son olarak araç hakkında VLM kullanarak bir açıklama yapıyor.

Bu bilgilerin hepsini yani ekrana yazdırıyor. Böylece her aracı gösterdiğinde yukarıda anlattığım senaryoların hepsi uygulanacaktır.

Şimdi projenin genel yapısından biraz bahsedelim: Projemizde bir main.py dosyamız ve yanında requirements.txt diye yardımcı paketlerimiz var.

**Kaynak kısmında dört tane Python dosyalarımız var:<br>**
detect_vehicle.py<br>
plate_ocr.py<br>
vlm_description.py<br>
decision_engine.py<br>

Database kısmında ise authorized_plates.csv bir dosyamız var, buradan plaka karşılaştırması olacaktır.

Ve en son input_image klasörü içinde test edeceğimiz araç fotoğrafı oluyor (test.jpg).

Yukarıda bahsettiğim yapısını şimdi adım adım her dosyada ne yaptığımı ve ne işe yaradığını kısaca anlatacağım:

main.py dosyasında bizim projemiz başlıyor, projenin beyni gibidir tüm dosyaları sırayla çağırır:<br>

from scr.detect_vehicle import detect_vehicle<br>
from scr.plate_ocr import read_plate<br>
from scr.vlm_description import describe_vehicle<br>
from scr.decesion_engine import decide_access<br>

Kaynak kısmında kısa bir şekilde dosyaları anlatacağım:

**1)detect_vehicle.py:<br>**
dosyasi araci bulup aracin turunu bililiyor Burada hazır eğitilmiş bir YOLO modeli kullandim<br>

ornek kod parcasi :<br>
from ultralytics import yolo<br>
model = yolo(yolov8n.pt)<br>
result = model (image_path)<br>

**2) plate_ocr.py :<br>**
bu dosya gorselden plakayi okuyor ve metne ceviriyor<br>
 
ornek kod parcasi :<br>
import easyocr<br>
reader = easyocr.Reader(['en'])<br>
result = reader.readtext(plate_image)<br>
sonucunda plaka metni elde ediliyor <br>

**3) vlm_description.py:<br>**
kisa ve anlasilir bir cumle yaziyor <br>
mesela :White car, sedan type vehicle<br>

ornek kod parcasi :<br>
def describe_vehicle(vehicle_type):<br>
    return f"This is a {vehicle_type} vehicle."<br>

**4)decision_engine.py:<br>**
okunan plakayi alir databaste varsa islesip aracin icere aliyor <br>

ornek kod parcasi :<br>
import pandas as pd<br>
db = pd.read_csv("data/authorized_plates.csv")<br>

if plate in db["plate"].values:<br>
    return "Access Granted"<br>
else:<br>
    return "Access Denied"<br>


ve en son projenin sonunda geldik ve sonuclari ekranda yazacaktir 
