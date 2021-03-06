from math import exp

def func(x):
    """Fungsi yang dicari akarnya"""
    return (x*exp(-x))

def dfunc(x):
    """Turunan fungsi yang di cari akarnya"""
    return (1-x)*exp(-x)

def bagi_dua(f,a,b,eps):
    """Algorithma Bagi Dua (bisection)

    Args:
        f (function): fungsi yang dicari akarnya
        a (float): tebakan awal (interval a-b)
        b (float): tebakan awal (interval a-b)
        eps (float): batas ketelititan
    """
    fa=f(a)
    fb=f(b)

    if b<=a or 0<=fa*fb:
        raise ValueError("Tebakan awal tidak sesuai")


    while abs(b-a) > eps :
        c = (a+b)/2
        fc=f(c)

        if fa*fc<0:
            b = c
            fb=fc

        else:
            a = c
            fa=fc

        print(f"Approximation: {c}",f"\nInterval : |{b}-{a}|={b-a}")
    return c

def posisi_palsu(f,a,b,eps):
    """Algorithma Posisi Palsu

    Args:
        f (function): fungsi yang dicari akarnya
        a (float): tebakan awal (interval a-b)
        b (float): tebakan awal (interval a-b)
        eps (float): batas ketelititan
    """
    fa=f(a)
    fb=f(b)

    if b<=a or 0<=fa*fb:
        raise ValueError("Tebakan awal tidak sesuai")

    clama= 2*b-a
    while True :
        c = a-fa*(b-a)/(fb-fa)
        fc=f(c)

        if abs(fc) < 10**-10:
            break

        if fa*fc<0:
            b = c
            fb=fc

        else:
            a = c
            fa=fc

        if abs(c-clama) < eps :
            break
        print(f"clama: {c}",f"\n|c-clama|:{abs(c-clama)}")
        clama=c
    print(c)
    return c

def modifikasi_posisi_palsu(f,a,b,eps):
    """Algorithma Modifikasi Posisi Palsu

    Args:
        f (function): fungsi yang dicari akarnya
        a (float): tebakan awal (interval a-b)
        b (float): tebakan awal (interval a-b)
        eps (float): batas ketelititan
    """

    fa=f(a)
    fb=f(b)

    if b<=a or 0<=fa*fb:
        raise ValueError("Tebakan awal tidak sesuai")

    clama= 2*b-a
    kiri=0
    kanan=0
    while True :
        c = a-fa*(b-a)/(fb-fa)
        fc=f(c)

        if abs(fc) < 10**-10:
            break

        if fa*fc<0:
            b = c
            fb=fc
            kanan,kiri = 0, kiri+1
            if kiri > 2 :
                fa = fa/2

        else:
            a = c
            fa=fc
            kiri,kanan = 0, kanan+1
            if kanan > 2 :
                fb = fb/2

        if abs(c-clama) < eps :
            break
        print(f"clama: {c}",f"\n|c-clama|:{abs(c-clama)}")
        clama=c
    print(c)
    return c

def newton_raphson(f,df,x,eps,maks):
    """Algorithma Newton-Raphson

    Args:
        f (function): fungsi yang dicari akarnya
        df (function): fungsi turunan f
        x (float): tebakan awal
        eps (float): batas galat
        maks (int): batas maksimum iterasi
    """
    for iter in range(1,maks+1):
        d= df(x)
        if abs(d)< 10**-12:
            raise ArithmeticError("Proses gagal")
            break
        xbaru = x-f(x)/d
        delta = abs(xbaru-x)/abs(xbaru)
        print(f"x untuk iterasi-{iter}: {round(xbaru,7)}")
        if delta < eps :
            print(f"Akar:{xbaru}")
            return xbaru
        x = xbaru
    raise ArithmeticError("Proses belum konvergen")

def tali_busur(f,x0,x1,eps,maks):
    """Metode Tali Busur (Secant Method)

    Args:
        f (function): fungsi yang dicari akarnya
        x0 (float): titik 1
        x1 (float): titik 2
        eps (float): batas ketelitian
        maks (int): maksimum iterasi
    """

    f0 = f(x0)
    f1 = f(x1)
    for iter in range(1,maks+1):
        x2 = x1 -f1*(x1-x0)/(f1-f0)
        f2 = f(x2)
        delta = abs(x2-x1)/abs(x2)
        print(f"x untuk iterasi-{iter}: {x2}")
        if delta < eps :
            return x2
        x0 = x1
        f0= f1
        x1 = x2
        f1 = f2
    raise ArithmeticError("Proses belum konvergen")

def newton_raphson_polinom(n,a,z,eps,maks):
    """Algorithma Newton-Raphson untuk polinom

    Args:
        n (int): derajat polinom
        a (array): koefisien polinom dalam bentuk array/list
        z (float): tebakan awal
        eps (float): batas galat
        maks (int): batas maksimum iterasi
    """
    for i in range(iter):

        # Array di copy untuk menghindari komplikasi variabel non-primitif
        b= a.copy()
        c= b.copy()

        b = [a[i]+b[i+1]*z for i in range(1,n)]
        c = [b[i]+c[i+1]*z for i in range(1,n)]
        b[0] = a[0] + b[1]*z

        if abs(c[1]<10**-12):
            raise ArithmeticError("Proses Gagal")

        zbaru = z -b[0]/c[1]
        delta = abs(zbaru-z)/abs(zbaru)
        print(f"akar untuk iterasi-{iter}: {delta}")
        if delta < eps :
            return zbaru
    raise ArithmeticError("Proses belum konvergen")


newton_raphson(func,dfunc,0.2,10**-14,5)
