def f(x):
  y=-pow(x,4)+(30*pow(x,3))+(15*pow(x,2))+(34*x)+540
  return y

def biseccion(x1, x2, xra):
  xr=(x1-x2)/2
  ep=(xr-xra)/xr
  if abs(ep)>0.001:
    if (f(x1)*f(xr))>0:
      return biseccion(xr,x2,xr)
    else:
      return biseccion(x1,xr,xr)
  else:
    return xr

print(biseccion(0,1000,0))