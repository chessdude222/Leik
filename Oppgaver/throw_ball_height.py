v_0 = 0
a = 9.81
y_1 = 5
t = 0
change_t = 0.01
h = 10

y_t = v_0*t-0.5*a*t**2+h

while y_1 <= y_t:
  t += change_t
  y_t = v_0*t-0.5*a*t**2+h

print(t)
print(v_0*t-0.5*a*1**2+h)
