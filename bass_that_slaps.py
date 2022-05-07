Scale.default.set(Scale.minorPentatonic)

Root.default.set(-6)

jj >> play("x",amp=PEuclid(3,8))

kl >> play("O",amp=PEuclid(4,15)*0.4,sample=2)

ll >> play("<:><->")

jo >> dbass(P[[1,2,4,6],P[1,2,1,2]]*PEuclid(1,3),dur=PDur(2,5))
