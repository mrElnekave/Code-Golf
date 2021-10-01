

def finalQuizScore(h,l,r,o,t,p):s=-((3*h+2*l+o+.5*p+1.5*r+t-900)//1);return f"{'Sorry, y' if s>100 else 'Y'}ou would need a {s}% on the final quiz to get an A-."
def finalQuizScore(h,l,r,o,t,p):s=-((3*h+2*l+o+.5*p+1.5*r+t-900)//1);return"%sou would need a %s%% on the final quiz to get an A-."%(("Sorry, y","Y")[s<100],s)
def finalQuizScore(h,l,r,o,t,p):s=-((3*h+2*l+o+.5*p+1.5*r+t-900)//1);return f"{('Sorry, y','Y')[s<100]}ou would need a {s}% on the final quiz to get an A-."
def finalQuizScore(h,l,r,o,t,p):s=900-int(3*h+2*l+o+.5*p+1.5*r+t);return('Sorry, y','Y')[s<100]+f"ou would need a {s}% on the final quiz to get an A-."
def finalQuizScore(h,l,r,o,t,p):s=900-int(.5*(p+3*r+6*h+4*l))-t-o;return('Sorry, y','Y')[s<100]+f'ou would need a {s}% on the final quiz to get an A-.'
l=[3,2,1.5,1,1,.5]
def finalQuizScore(*a):s=900-int(sum(x*y for x,y in zip(l,a)));return('Sorry, y','Y')[s<100]+f'ou would need a {s}% on the final quiz to get an A-.'
# finalQuizScore=lambda h,l,r,o,t,p: (f"{('Sorry, y','Y')[-((3*h+2*l+o+.5*p+1.5*r+t-900)//1)<100]}ou would need a {s}% on the final quiz to get an A-."
# finalQuizScore=lambda h,l,r,o,t,p:('Y','Sorry, y')[(s:=900-int((p+3*r+6*h+4*l)/2)-t-o)>100]+f'ou would need a {s}% on the final quiz to get an A-.'

"""
required
def finalQuizScore(h,l,r,o,t,p):
(-3*h-2*l-o-.5*p-1.5*r-t+900)
return "ou would need a % on the final quiz to get an A-."
'Sorry, y'
"Y"
"""

print(finalQuizScore(90, 90, 90, 90, 90, 90))
print(finalQuizScore(90, 90, 90, 85, 85, 90))
print(finalQuizScore(0, 0, 0, 0, 0, 0))
print(finalQuizScore(100, 100, 100, 100, 100, 100))
print(finalQuizScore(12, 34, 56, 78, 90, 11))
