class BinString:
    def __init__(self, b):
        b = [format(int(c, base = 16), 'b') for c in input]
        b = "".join(["0" * (4 - len(n)) + n for n in b])
        self.b = b
        self.vtotal = 0

    def pickint(self, n):
        o = self.pick(n)
        return int(o, base=2)

    def pick(self, n):
        o = self.b[:n]
        self.b = self.b[n:]
        return o

    def vt(self):
        v = self.pickint(3)
        t = self.pickint(3)
        return v, t

    def n(self):
        c = 1
        num = ""
        while (c == 1):
            c = self.pickint(1)
            n = self.pick(4)
            num += n
        return int(num, base=2)

    def l(self):
        l = self.pickint(1)
        if (l == 0):
            return self.l0()
        return self.l1()

    def l0(self):
        return 0, self.pickint(15)
    
    def l1(self):
        return 1, self.pickint(11)

    def p(self):
        v, t = self.vt()
        self.vtotal += v
        print(f"v, t: {v, t} and b: {self.b}")
        if (t == 4):
            n = self.n()
            print(f"n: {n}")
            return n
        else:
            values = self.op()

        if (t == 0):
            return sum(values)
        elif (t == 1):
            total = 1
            for v in values:
                total *= v
            return total
        elif (t == 2):
            return min(values)
        elif (t == 3):
            return max(values)
        elif (t == 5):
            if (values[0] > values[1]):
                return 1
            return 0
        elif (t == 6):
            if (values[0] < values[1]):
                return 1
            return 0
        elif (t == 7):
            if (values[0] == values[1]):
                return 1
            return 0

                
    def op(self):
        lt, l = self.l()
        values = []
        print(f"lt, l: {lt, l}")
        if (lt == 0):
            print(f"l type 0")
            cl = len(self.b)
            lr = 0
            
            while(l != lr):
                print (f"l and lr: {l}, {lr}")
                values.append(self.p())
                lr = cl - len(self.b)
        elif (lt == 1):
            print(f"l type 1")
            for i in range(l):
                values.append(self.p())
        return values


input = "E054831006016008CF01CED7CDB2D495A473336CF7B8C8318021C00FACFD3125B9FA624BD3DBB7968C0179DFDBD196FAE5400974A974B55C24DC580085925D5007E2D49C6579E49252E28600B580272379054AF57A54D65E1586A951D860400434E36080410926624D25458890A006CA251006573D2DFCBF4016919CC0A467302100565CF24B7A9C36B0402840002150CA3E46000042621C108F0200CC5C8551EA47F79FC28401C20042E0EC288D4600F42585F1F88010C8C709235180272B3DCAD95DC005F6671379988A1380372D8FF1127BDC0D834600BC9334EA5880333E7F3C6B2FBE1B98025600A8803F04E2E45700043E34C5F8A72DDC6B7E8E400C01797D02D002052637263CE016CE5E5C8CC9E4B369E7051304F3509627A907C97BCF66008500521395A62553A9CAD312A9CCCEAF63A500A2631CCD8065681D2479371E4A90E024AD69AAEBE20002A84ACA51EE0365B74A6BF4B2CC178153399F3BACC68CF3F50840095A33CBD7EF1393459E2C3004340109596AB6DEBF9A95CACB55B6F5FCD4A24580400A8586009C70C00D44401D8AB11A210002190DE1BC43872C006C45299463005EC0169AFFF6F9273269B89F4F80100507C00A84EB34B5F2772CB122D26016CA88C9BCC8BD4A05CA2CCABF90030534D3226B32D040147F802537B888CD59265C3CC01498A6B7BA7A1A08F005C401C86B10A358803D1FE24419300524F32AD2C6DA009080330DE2941B1006618450822A009C68998C1E0C017C0041A450A554A582D8034797FD73D4396C1848FC0A6F14503004340169D96BE1B11674A4804CD9DC26D006E20008747585D0AC001088550560F9019B0E004080160058798012804E4801232C0437B00F70A005100CFEE007A8010C02553007FC801A5100530C00F4B0027EE004CA64A480287C005E27EEE13DD83447D3009E754E29CDB5CD3C"

b = BinString(input)
print(b.b)
print(b.p())
