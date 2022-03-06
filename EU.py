import random
from random import randint as run
import bonazzo
import string

def generaEU():
  num = input("How many cc do you want: ")
  num = int(num)

  for i in range(num):
    marocco = (random.choice(list(bonazzo.EU)))
      

    g,r,p='\033[1;32m','\033[1;31m','\033[1;35m'

    bb = marocco
    mm= str(random.randrange(1,12))
    yy= str(random.randrange(2,9))
    cc=0
    h = 16

    def alive(card_number):
                sum = 0
                num_digits = len(card_number)
                oddeven = num_digits & 1
                for count in range(0, num_digits):
                  digit = int(card_number[count])
                  if not (( count & 1 ) ^ oddeven ):
                    digit = digit * 2
                  if digit > 9:
                    digit = digit - 9
                    sum = sum + digit
                  return ( (sum % 10) == 0 )

    def bins(gen):
              if len(str(marocco))==6:
                bb1 = "".join(random.choices(
                  string.digits,
                  k = 10))
                bb = f"{marocco}{bb1}"
              else:
                bb1 = "".join(random.choices(
                  string.digits,
                  k = 8))
                bb = f"{marocco}{bb1}"
              return bb

    def mont(mm):
                if len(str(mm))==0:
                  mm=str(run(1,12))
                  if int(mm)<10:
                    mm=("0"+str(mm))
                elif mm=='1':
                  mm=mm+str(run(0,2))
                else:
                  if int(mm)<10:
                    mm=("0"+str(mm))
                return mm

    def year(yy):
                if len(str(yy))==0:
                  yy="2"+str(run(1, 9))
                elif len(str(yy))==1:
                  yy=f"2{yy}"
                elif len(str(yy))==2:
                  yy=f"2{yy}"
                return yy

    b,y,nn='\033[1;36m','\033[1;33m',list("0123456789")

    def cvv(cc):
              rocco = str(random.randrange(3,4))
              if rocco == "3":
                cc = "".join(random.choices(
                    string.digits,
                    k = 3))
              else:
                cc = "".join(random.choices(
                    string.digits,
                    k = 4))
              return cc

    toto=str(bins(bb)+"|"+mont(mm)+"|"+year(yy)+"|"+cvv(cc))
    print(toto)