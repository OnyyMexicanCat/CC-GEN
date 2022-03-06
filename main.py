import random
import US as us
import EU as eu
import AS as asia
import ALL as all
from random import randint as run

print("[////𝓒𝓒 𝓖𝓮𝓷 𝓫𝔂 @𝓞𝓷𝔂𝔂𝓣𝓱𝓮𝓑𝓮𝓼𝓽\\\\\\\]")
print("[1] US")
print("[2] EU")
print("[3] ASIA")
print("[4] ALL")
select1 = input("Select bin country: ")
if select1 == "1":
    us.generaUS()
if select1 == "2":
    eu.generaEU()
if select1 == "3":
    asia.generaAS()
if select1 == "4":
    all.generaALL()