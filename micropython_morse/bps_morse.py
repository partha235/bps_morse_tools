# this program is for micropython device for morse code.

from utime import sleep_ms

class morse_code():
    def __init__(self,pin,dot_time):
        self.pin=pin
        self.dot_time=dot_time

    def dit(self):
        self.pin.on()
        sleep_ms(self.dot_time)
        self.pin.off()
        sleep_ms(self.dot_time)

    def dah(self):
        self.pin.on()
        sleep_ms(self.dot_time*3)
        self.pin.off()
        sleep_ms(self.dot_time)

class Character(morse_code):
    def __init__(self, pin, dot_time,):
        super().__init__(pin, dot_time)

    def a(self):
        self.dit()
        self.dah()
        sleep_ms(self.dot_time*3)

    def b(self):
        self.dah()
        self.dit()
        self.dit()
        self.dit()
        sleep_ms(self.dot_time*3)

    def c(self):
        self.dah()
        self.dit()
        self.dah()
        self.dit()
        sleep_ms(self.dot_time*3)

    def d(self):
        self.dah()
        self.dit()
        sleep_ms(self.dot_time*3)

    def e(self):
        self.dit()
        sleep_ms(self.dot_time*3)

    def f(self):
        self.dit()
        self.dit()
        self.dah()
        self.dit()
        sleep_ms(self.dot_time*3)

    def g(self):
        self.dah()
        self.dah()
        self.dit()
        sleep_ms(self.dot_time*3)
    def h(self):
        self.dit()
        self.dit()
        self.dit()
        self.dit()
        sleep_ms(self.dot_time*3)

    def i(self):
        self.dit()
        self.dit()
        sleep_ms(self.dot_time*3)

    def j(self):
        self.dit()
        self.dah()
        self.dah()
        self.dah()
        sleep_ms(self.dot_time*3)
    
    def k(self):
        self.dah()
        self.dit()
        self.dah()
        sleep_ms(self.dot_time*3)

    def l(self):
        self.dit()
        self.dah()
        self.dit()
        self.dit()
        sleep_ms(self.dot_time*3)

    def m(self):
        self.dah()
        self.dah()
        sleep_ms(self.dot_time*3)

    def n(self):
        self.dah()
        self.dit()
        sleep_ms(self.dot_time*3)

    def o(self):
        self.dah()
        self.dah()
        self.dah()
        sleep_ms(self.dot_time*3)

    def p(self):
        self.dit()
        self.dah()
        self.dah()
        self.dit()
        sleep_ms(self.dot_time*3)

    def q(self):
        self.dah()
        self.dah()
        self.dit()
        self.dah()
        sleep_ms(self.dot_time*3)

    def r(self):
        self.dit()
        self.dah()
        self.dit()
        sleep_ms(self.dot_time*3)

    def s(self):
        self.dit()
        self.dit()
        self.dit()
        sleep_ms(self.dot_time*3)

    def t(self):
        self.dah()
        sleep_ms(self.dot_time*3)

    def u(self):
        self.dit()
        self.dit()
        self.dah()
        sleep_ms(self.dot_time*3)

    def v(self):
        self.dit()
        self.dit()
        self.dit()
        self.dah()
        sleep_ms(self.dot_time*3)

    def w(self):
        self.dit()
        self.dah()
        self.dah()
        sleep_ms(self.dot_time*3)

    def x(self):
        self.dah()
        self.dit()
        self.dit()
        self.dah()
        sleep_ms(self.dot_time*3)

    def y(self):
        self.dah()
        self.dit()
        self.dah()
        self.dah()
        sleep_ms(self.dot_time*3)

    def z(self):
        self.dah()
        self.dah()
        self.dit()
        self.dit()
        sleep_ms(self.dot_time*3)   

    def _1(self):
        self.dit()
        self.dah()
        self.dah()
        self.dah()
        self.dah()

    def _2(self):
        self.dit()
        self.dit()
        self.dah()
        self.dah()
        self.dah()

    def _3(self):
        self.dit()
        self.dit()
        self.dit()
        self.dah()
        self.dah()

    def _4(self):
        self.dit()
        self.dit()
        self.dit()
        self.dit()
        self.dah()

    def _5(self):
        self.dit()
        self.dit()
        self.dit()
        self.dit()
        self.dit()

    def _6(self):
        self.dah()
        self.dit()
        self.dit()
        self.dit()
        self.dit()

    def _7(self):
        self.dah()
        self.dah()
        self.dit()
        self.dit()
        self.dit()

    def _8(self):
        self.dah()
        self.dah()
        self.dah()
        self.dit()
        self.dit()

    def _9(self):
        self.dah()
        self.dah()
        self.dah()
        self.dah()
        self.dit()

    def _0(self):
        self.dah()
        self.dah()
        self.dah()
        self.dah()
        self.dah()

    def period(self):
        self.a()
        self.a()
        self.a()

    def comma(self):
        self.g()
        self.w()

    def semicolon(self):
        self.c()
        self.n()

    def ques(self):
        self.i()
        self.m()
        self.i()

    def hyp(self):
        self.d()
        self.u()

    def apos(self):
        self.w()
        self.g()

    def inv_com(self):
        self.r()
        self.r()

    def brack(self):
        self.k()
        self.k()

    def col(self):
        self.o()
        self.s()

    def slash(self):
        self.x()
        self.e()

    def space(self):
        sleep_ms(self.dot_time*4)

    def start(self):
        self.k()
        self.a()

    def end(self):
        self.v()
        self.a()

    def morse_out(self,char):
        if char.isupper():
            char = char.lower()
        ch_dict={"a":self.a,"b":self.b,"c":self.c,"d":self.d,"e":self.e,"f":self.f,"g":self.g,"h":self.h,"i":self.i,"j":self.j,
        "k":self.k,"l":self.l,"m":self.m,"n":self.n,"o":self.o,"p":self.p,"q":self.q,"r":self.r,"s":self.s,"t":self.t,"u":self.u,"v":self.v,"w":self.w,"x":self.x,"y":self.y,"z":self.z,
        " ":self.space,".":self.period,"0":self._0,"1":self._1,"2":self._2,"3":self._3,"4":self._4,"5":self._5,"6":self._6,
        "7":self._7,"8":self._8,"9":self._9,",":self.comma,";":self.semicolon,":":self.col,"?":self.ques,"-":self.hyp,"'":self.apos,
        "\"":self.inv_com,"(":self.brack,")":self.brack,"[":self.brack,"]":self.brack,"/":self.slash,"\\":self.slash}
        return ch_dict[char]()
  