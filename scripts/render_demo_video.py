from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path('demo_video_assets')
OUT.mkdir(exist_ok=True)
W, H = 1920, 1080
BG = '#08141b'; PANEL = '#10252d'; BORDER = '#2b4a51'; MINT = '#8de3c6'; MUTED = '#94a9ad'; WHITE = '#edf3f5'

def font(size, bold=False):
    path = 'C:/Windows/Fonts/segoeuib.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf'
    return ImageFont.truetype(path, size)

def text(draw, xy, value, size=30, fill=WHITE, bold=False, anchor=None):
    draw.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)

def base(kicker, title, subtitle):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    d.ellipse((1450, -350, 2100, 300), fill='#12333b')
    d.ellipse((-300, 850, 500, 1400), fill='#0d2830')
    text(d, (120, 90), 'P', 34, BG, True); d.rounded_rectangle((110, 80, 170, 140), 16, fill=MINT)
    text(d, (195, 92), 'PAYPILOT AI', 28, WHITE, True)
    text(d, (120, 235), kicker.upper(), 18, MINT, True)
    text(d, (120, 285), title, 58, WHITE, True)
    text(d, (120, 370), subtitle, 25, MUTED)
    return im, d

def card(d, box, title, value, note=''):
    d.rounded_rectangle(box, 18, fill=PANEL, outline=BORDER, width=2)
    x, y, _, _ = box; text(d, (x+28, y+24), title, 18, MUTED, True); text(d, (x+28, y+65), value, 35, WHITE, True)
    if note: text(d, (x+28, y+120), note, 17, MINT)

slides=[]
im,d=base('Controlled commerce','Procurement, on autopilot.','PayPilot turns a plain-English brief into a verified purchase plan — while humans keep financial control.')
card(d,(120,540,620,790),'VERIFIED SPEND','$0.00','No fabricated payment metrics')
card(d,(660,540,1160,790),'PENDING REQUESTS','1','Needs human review')
card(d,(1200,540,1700,790),'COMPLETED ORDERS','0','Capture verification required')
slides.append(im)

im,d=base('01 · Natural language','Tell the agent what your team needs.','No forms. No hidden automation. State the outcome, quantities, budget, and preferences.')
d.rounded_rectangle((120,520,1800,820),18,fill='#071219',outline=BORDER,width=2)
text(d,(165,575),'I need two monitors and one office chair.',26,WHITE)
text(d,(165,630),'My total budget is $600. Prioritize quality and value.',26,WHITE)
d.rounded_rectangle((165,710,560,775),12,fill=MINT); text(d,(360,742),'BUILD PURCHASE PLAN  →',18,BG,True,anchor='mm')
slides.append(im)

im,d=base('02 · AI recommendation','A reviewable plan, not a black box.','The server matches the request to a seeded catalogue and re-checks every price.')
card(d,(120,520,850,760),'RECOMMENDED ITEMS','2× Acer Vero 24” Monitor','$298.00')
card(d,(900,520,1630,760),'RECOMMENDED ITEMS','1× Branch Ergonomic Chair','$299.00')
d.rounded_rectangle((120,820,1630,930),16,fill='#173b38',outline='#397469',width=2)
text(d,(165,875),'TOTAL   $597.00     ·     WITHIN BUDGET     ·     $3.00 REMAINING',24,MINT,True,anchor='lm')
slides.append(im)

im,d=base('03 · Human approval','You approve every payment.','AI recommends. PayPilot never authorizes or captures a payment on its own.')
d.rounded_rectangle((120,505,1080,860),18,fill=PANEL,outline=BORDER,width=2)
text(d,(170,565),'READY TO AUTHORIZE?',22,MINT,True); text(d,(170,625),'PayPal Sandbox checkout',36,WHITE,True)
text(d,(170,705),'The order is created server-side only after review.',21,MUTED); text(d,(170,755),'The final capture is verified server-side.',21,MUTED)
d.rounded_rectangle((1180,590,1690,740),14,fill='#ffc439'); text(d,(1435,665),'PayPal',36,'#10202b',True,anchor='mm')
slides.append(im)

im,d=base('04 · Verified payment','A clean audit trail.','Only a completed PayPal capture becomes a transaction in PayPilot history.')
headers=['SUMMARY','AMOUNT','STATUS','CAPTURE REFERENCE']
xs=[120,790,1080,1320]
for x,h in zip(xs,headers): text(d,(x,510),h,16,MUTED,True)
d.line((120,555,1740,555),fill=BORDER,width=2)
text(d,(120,605),'Approved procurement purchase',22,WHITE); text(d,(790,605),'$597.00 USD',22,WHITE); text(d,(1080,605),'COMPLETED',20,MINT,True); text(d,(1320,605),'CAPTURE-VERIFIED',20,MINT)
d.rounded_rectangle((120,735,1740,850),16,fill=PANEL,outline=BORDER,width=2)
text(d,(165,790),'Server-verified · stored for reconciliation · ready for an accountable team',22,MUTED,anchor='lm')
slides.append(im)

im,d=base('05 · The value','Faster purchasing. Accountable spend.','PayPilot AI is controlled agentic commerce: recommendations from AI, authorization by humans, payment through PayPal.')
for i,(head,body) in enumerate([('GROUNDING','Catalogue prices are the source of truth.'),('GUARDRAILS','Budgets, quantities, and availability are enforced.'),('CONTROL','Every payment requires an explicit approval.')]):
    y=510+i*125; d.ellipse((140,y,190,y+50),fill=MINT); text(d,(165,y+25),str(i+1),22,BG,True,anchor='mm'); text(d,(230,y),head,20,MINT,True); text(d,(230,y+37),body,24,WHITE)
slides.append(im)

concat=[]
for i,im in enumerate(slides,1):
    path=OUT/f'slide-{i:02d}.png'; im.save(path); concat.append(f"file '{path.resolve().as_posix()}'\nduration 20")
concat.append(f"file '{(OUT/'slide-05.png').resolve().as_posix()}'\nduration 1")
(OUT/'concat.txt').write_text('\n'.join(concat),encoding='utf-8')
print(f'Wrote {len(slides)} slides to {OUT.resolve()}')
