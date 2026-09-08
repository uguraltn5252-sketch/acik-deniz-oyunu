"""Current rulebook layout; paragraphs stay together, overview table breathes.
Derived from the retained 20260907 print layout without modifying its source.
"""
import re
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Spacer, PageBreak, CondPageBreak, KeepTogether, LongTable, TableStyle
from reportlab.platypus.tableofcontents import TableOfContents

def build_book(layout):
    PDF=layout.PDF;P=layout.P;BookDoc=layout.BookDoc;para=layout.para
    INK=layout.INK;PAPER=layout.PAPER;RUST=layout.RUST;WHITE=layout.WHITE
    clean=layout.clean;Horizon=layout.Horizon;book_page=layout.book_page
    path=PDF/'FOULWAKE_KURAL_KITABI_v2.7.pdf'
    doc=BookDoc(str(path),pagesize=A4,leftMargin=21*mm,rightMargin=21*mm,topMargin=24*mm,bottomMargin=21*mm,title='FOULWAKE - Kuru Pay - Kural Kitabı',author='FOULWAKE / CHIEF_EDITOR')
    flow=[Spacer(1,230*mm),PageBreak(),para('Kitabı kullanırken',22,'Title',after=14)]
    flow.append(para('İlk oyunda önce hazırlık ve kurulum. Oyun sırasında günlük akış açık kalsın; nadir etkileşimlere gerektiğinde bakın. Arka planı baştan sona sesli okumak gerekmiyor.',11,after=14))
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='Body',fontSize=10.2,leading=16,textColor=INK,spaceBefore=3)]
    flow.extend([toc,PageBreak()])
    lines=(P/'FOULWAKE_KURAL_KITABI_v2.7.md').read_text().splitlines();i=0;section=0
    while i<len(lines):
        line=lines[i].strip()
        if not line or line=='---' or line.startswith('# '):i+=1;continue
        if line.startswith('## '):
            section+=1;title=line[3:]
            flow.append(PageBreak()if title.startswith(('3. ','4. ','13. ','17. ','Masada')) else CondPageBreak(50*mm))
            h=para(title,18,'Title',after=12,keepWithNext=True);h.toc_title=clean(title);h.toc_number=section;flow.append(h);i+=1;continue
        if line.startswith('### '):
            if not hasattr(flow[-1],'toc_title'):flow.append(CondPageBreak(42*mm))
            flow.append(para(line[4:],13,'Strong',after=8,spaceBefore=8,keepWithNext=True))
            if line.startswith('### 6.2'):flow.append(Horizon())
            i+=1;continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines)and lines[i].strip().startswith('|'):
                cells=[s.strip()for s in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+',c)for c in cells):rows.append(cells)
                i+=1
            n=len(rows[0]);width=168*mm
            weights={2:[.37,.63],3:[.28,.20,.52],4:[.24,.23,.29,.24],5:[.21,.18,.20,.20,.21],6:[.12,.17,.18,.17,.18,.18]}.get(n,[1/n]*n)
            if section==13 and n==3:weights=[.31,.08,.61]
            if section in (14,15)and n==3:weights=[.29,.22,.49]
            data=[[para(t,9.2,'Strong'if r==0 else'Body',12.3,PAPER if r==0 else INK)for t in row]for r,row in enumerate(rows)]
            table=LongTable(data,colWidths=[v*width for v in weights],repeatRows=1,hAlign='LEFT')
            pad=5 if section==1 else 6 if section==16 else 7
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,colors.HexColor('#EDE7D9')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),pad),('BOTTOMPADDING',(0,0),(-1,-1),pad),('LINEBELOW',(0,0),(-1,0),.5,INK)]))
            flow.extend([table,Spacer(1,9)]);continue
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            content=line[2:]if line.startswith('- ')else line
            if line.startswith('- '):content='• '+content
            flow.append(para(content,10.7,after=6,leftIndent=8,firstLineIndent=-8));i+=1;continue
        buf=[line];i+=1
        while i<len(lines)and lines[i].strip()and not lines[i].startswith(('#','|','- ')):
            buf.append(lines[i].strip());i+=1
        text=' '.join(buf)
        if text in ('**OKU**','**YAP**')or text.startswith('**OKU -'):
            flow.append(para(text,9,'Strong',color=RUST,after=6,keepWithNext=True,spaceBefore=7))
        else:flow.append(KeepTogether([para(text,10.8,leading=15.2,after=9)]))
    doc.multiBuild(flow,onFirstPage=book_page,onLaterPages=book_page)
    return path
