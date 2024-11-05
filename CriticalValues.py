import math

L1 = float(input("L1 Value 'Put zero if none'"))
Rc = float(input("Rc Value'Put zero if none'"))
Lp = float(input("Lp Value'Put zero if none'"))
Lc = float(input("Lc Value'Put zero if none'"))
Lt = float(input("Lt Value'Put zero if none'"))
AM = float(input("Alpha Max Value'Put zero if none'"))
Rv = float(input("Rv Value'Put zero if none'"))
V = float(input("V Value 'Put zero if none'"))
h = float(input("H Value 'Put zero if none'"))

# -----------------------Starting with 4/5 in first equation-------------------
if L1 == 0:
    if Rc > 0:
        if Lp > 0:
            if Lc > 0:
                if Lt > 0:
                    L1 = - Rc + Lp + Lc - Lt
                    if L1 > 0:
                             print ("yes L1")    
if Rc == 0:
    if L1 > 0:
        if Lp > 0:
            if Lc > 0:
                if Lt > 0:
                    Rc = -L1 + Lp + Lc - Lt
                    if Rc > 0:
                        print("yes Rc")
if Lp == 0:
    if L1 > 0:
        if Rc > 0:
            if Lc > 0:
                if Lt > 0:
                    Lp = L1 +Rc - Lc + Lt
                    if Lp > 0:
                        print("yes Lp")  
if Lc == 0:
    if L1 > 0:
        if Rc > 0:
            if Lp > 0:
                if Lt > 0:
                    Lc =L1 + Rc - Lp + Lt
                    if Lp > 0:
                        print("yes Lc")  
if Lt == 0:
    if L1 > 0:
        if Rc > 0:
            if Lp > 0:
                if Lc > 0:
                    Lt =-L1 - Rc + Lp + Lc
                    if Lp > 0:
                        print("yes Lt")
 # AM, V, H                      
if Rc > 0:
    if L1 >0:
        if Rv > 0:
            AM = (math.asin(Rc/L1))*(180/math.pi)
            V = (Rc/L1)*(Rv)
            h = ((math.cos(math.asin(Rc/L1))))*(Rv)
#-----------starting with 2/3 second equation-------------------------
# Am V H
if AM == 0:
    if Rc > 0:
        if L1 > 0:
            AM = (math.asin(Rc/L1))*(180/math.pi) 

if Rc == 0:
    if AM > 0:
        if L1 > 0:
            Rc = (math.sin(math.radians(AM)))*(L1)
    if AM == 0:
        if V > 0:
            if Rv > 0:
                AM = (math.asin(V/Rv))
    
if L1 == 0:
    if Rc > 0:
        if AM > 0:
            L1 = (Rc)/(math.sin(math.radians(AM)))

if L1 == 0:
    if Rc > 0:
        if Lp > 0:
            if Lc > 0:
                if Lt > 0:
                    L1 = - Rc + Lp + Lc - Lt
                    if L1 > 0:
                             print ("yes L1")    
if Rc == 0:
    if L1 > 0:
        if Lp > 0:
            if Lc > 0:
                if Lt > 0:
                    Rc = -L1 + Lp + Lc - Lt
                    if Rc > 0:
                        print("yes Rc")
if Lp == 0:
    if L1 > 0:
        if Rc > 0:
            if Lc > 0:
                if Lt > 0:
                    Lp = L1 +Rc - Lc + Lt
                    if Lp > 0:
                        print("yes Lp")  
if Lc == 0:
    if L1 > 0:
        if Rc > 0:
            if Lp > 0:
                if Lt > 0:
                    Lc =L1 + Rc - Lp + Lt
                    if Lp > 0:
                        print("yes Lc")  
if Lt == 0:
    if L1 > 0:
        if Rc > 0:
            if Lp > 0:
                if Lc > 0:
                    Lt =-L1 - Rc + Lp + Lc
                    if Lp > 0:
                        print("yes Lt")

if V == 0:
    V = (Rc/L1)*(Rv) 
if AM == 0:
    AM = (math.asin(Rc/L1))*(180/math.pi)
if L1 == 0:
    h = ((math.cos(math.asin(Rc/L1))))*(Rv)

print(L1, "L1")
print(Rc,"Rc")
print(Lp,"Lp")
print(Lc,"Lc")
print(Lt,"Lt")
print(AM,"AM")
print(Rv,"Rv")
print(V,"V")
print(h,"h")