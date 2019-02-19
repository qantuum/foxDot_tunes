# Find the in C tune here : http://aleatoric.backporchrevolution.com/wp-content/uploads/2009/01/inc_score.gif

# Now for the 53 different patterns, all converted in FoxDot language

# There is 53 different patterns. I have only two characters with letter first for naming players, consequently here is my enum :
'''
1 becomes p1
10 becomes q0
11 becomes q1
20 becomes r0
30 becomes s0
40 becomes t0
50 becomes u0
and so on
'''

# The score does not mention any time signature nor tempo so I'll consider we're set like this, feel free to change whatever :
Clock.bpm = 120
Clock.meter = (4,4)

# Root and scale, in the original set it's a C major but we have full possibility of experimenting something else
Root.default.set(0)
Scale.default.set("major")

# Pattern list :

# All-in-one class
class INC :
  p1.degree = 0
  p1.dur = 1
  p1.oct = (5,6)

  p2.degree = P[0,1,0] 
  p2.dur = P[1/2,1/2,1]
  p2.oct = P[(5,6),6,6]

  p3.degree = P[0,1,0]
  p3.dur = 1/2
  p3.oct = 6

  p4.degree = P[-3,0,1,2]
  p4.dur = P[rest(1/2),1/2,1/2,1/2]
  p4.oct = 6

  p5.degree = P[0,1,2,-3]
  p5.dur = P[1/2,1/2,1/2,rest(1/2)]
  p5.oct = 6

  p6.degree = 5
  p6.dur = 4 # this is a full bar, changes with Clock.meter
  p6.oct = 6

  p7.degree = P[[-3]*4,[5]*3,[-3]*5]
  p7.dur = P[[rest(1)]*3,rest(1/2),[1/4]*2,1/2,rest(1/2),[rest(1)]*4]
  p7.oct = 5

  p8.degree = P[2,0,0]
  p8.dur = P[6,4,4]
  p8.oct = 6

  p9.degree = P[4,2,[-3]*4]
  p9.dur = P[[1/4]*2,rest(1/2),[rest(1)]*4]
  p9.oct = 6

  q0.degree = P[4,2]
  q0.dur = 1/2
  q0.oct = 6

  q1.degree = 
  q1.dur = 1/4
  q1.oct = 6

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

  p1.degree = 
  p1.dur = 

