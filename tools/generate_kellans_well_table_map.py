#!/usr/bin/env python3
"""Draw a reusable 20 x 24 square Kellan's Well pump-bay battlefield."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import random
random.seed(20261010)
S=200; W=20*S; H=24*S
try:
 font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
 small=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 43)
except OSError: font=ImageFont.load_default(); small=font
def xy(a,b,c,d): return (int(a*S),int(b*S),int(c*S),int(d*S))
def make(dm):
 random.seed(20261010)
 im=Image.new("RGB",(W,H),(190,188,170))
 d=ImageDraw.Draw(im)
 d.rectangle(xy(0,0,20,24),fill="#626d69")
 d.rectangle(xy(0.6,0.7,19.4,23.3),fill="#c6c4b2")
 # stone floor scratches
 for i in range(600):
  x=random.randint(150,W-160);y=random.randint(150,H-160)
  d.line((x,y,x+random.randint(10,65),y-random.randint(-20,20)),fill="#b4b3a3",width=2)
 # perimeter
 for xx in [0,19]:
  d.rectangle(xy(xx,0,xx+1,24),fill="#59615e",outline="#343f42",width=18)
 for yy in [0,23]:
  d.rectangle(xy(0,yy,20,yy+1),fill="#59615e",outline="#343f42",width=18)
 # gallery and parapet (10 feet above floor)
 d.rectangle(xy(3,2,17,7.1),fill="#918e7d",outline="#5c5f55",width=24)
 d.rectangle(xy(5.4,7,16.4,7.3),fill="#566166")
 for i in range(6,16):
  d.rectangle(xy(i,7.07,i+.53,7.25),fill="#cbcabb")
 # north/south doors
 for y in [0,23]:
  d.rectangle(xy(8.85,y,11.15,y+1),fill="#9c8060",outline="#383c39",width=16)
 # west stairs
 d.rectangle(xy(3.25,7,5.35,10.3),fill="#8e9186",outline="#444d4c",width=20)
 for y in [7.25,7.8,8.35,8.9,9.45]:
  d.line((int(3.25*S),int(y*S),int(5.35*S),int(y*S)),fill="#536064",width=10)
 # east ladder
 d.rectangle(xy(16.2,7.2,16.7,10.1),fill="#5c665e",outline="#343e3d",width=15)
 for y in [7.6,8.15,8.7,9.25]:
  d.line((int(16.2*S),int(y*S),int(16.7*S),int(y*S)),fill="#dcc18d",width=12)
 # channel, 60 ft long 10 ft wide
 d.rectangle(xy(8.5,8.4,10.5,20.1),fill="#347e95",outline="#485958",width=22)
 for y in range(9,20):
  d.arc(xy(8.7,y,10.35,y+.4),0,180,fill="#73b5c0",width=5)
 # catwalk right side
 d.rectangle(xy(10.55,8.6,11.55,19.9),fill="#777f78",outline="#425451",width=17)
 for y in range(9,20):
  d.line((int(10.6*S),int(y*S),int(11.5*S),int(y*S)),fill="#b5b5a2",width=5)
 # crosswalk at south side
 d.rectangle(xy(8.0,19.6,12.1,20.6),fill="#757f79",outline="#485653",width=18)
 # pump housings
 for x1,y1,x2,y2 in [(2.0,13,6.0,16.4),(13.9,15.2,18.3,18.4)]:
  d.rounded_rectangle(xy(x1,y1,x2,y2),radius=38,fill="#687b80",outline="#354348",width=30)
  d.rectangle(xy(x1+.2,y1+.2,x2-.2,y2-.2),fill="#909fa1",outline="#bea879",width=15)
  for x,y,r in [(x1+.85,y1+.85,.55),(x2-1.1,y2-.9,.55)]:
   d.ellipse(xy(x-r/2,y-r/2,x+r/2,y+r/2),fill="#334b4e",outline="#c6b47b",width=18)
 for a in [(6.45,10.5,7.3,11.65),(12.1,17.85,13.2,18.9)]:
  d.rectangle(xy(*a),fill="#6c7a7a",outline="#38494a",width=22)
 # sluice and counterweight apparatus
 d.ellipse(xy(8.9,7.65,10.5,9.2),fill="#a7956e",outline="#576166",width=25)
 d.ellipse(xy(14.4,10.8,16,12.4),fill="#a7956e",outline="#576166",width=24)
 d.rectangle(xy(14.05,10.65,16.6,12.6),outline="#3d5151",width=28)
 # coordinate grid, one square = 5 feet
 for x in range(21): d.line((x*S,0,x*S,H),fill="#81857e",width=4)
 for y in range(25): d.line((0,y*S,W,y*S),fill="#81857e",width=4)
 # grid markers
 for x in range(20):
  d.text(((x+.22)*S,.12*S),chr(65+x),font=small,fill="white")
 for y in range(24):
  d.text((.12*S,(y+.1)*S),str(y+1),font=small,fill="white")
 if dm:
  marks=[(1,15.55,4.9),(2,15.0,11.6),(3,9.7,8.55),(4,3.5,5.75),(5,14.7,3.9),(6,16.48,8.85),(7,4.25,9.1)]
  for n,x,y in marks:
   r=.45*S
   d.ellipse((int(x*S-r),int(y*S-r),int(x*S+r),int(y*S+r)),fill="#fae9bd",outline="#8b432d",width=20)
   text=str(n); bb=d.textbbox((0,0),text,font=font);tw=bb[2]-bb[0];th=bb[3]-bb[1]
   d.text((int(x*S-tw/2),int(y*S-th/2-8)),text,font=font,fill="#78351f")
 else:
  # unlabeled hidden exit exists only in command bay, not universal terrain
  pass
 return im
root=Path("img")
for side in ["player","dm"]:
 folder=root/side;folder.mkdir(parents=True,exist_ok=True)
 im=make(side=="dm")
 im.save(folder/"kellans_well_table_ready.webp","WEBP",quality=84,method=6)
