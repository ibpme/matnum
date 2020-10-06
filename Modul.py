from math import pi
def metode_bagi_dua(R, V):
  ### Isi jawaban Anda di bawah ###
  f = lambda h: V - pi*(h**2)*(3*R - h)/3

  a = 4
  b = 12
  eps = 10^-8 #Syarat berhenti 
  fa=f(a)
  fb=f(b)

  if b<=a or 0<=fa*fb: 
    return "Invalid input"
  while abs(b-a) >= eps:   
    
    c = (a+b)/2
    fc=f(c)

    if fa*fc<0:
      b = c
      fb=fc
    else:
      a = c
      fa=fc

    if abs(f(c)) < eps :
      break
    print(f"Iter ke-{iter}")
    iter = iter + 1
    
    if iter > 100 : 
      break
    
  return c

R = 2
V = 5
print(metode_bagi_dua(R, V))
