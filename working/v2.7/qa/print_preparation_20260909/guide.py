"""A short user guide plus one duplex calibration sheet, separate from the deck."""
from common import *
from reportlab.pdfgen import canvas
from reportlab.platypus import Table,TableStyle

SOURCES=[('Adobe: ölçeklendirme','https://helpx.adobe.com/uk/acrobat/kb/scale-or-resize-printed-pages.html'),('Adobe: çift taraflı baskı','https://helpx.adobe.com/uk/acrobat/desktop/print-documents/print-duplex-and-multi-page-document/set-double-side-print.html'),('Epson: elle çift taraflı baskı','https://www.epson.co.uk/faq/KA-01558/contents?loc=en-us'),('MB Print: taşma ve güvenli alan','https://mbprint.pl/en/instruction/cards/')]

def heading(c,n,title):
    c.setFillColor(NAVY);c.setFont('Title',21);c.drawString(20*mm,269*mm,title)
    c.setFont('Bold',8);c.drawString(20*mm,283*mm,'FOULWAKE / A4 BASKI')
    c.setFillColor(INK);c.setFont('Body',8);c.drawString(20*mm,12*mm,'v2.7 · 09.09.2026');c.drawRightString(190*mm,12*mm,str(n))

def p(c,s,y,size=10.3):return y-text(c,s,20*mm,y,170*mm,size)-5*mm

def trial_card(c,label,x,y,w,h,angle):
    c.saveState()
    if angle==90:c.translate(x+h,y);c.rotate(90)
    elif angle==270:c.translate(x,y+w);c.rotate(-90)
    else:c.translate(x,y)
    c.setStrokeColor(INK);c.setLineWidth(.5);c.rect(0,0,w,h)
    c.setDash(2,2);c.rect(3*mm,3*mm,w-6*mm,h-6*mm);c.setDash()
    c.setFont('Bold',10);c.drawCentredString(w/2,h-12*mm,label)
    c.setFont('Body',8);c.drawCentredString(w/2,h-18*mm,f'{w/mm:g} × {h/mm:g} mm')
    c.setFont('Bold',8);c.drawCentredString(w/2,h-25*mm,'ÜST')
    arrow=c.beginPath();arrow.moveTo(w/2-2*mm,h-31*mm);arrow.lineTo(w/2+2*mm,h-31*mm);arrow.lineTo(w/2,h-27*mm);arrow.close();c.drawPath(arrow,fill=1,stroke=0)
    for t,xx,yy in [('A',6,7),('B',w/mm-9,7),('C',6,h/mm-7),('D',w/mm-9,h/mm-7)]:c.drawString(xx*mm,yy*mm,t)
    c.restoreState()

def cross(c,x,y,label):
    c.setStrokeColor(INK);c.setLineWidth(.35);c.line(x-3*mm,y,x+3*mm,y);c.line(x,y-3*mm,x,y+3*mm)
    c.setFont('Body',6);c.drawString(x+4*mm,y+mm,label)

def trial(c,back=False):
    side='ARKA'if back else'ÖN';c.setFillColor(INK);c.setFont('Bold',12);c.drawCentredString(105*mm,280*mm,'HİZALAMA DENEMESİ / '+side)
    for x,y,label in [(15,276,'1'),(195,276,'2'),(15,18,'3'),(195,18,'4')]:cross(c,(210-x if back else x)*mm,y*mm,label)
    for label,x,y,w,h,a in [('UZUN',20,147,70,120,0),('GÜÇ / SADAKAT',105,186.5,63.5,88.9,90),('HARİTA',115,83,70,70,0)]:
        pw=h if a else w
        xx=210-x-pw if back else x;angle=(-a)%360 if back else a
        trial_card(c,label+' '+side,xx*mm,y*mm,w*mm,h*mm,angle)
    # Physical length rulers; both are 100 mm and deliberately independent of cards.
    rx=180 if back else 30;hx=70 if back else 40
    c.setLineWidth(.5);c.line(hx*mm,45*mm,(hx+100)*mm,45*mm);c.line(rx*mm,35*mm,rx*mm,135*mm)
    for k in range(101):
        tick=(3 if k%10==0 else 1.5)*mm
        c.line((hx+k)*mm,45*mm,(hx+k)*mm,45*mm+tick)
        c.line(rx*mm,(35+k)*mm,rx*mm+(-tick if back else tick),(35+k)*mm)
    c.setFont('Body',8);c.drawCentredString((hx+50)*mm,39*mm,'100 mm');c.saveState();c.translate((185 if back else 25)*mm,85*mm);c.rotate(90);c.drawCentredString(0,0,'100 mm');c.restoreState()
    text(c,'Bu yaprağı uzun kenardan çevirin. Işığa tuttuğunuzda eşleşen dış dikdörtgenler ve numaralı artılar üst üste gelmeli. Harfler, kartı kestikten sonra yönünü kontrol etmek içindir.',(103 if back else 42)*mm,124*mm,65*mm,8.5)
    text(c,'Yatay kayma: ____ mm     Dikey kayma: ____ mm',45*mm,30*mm,137*mm,8.5)

def build():
    raw=TMP/'guide_native.pdf';c=canvas.Canvas(str(raw),pagesize=A4,invariant=1,pageCompression=1)
    heading(c,1,'Önce bir yaprak deneyin');y=253*mm
    y=p(c,'**1. Bu rehberin yalnız 3-4. sayfalarını tek yaprağın iki yüzüne basın.** Önce normal kâğıtla besleme yönünü, sonra kullanacağınız kartonla hizayı kontrol edin.',y)
    y=p(c,'**2. Yazıcı ayarı:** A4 (210 × 297 mm), dikey, gerçek boyut / %100, uzun kenardan çift taraflı baskı. Her PDF sayfası kâğıdın bir yüzüne basılmalı.',y)
    y=p(c,'“Sayfaya sığdır”, küçült/büyüt, kenarlıksız büyütme, kitapçık, çoklu sayfa ve ayna görüntüsü kapalı olsun. Arka yerleşim dosyada hazırdır; ayrıca aynalamayın. [1-2]',y)
    y=p(c,'**3. Cetvelle ölçün:** İki kontrol çizgisi de 100 mm olmalı. Dikdörtgenleri ışığa tutun; dört köşeyi karşılaştırın. Eşleşme iyiyse bir deneme kartı kesin ve iki yüzdeki ÜST yönünü kontrol edin.',y)
    y=p(c,'**4. Desteyi basın:** Kart PDF’si 46 sayfa / 23 yapraktır. 1-2 ilk ön/arka çift, 3-4 ikinci çifttir; 45-46 son çifttir. Boş kalan yuvaları kart saymayın.',y)
    y=p(c,'Güç, Erzak ve Sadakat kartları A4 üzerinde yatay durur. Kesilince doğru ölçüde dikey kart olur; ön/arka yönleri buna göre hazırlanmıştır.',y)
    data=[[para(a,9.4,'Bold'if i==0 else'Body')for a in row]for i,row in enumerate([['Kart grubu','Kesilmiş ölçü','Adet'],['Karakter + iki Liman + Kaptan','70 × 120 mm','23'],['Güç + Erzak + Sadakat','63,5 × 88,9 mm','46'],['Harita','70 × 70 mm','52']])]
    table=Table(data,colWidths=[96*mm,51*mm,23*mm]);table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));_,h=table.wrap(170*mm,1000);table.drawOn(c,20*mm,y-h);y-=h+5*mm
    p(c,'Kesim ölçüsüne her kenardaki 3 mm taşma dahil değildir. PDF eşleşmesi doğrulanmıştır; yazıcının fiziksel kâğıt kayması deneme yaprağıyla ölçülür.',y,9.5)
    c.showPage();heading(c,2,'Baskı ve kesim sırası');y=253*mm
    y=p(c,'**Otomatik çift taraflı yazıcı:** Tüm sayfaları sırayla, uzun kenardan çevirerek basın. Her kopyayı ayrı tam takım basın; önce aynı ön sayfayı çoğaltıp arka sayfaları karıştırmayın.',y)
    y=p(c,'**Elle çift taraflı yazıcı:** Varsa sürücünün “elle, uzun kenar” seçeneğini kullanın. Kâğıdın hangi yüzü ve hangi kenarı önce alındığı yazıcıya göre değişir; besleme yönünü 3-4. sayfayla belirleyin. Sürücü yönlendirmesini izleyin. [3]',y)
    y=p(c,'Elle beslemede en güvenilir yöntem bir çifti bitirmektir: 1’i basın, aynı yaprağı deneyle bulduğunuz yönde takıp 2’yi basın; sonra 3-4 diye ilerleyin. Çıkış yığınına bakmadan bütün tek/çift sayfaları topluca ters sıralamayın.',y)
    y=p(c,'**Kayma varsa:** Ölçek %100 kalsın. Sabit yatay/dikey kaymayı yazıcının ön/arka kayıt ayarıyla düzeltin. Köşeler farklı miktarda kayıyorsa kâğıt eğri besleniyordur; kılavuzları ve kâğıdı kontrol edin. Tek deneme düzgün çıkmadan bütün desteyi basmayın.',y)
    y=p(c,'**Kâğıt ve kesim:** Yazıcınızın çift taraflı baskıda desteklediği, iki yüzü baskıya uygun mat ve opak kâğıt/karton kullanın. Ön yüz kuruduktan sonra arkayı basın. Kesimi ön yüzdeki ince dış işaretlerden yapın; çerçevenin içinden kesmeyin. Aynı gruptaki kartları eşit ölçüde kesin. [4]',y)
    y=p(c,'**Gizlilik:** Sadakatlerin tümü aynı arkalıdır; Tayfa/Hain önleri arkadan seçilmemeli. Açık Deniz/Kayalık aynı deniz arkasını paylaşır. Ada altı, Fener dört aynı arka kullanır. Gerekirse bütün ailede aynı opak kılıf kullanın.',y)
    y=p(c,'**Kural kitabı:** Ayrı PDF 30 sayfa / 15 yapraktır. A4, %100 ve uzun kenardan çift taraflı basın. Soldan dosyalama/ciltleme için iç kenar payı ayrılmıştır. Kitapçık veya iki sayfayı bir yüze küçültme seçmeyin.',y)
    y-=mm
    for i,(label,url)in enumerate(SOURCES,1):
        c.setFont('Body',7.8);c.setFillColor(NAVY);c.drawString(20*mm,y,f'[{i}] {label}');c.linkURL(url,(20*mm,y-2,190*mm,y+9),relative=0);y-=5*mm
    c.showPage();trial(c);c.showPage();trial(c,True);c.showPage();c.save()
    doc=fitz.open(raw);target=ART/'FOULWAKE_A4_BASKI_REHBERI_VE_HIZALAMA.pdf';save_pdf(doc,target)
    import shutil;shutil.copy2(target,PDF/target.name)
    dump(QA/'print_research.json',{'accessed_at':'2026-09-09','sources':[{'title':a,'url':b}for a,b in SOURCES],'choices':['A4 portrait, 100 percent, long-edge duplex','3 mm bleed, 7.35 mm minimum crop-mark page margin','Native text and retained full-resolution front art','Two-axis 100 mm scale and asymmetric duplex trial before full printing'],'physical_evidence':'NOT_PERFORMED'})
    print(target)

if __name__=='__main__':build()
