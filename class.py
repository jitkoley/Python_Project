class Demo:
    """ demo class """

    def __init__(self, Sname, Sid, Snum):
        self.Sname = Sname
        self.Sid = Sid
        self.Snum = Snum

    def information(self):
        print("*" * 10, "😍😍😍😍😍😍", "*" * 10)
        print('Student name is :', self.Sname)
        print('My Student id is :', self.Sid)
        print('My Student Number is :', self.Snum)
        print(Demo.__doc__)  # print the string Doc
        print("-" * 30)


''' Creating  Object'''
s1 = Demo('jit', 13, 7003864771)
s2 = Demo('abhi', 10, 8240516820)
s3 = Demo("Sajim", 12, 9748307475)

""" Call the Method """
s1.information()
s2.information()
s3.information()
##help(Demo)  # help of the class
