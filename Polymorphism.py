# # POLYMORPHISM:
# class Police:
#     def work(self):
#         print("Control law and order")
# class Docter:
#     def work(self):
#         print("Tretment of patient")
# class Teacher():
#     def work(self):
#       print("Teach student")
# # xyz=[Police(),Docter(),Teacher()]
# # for i in xyz:
# #    i.work()
# P=Police()
# P.work()
# D=Docter()
# D.work()
# T=Teacher()
# T.work()

class student:
    def work(self):
        print("student:","reading book")
class cricketers:
    def work(self):
        print("Cricketers:","playing a cricket")
class singers:
    def work(self):
        print("singers:","to sing a song")

abc=[student(),cricketers(),singers()]   #FIRST METHODE
for m in abc:
    m.work()

# s=student()  #SECOND METHODE
# s.work()
# c=cricketers()
# c.work()
# m=singers()
# m.work()
