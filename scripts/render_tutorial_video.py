from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT=Path('tutorial_video_assets'); OUT.mkdir(exist_ok=True)
W,H=1920,1080; BG='#08141b'; SIDE='#0a1921'; PANEL='#0e2028'; BORDER='#263f47'; MINT='#8de3c6'; WHITE='#edf3f5'; MUTED='#8fa5aa'; RED='#ffb4a9'
def f(n,b=False): return ImageFont.truetype('C:/Windows/Fonts/segoeui'+('b' if b else '')+'.ttf',n)
def t(d,x,y,s,n,c=WHITE,b=False): d.text((x,y),n,font=f(s,b),fill=c)
def ui(step,title,sub):
 im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); d.rectangle((0,0,285,H),fill=SIDE); d.rectangle((285,0,W,H),fill=BG)
 d.rounded_rectangle((32,35,82,85),12,fill=MINT); t(d,48,43,28,'P',BG,True); t(d,96,45,20,'PAYPILOT AI',WHITE,True)
 for i,n in enumerate(['Overview','AI Assistant','Transactions','Catalogue']):
  y=170+i*62; active=(i==step%4); d.rounded_rectangle((25,y,260,y+44),9,fill='#142a32' if active else SIDE); t(d,51,y+10,15,n,MINT if active else MUTED,True)
 t(d,335,70,13,f'TEST {step+1} OF 7',MINT,True); t(d,335,110,38,title,WHITE,True); t(d,335,170,18,sub,MUTED)
 return im,d
def card(d,x,y,w,h,label,value,note='',color=WHITE):
 d.rounded_rectangle((x,y,x+w,y+h),14,fill=PANEL,outline=BORDER,width=2); t(d,x+22,y+18,12,label,MUTED,True); t(d,x+22,y+55,29,value,color,True)
 if note:t(d,x+22,y+h-35,13,note,MINT)
def footer(d,msg,ok=True):
 d.rounded_rectangle((335,940,1810,1000),12,fill='#173b38' if ok else '#3b2528',outline='#397469' if ok else '#74413e',width=1); t(d,365,958,16,('PASS  ' if ok else 'BLOCKED  ')+msg,MINT if ok else RED,True)
slides=[]
im,d=ui(0,'Dashboard health check','Test: application loads with verified, non-fabricated metrics.');
card(d,335,300,390,170,'VERIFIED SPEND','$0.00','No verified captures yet'); card(d,755,300,390,170,'PENDING REQUESTS','1','Needs your review'); card(d,1175,300,390,170,'COMPLETED ORDERS','0','Verified only');
d.rounded_rectangle((335,520,1565,790),14,fill=PANEL,outline=BORDER,width=2); t(d,370,555,20,'Recent activity',WHITE,True); t(d,370,630,18,'Your verified activity will appear here.',MUTED); footer(d,'Dashboard loads; seeded examples are clearly not presented as real payments.'); slides.append(im)
im,d=ui(1,'Natural-language request','Test: user submits a realistic procurement brief.');
d.rounded_rectangle((335,310,1565,650),14,fill='#071219',outline=BORDER,width=2); t(d,375,355,15,'AI PURCHASING AGENT',MINT,True); t(d,375,430,25,'I need two monitors and one office chair.',WHITE); t(d,375,480,25,'My total budget is $600. Prioritize quality and value.',WHITE); d.rounded_rectangle((375,555,740,615),10,fill=MINT); t(d,410,572,16,'BUILD PURCHASE PLAN  →',BG,True); footer(d,'Request accepted and sent to the server API.'); slides.append(im)
im,d=ui(2,'Catalogue-grounded AI plan','Test: quantities, product IDs, and prices are matched server-side.');
card(d,335,300,590,150,'RECOMMENDED ITEM','2× Acer Vero 24” Monitor','$298.00'); card(d,955,300,590,150,'RECOMMENDED ITEM','1× Branch Ergonomic Chair','$299.00');
d.rounded_rectangle((335,520,1545,670),14,fill='#173b38',outline='#397469',width=2); t(d,370,570,20,'TOTAL',MUTED,True); t(d,510,557,33,'$597.00',WHITE,True); t(d,850,570,20,'WITHIN BUDGET  ·  $3.00 REMAINING',MINT,True); footer(d,'AI output is grounded in the seeded catalogue and recalculated on the server.'); slides.append(im)
im,d=ui(3,'Budget guardrail test','Test: a purchase above the budget cannot continue.');
d.rounded_rectangle((335,300,1545,430),14,fill=PANEL,outline=BORDER,width=2); t(d,370,340,20,'Example negative test',MINT,True); t(d,370,380,20,'Change quantity to 3 monitors → total becomes $746.00',WHITE); d.rounded_rectangle((335,490,1545,650),14,fill='#3b2528',outline='#74413e',width=2); t(d,375,530,24,'OVER BUDGET',RED,True); t(d,375,580,20,'Payment button remains disabled.',WHITE); t(d,375,615,16,'No order is sent to PayPal.',MUTED); footer(d,'Budget exceeded is rejected before payment.',False); slides.append(im)
im,d=ui(4,'PayPal Sandbox approval','Test: only an explicit human approval creates the PayPal order.');
d.rounded_rectangle((335,300,1030,700),14,fill=PANEL,outline=BORDER,width=2); t(d,375,350,13,'APPROVAL REQUIRED',MINT,True); t(d,375,405,27,'Ready to authorize?',WHITE,True); t(d,375,470,18,'The server will re-check every price',MUTED); t(d,375,505,18,'before creating the order.',MUTED); d.rounded_rectangle((1120,420,1540,545),12,fill='#ffc439'); t(d,1330,456,34,'PayPal',BG,True,anchor='mm') if False else t(d,1210,460,34,'PayPal',BG,True); footer(d,'Sandbox order creation is server-side and human-approved.'); slides.append(im)
im,d=ui(5,'Capture and cancellation tests','Test: cancellation shows no success; completed capture is verified.');
d.rounded_rectangle((335,300,1545,490),14,fill=PANEL,outline=BORDER,width=2); t(d,375,345,18,'Cancel checkout',WHITE,True); t(d,375,390,17,'Expected: “No payment was captured.”',MUTED); d.rounded_rectangle((335,550,1545,740),14,fill='#173b38',outline='#397469',width=2); t(d,375,595,18,'Approve Sandbox payment',MINT,True); t(d,375,640,17,'Expected: PayPal COMPLETED + capture reference.',WHITE); footer(d,'Frontend claims never determine payment success; PayPal response does.',True); slides.append(im)
im,d=ui(6,'Transaction history and handoff','Test complete: verified activity is persisted for auditability.');
d.rounded_rectangle((335,300,1545,710),14,fill=PANEL,outline=BORDER,width=2); t(d,375,345,14,'SUMMARY',MUTED,True); t(d,820,345,14,'AMOUNT',MUTED,True); t(d,1080,345,14,'STATUS',MUTED,True); d.line((375,390,1500,390),fill=BORDER,width=2); t(d,375,440,19,'Approved procurement purchase',WHITE); t(d,820,440,19,'$597.00 USD',WHITE); t(d,1080,440,18,'COMPLETED',MINT,True); t(d,375,520,18,'PayPal order ID + capture ID stored',MUTED); t(d,375,575,18,'Secrets never reach the browser.',MINT); footer(d,'End-to-end tutorial passed: plan → guardrail → approval → verified history.'); slides.append(im)
for i,im in enumerate(slides,1): im.save(OUT/f'slide-{i:02d}.png')
concat=[]
for i in range(1,8): concat.append(f"file '{(OUT/f'slide-{i:02d}.png').resolve().as_posix()}'\nduration 20")
concat.append(f"file '{(OUT/'slide-07.png').resolve().as_posix()}'\nduration 1")
(OUT/'concat.txt').write_text('\n'.join(concat),encoding='utf-8')
print('Rendered 7 original app-testing scenes')
