"""A4 rulebook: mirrored binding margins, embedded type and traceable copy."""
from common import *
from reportlab.platypus import BaseDocTemplate,Frame,PageTemplate,Spacer,PageBreak,CondPageBreak,KeepTogether,LongTable,TableStyle,Flowable,NextPageTemplate
from reportlab.platypus.tableofcontents import TableOfContents

class Horizon(Flowable):
    def __init__(self):super().__init__();self.width=170*mm;self.height=57*mm
    def draw(self):
        c=self.canv;x=53*mm;sz=13*mm
        for row in range(3):
            for col in range(5):
                xx=x+col*sz;yy=(2-row)*sz+4*mm
                active=(row<2 and col in (1,2,3))or(row==2 and col==2)
                c.setFillColor(PALE if active else colors.white);c.setStrokeColor(colors.HexColor('#B0B4B3'));c.setLineWidth(.4);c.rect(xx,yy,sz-1*mm,sz-1*mm,fill=1,stroke=1)
                if row==2 and col==2:
                    c.setFillColor(NAVY);p=c.beginPath();p.moveTo(xx+3*mm,yy+3*mm);p.lineTo(xx+9*mm,yy+3*mm);p.lineTo(xx+6*mm,yy+9*mm);p.close();c.drawPath(p,fill=1,stroke=0)
        for label,yy in [('UZAK UFUK',34),('YAKIN UFUK',21),('GEMİ',8)]:text(c,label,0,(yy+3)*mm,48*mm,8.5,'Bold')
        text(c,'Gemi ortadayken üç sütun. Sınır, açık Geçilmez ve yasal yol koşulları ayrıca uygulanır.',0,54*mm,170*mm,9.3)

class BookDoc(BaseDocTemplate):
    def __init__(self,path):
        super().__init__(str(path),pagesize=A4,title='FOULWAKE - Kuru Pay - A4 Kural Kitabı',author='FOULWAKE / CHIEF_EDITOR',leftMargin=22*mm,rightMargin=18*mm,topMargin=23*mm,bottomMargin=23*mm)
        self.chapter_entries=[]
        templates=[]
        for name,x,other in [('odd',22,'even'),('even',18,'odd')]:
            f=Frame(x*mm,23*mm,170*mm,251*mm,id=name,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
            templates.append(PageTemplate(id=name,frames=[f],onPage=page_frame))
        self.addPageTemplates(templates)
    def handle_pageBegin(self):
        # Choose from the actual physical page parity. ReportLab's automatic
        # template index can persist for a second page after a natural break.
        self.pageTemplate=self.pageTemplates[self.page%2]
        super().handle_pageBegin()
    def afterFlowable(self,f):
        if hasattr(f,'toc_title'):
            key='s'+str(f.toc_number);self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.toc_title,key,0,False)
            self.notify('TOCEntry',(0,f.toc_title,self.page,key));self.chapter_entries.append({'title':f.toc_title,'page':self.page})

def page_frame(c,doc):
    if doc.page==1:
        c.setFillColor(NAVY);c.setFont('Title',38);c.drawCentredString(A4[0]/2,253*mm,'FOULWAKE')
        c.setFont('Title',20);c.drawCentredString(A4[0]/2,235*mm,'Kuru Pay')
        c.setFont('Body',11);c.drawCentredString(A4[0]/2,219*mm,'KURAL KİTABI')
        c.setStrokeColor(NAVY);c.setLineWidth(.6);c.line(42*mm,208*mm,168*mm,208*mm)
        text(c,'6-15 oyuncu ve 1 tarafsız Moderatör',30*mm,84*mm,150*mm,12,'Bold',alignment=1)
        text(c,'Gizli sadakat · Ortak gemi · Birlikte seçilen rota',27*mm,72*mm,156*mm,10.5,alignment=1)
        text(c,'v2.7 · 9 Eylül 2026',30*mm,38*mm,150*mm,9.5,alignment=1)
        return
    x=(22 if doc.page%2 else 18)*mm
    c.setFillColor(NAVY);c.setFont('Bold',8);c.drawString(x,283*mm,'FOULWAKE / KURU PAY')
    c.setStrokeColor(colors.HexColor('#C7C9C4'));c.setLineWidth(.5);c.line(x,279*mm,x+170*mm,279*mm)
    c.setFillColor(INK);c.setFont('Body',7.7)
    if doc.page%2:
        c.drawString(x,13*mm,'v2.7 · 09.09.2026');c.drawRightString(x+170*mm,13*mm,str(doc.page))
    else:
        c.drawString(x,13*mm,str(doc.page));c.drawRightString(x+170*mm,13*mm,'v2.7 · 09.09.2026')

def build():
    d=BookDoc(TMP/'book_native.pdf');flows=[Spacer(1,240*mm),PageBreak(),para('Kitabı kullanırken',21,'Title',after=13)]
    flows.append(para('Önce §2 ile haritayı hazırlayın; masada §3 ile başlayın. Sefer sırasında §4 açık kalsın. §13-16 başvuru tablolarıdır; §17 isteğe bağlı hikâyedir.',10.8,after=12))
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Body',fontSize=9.8,leading=15.1,textColor=INK,spaceBefore=3)]
    flows += [toc,Spacer(1,12),para('OKU bloklarını seslendirin; YAP adımlarını uygulayın. Tat metni, yeni bir kural veya gizli ipucu değildir.',10.2,after=9),PageBreak()]
    lines=(P/'FOULWAKE_KURAL_KITABI_v2.7.md').read_text().splitlines();i=0;section=0;units=[]
    while i<len(lines):
        line=lines[i].strip()
        if not line or line=='---'or line.startswith('# '):i+=1;continue
        if line.startswith('## '):
            section+=1;title=line[3:]
            flows.append(PageBreak()if title.startswith(('3. ','4. ','13. ','17. ','Masada'))else CondPageBreak(48*mm))
            h=para(title,18,'Title',after=11,keepWithNext=True);h.toc_title=title;h.toc_number=section;flows.append(h);units.append(title);i+=1;continue
        if line.startswith('### '):
            if not hasattr(flows[-1],'toc_title'):flows.append(CondPageBreak(40*mm))
            flows.append(para(line[4:],12.6,'Bold',after=8,spaceBefore=8,keepWithNext=True));units.append(line[4:])
            if line.startswith('### 6.2'):flows.append(Horizon())
            i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines)and lines[i].strip().startswith('|'):
                cells=[s.strip()for s in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+',x)for x in cells):rows.append(cells);units.extend(cells)
                i+=1
            n=len(rows[0]);weights={2:[.37,.63],3:[.28,.20,.52],4:[.25,.23,.28,.24],5:[.17,.18,.235,.18,.235]}.get(n,[1/n]*n)
            if section==1:weights=[.18,.34,.48]
            if section==13:weights=[.31,.08,.61]
            if section in (14,15):weights=[.29,.20,.51]
            data=[[para(t,9.4,'Bold'if j==0 else'Body',leading=12.7)for t in row]for j,row in enumerate(rows)]
            table=LongTable(data,colWidths=[v*170*mm for v in weights],repeatRows=1,hAlign='LEFT',splitByRow=1)
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DCE3E3')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F4EE')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5.5),('BOTTOMPADDING',(0,0),(-1,-1),5.5),('LINEBELOW',(0,0),(-1,0),.5,NAVY)]))
            flows += [table,Spacer(1,9)];continue
        if line.startswith('- ')or re.match(r'^\d+\. ',line):
            s='• '+line[2:]if line.startswith('- ')else line
            flows.append(para(s,10.6,after=6,leftIndent=8,firstLineIndent=-8));units.append(s);i+=1;continue
        buf=[line];i+=1
        while i<len(lines)and lines[i].strip()and not lines[i].startswith(('#','|','- '))and not re.match(r'^\d+\. ',lines[i]):buf.append(lines[i].strip());i+=1
        s=' '.join(buf);units.append(s)
        if s in ('**OKU**','**YAP**')or s.startswith('**OKU -'):
            flows.append(para(s,9.3,'Bold',color=RUST,after=6,keepWithNext=True,spaceBefore=7))
        else:flows.append(para(s,10.7,leading=15,after=9,allowWidows=0,allowOrphans=0))
    d.multiBuild(flows)
    result=fitz.open(TMP/'book_native.pdf');back=fitz.open(BACK_ROOT/'BACK_LIGHTHOUSE.pdf')
    result[0].show_pdf_page(fitz.Rect(65*mm,104*mm,145*mm,184*mm),back,0,clip=back[0].rect+(3*mm,3*mm,-3*mm,-3*mm))
    if len(result)%2:
        p=result.new_page(width=A4[0],height=A4[1]);p.insert_text((22*mm,25*mm),'',fontsize=10)
        # Keep the final reverse intentional and useful without introducing rules.
        bg=TMP/'notes.pdf';from reportlab.pdfgen import canvas
        c=canvas.Canvas(str(bg),pagesize=A4,invariant=1);c.setFillColor(INK);c.setFont('Title',18);c.drawString(18*mm,268*mm,'Sefer notları')
        c.setStrokeColor(colors.HexColor('#D5D5CD'));c.setLineWidth(.35)
        for y in range(44,250,12):c.line(18*mm,y*mm,188*mm,y*mm)
        c.showPage();c.save();nd=fitz.open(bg);p.show_pdf_page(p.rect,nd,0)
    target=ART/'FOULWAKE_KURAL_KITABI_A4_v2.7.pdf';pages=len(result);save_pdf(result,target)
    import shutil;shutil.copy2(target,PDF/target.name)
    dump(QA/'rulebook_manifest.json',{'source_path':str((P/'FOULWAKE_KURAL_KITABI_v2.7.md').relative_to(R)),'source_sha256':sha(P/'FOULWAKE_KURAL_KITABI_v2.7.md'),'pages':pages,'sha256':sha(target),'units':units,'chapters':d.chapter_entries[-18:],'body_pt':10.7,'table_pt':9.4,'inner_margin_mm':22,'outer_margin_mm':18,'status':'AWAITING_RENDER_AND_COPY_CHECK'})
    print(target,pages)

if __name__=='__main__':build()
