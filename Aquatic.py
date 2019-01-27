# few lines for somehow liquid, aquatic atmos

Clock.meter = (5,4)
Root.default.set(-12)
Scale.default.set('majorPentatonic')
Clock.bpm = 133

qw >> dirt(var([0,4],20),dur=1/2,formant=0.04,oct=6,delay=(0,0.4),pan=(0.25,-0.41)) + PWalk(3,step=3)

ff >> pluck(qw.degree,dur=1/4,drive=0.2,oct=4)

fg >> play('YYysS',room=1,mix=0.5,rate=1.1)

ss >> ambi(ff.degree +3,dur=2,formant=0.08, lpf=0,hpf=400) + P(0,P*(3,7),var([10,11]))

qq >> space(P[0,1,0,P*(5,3),7],room=3,mix=0.5,drive=0.05)

xx >> play('# ',dur=2.5,drive=0.1,sample=4,rate=0.4)

xd >> play('Z',rate=0.1,dur=2.5,hpf=200,lpf=500)

xs >> play('C',dur=PDur(3,20),rate=0.42145,delay=(0,2),sample=3,room=1,drive=0.04)
