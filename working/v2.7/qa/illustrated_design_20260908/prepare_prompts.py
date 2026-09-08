"""Measured full-card design prompts, one original asset for each identity."""
import json,hashlib
from card_layout import records,measure,QA,OUT,P
from scenes import SCENES

STYLE='''FOULWAKE, an original 1721 seafaring board game about doubt, medicine cargo, damp bureaucracy and shared debt. Use the supplied captain card ONLY as a visual-language reference, not as a picture to paste, crop or trace. Create a genuinely different original scene for this card. Bold lively black comic-engraving outlines, exaggerated human expressions and silhouettes, deliberate hand crosshatching, aged warm tan parchment, faded navy blue, restrained ochre and small rusty red accents. Humorous human behavior in a serious physical world. One cohesive vintage printed illustrated card, NOT a realistic oil painting, not photorealism, not glossy fantasy, not 3D, not a photo in a frame. No modern objects. All figures are original, diverse adult faces and builds. Never copy the captain face or place the same man on every card. No secret faction symbols, no invented guilty clues, no gore. The four literary/media allusions, if relevant, stay quiet and indirect. Exact Turkish words will be added natively later: do not generate letters, numbers, glyphs, pseudo-writing, titles, watermarks or logos anywhere.'''

def prompt(r):
    g=measure(r);w,h=g['trim_mm'];square=r['collection']=='maps'
    # Give generation a little more blank space than the mathematical minimum.
    bottom=min(62,g['copy_panel_percent']+5)
    if r['collection'] in ('powers','provisions','loyalties'):bottom=min(68,g['copy_panel_percent']+12)
    if r['id'].startswith('SAD-H-'):bottom=max(bottom,66)
    if r['collection']=='characters':bottom=max(29,g['copy_panel_percent']+5)
    title=18 if square else 16 if h<100 else 14
    y_end=100-bottom
    ratio='square 1:1' if square else 'portrait 5:7' if h<100 else 'portrait 7:12'
    return f'''Create ONE full card background plate, {ratio}, entire card visible, straight-on flat print, no mockup, no extra cards or contact sheet. Output a single original asset.
{STYLE}
INTEGRATED DESIGN AND REQUIRED GEOMETRY: a worn irregular double ink frame about 4% inside all edges, subtle corner pen flourishes, the same salt-stained tan paper across the WHOLE card. A broad curling EMPTY title ribbon occupies the top {title}% of the card; its broad central part x=14%-86% must be blank and bright for later lettering. Do not draw a title.
CRITICAL: The BOTTOM {bottom}% of the entire card must be a large EMPTY quiet parchment text cartouche. Its top divider is at y={y_end}% measured from the TOP, not at the usual reference card position. This blank lower panel is intentionally {'more than half' if bottom>50 else 'about half' if bottom>=45 else 'a substantial part'} of the card. No objects, hands, faces, scenery, letters or ornament in x=9%-91% of this lower panel. Small engraving only in its far side margins. The art must stop above y={y_end-2}%. Respect the unusually large empty text area: DO NOT copy the reference proportions.
The illustration lives between y={title+2}% and y={y_end-2}%. It is drawn directly on the same paper and touches the side framing naturally. No inset rectangular photograph, no white margin or separate white picture box. Compose large expressive faces, objects and clear silhouettes for this {'wide shallow' if square or bottom>=45 else 'portrait'} illustration band; simplify distant scenery. Keep every important face, hand and object within the band. Leave generous native-copy room while making this a richly integrated comic card.
INDIVIDUAL SCENE for {r['id']} (identity only, DO NOT WRITE it): {SCENES[r['id']]}
Finish as a carefully engraved, lightly colored, memorable original board-game card. Both EMPTY title ribbon and EMPTY bottom copy panel must remain legible and unoccupied. No text. One image.'''

def main():
    assert len(records)==121 and set(SCENES)=={r['id'] for r in records}
    (QA/'prompts').mkdir(exist_ok=True)
    briefs=[]
    for r in records:
        p=prompt(r);(QA/'prompts'/f"{r['id']}.txt").write_text(p+'\n')
        briefs.append({'id':r['id'],'name':r.get('name',r.get('title')),'scene':SCENES[r['id']],'geometry':measure(r),'prompt_sha256':hashlib.sha256((p+'\n').encode()).hexdigest(),'status':'PLANNED_ORIGINAL_FULL_CARD_PLATE','reference_role':'STYLE_ONLY','copy_source_unchanged':True})
    (QA/'scene_manifest.json').write_text(json.dumps({'task_id':'FOULWAKE-ILLUSTRATED-DESIGN-002','cards':briefs},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'individual_scene_briefs':len(briefs),'copy_measured':121}))

if __name__=='__main__':main()
