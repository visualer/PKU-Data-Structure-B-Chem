class Rational:
    def _gcd(a,b):
        c=max(a,b)
        d=min(a,b)
        while c%d!=0:
            t=c%d
            c=d
            d=t
        return d
    def __init__(self, num, den=1):
        if type(num)!=int or type(den)!=int:
            raise TypeError
        self.num=num;
        sgn=1
        if den==0:
            raise ZeroDivisionError
        else:
            self.den=den
        if num*den<0:
            sgn=-1
        s=Rational._gcd(abs(num),abs(den))
        self.num=sgn*abs(num)//s
        self.den=abs(den)//s
    def val(self):
        return self.num*1.0/self.den
    def print(self):
        print(self.num, end='')
        if(self.den!=1):
            print("/", end='')
            print(self.den, end='')
    def opp(self): #opposite number
        return Rational(-self.num,self.den)
    def rec(self): #reciprocal
        return Rational(self.den,self.num)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self, another):
        return Rational(self.num*another.den+another.num*self.den, self.den*another.den)
    def __sub__(self, another):
        return self+another.opp()
    def __mul__(self, another):
        return Rational(self.num*another.num, self.den*another.den)
    def __truediv__(self, another):
        return self*another.rec()
    def __gt__(self, another):
        return self.val()>another.val()
    def __lt__(self, another):
        return another>self
    def __ge__(self, another):
        return self.val()>=another.val()
    def __le__(self, another):
        return another>=self
    def __eq__(self, another):
        return self<=another and self>=another
    pass
