# some sort of trippy arps

Root.default.set(-5)

Scale.default.set('mixolydian')

az >> play('<[xx]=><s>',rate=2,room=1,mix=0.4)

ay >> play('*',hpf=1000,lpf=2000,pan=sinvar([-1,1],24),amp=linvar([1,0],12),sample=3)

aw >> star(P[0,-2,0,3],dur=4,oct=6,vib=20,chop=16) + P(0,4)

av >> quin(aw.degree[0] + var([2,5]),dur=PDur(13,16),oct=4,drive=0.15)

au >> crunch(oct=7,room=3,mix=0.3)

ax >> blip(PTri(12) + var([-1,-2,5,-1],11),drive=linvar([0.1,0.2],11),vib=5,slide=0.1,dur=Pvar([P[1/8],PDur(7,8)],11))

at >> pasha(ax.penta(),dur=PDur(5,8),drive=0.1,vib=5)

af >> play("# ",amp=var([1,2],1),sample=9)

ah >> play(' h',drive=0.8,vib=20)

ad >> play('Z ',rate=0.1,dur=4,vib=5)

Clock.bpm = linvar([120,140],start=Clock.now())

Root.default = var([-5,-4,-3,-2,-1,0],12)
