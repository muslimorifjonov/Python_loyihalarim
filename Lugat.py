# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:43:32 2022

@author: Muslimbek Orifjonov
"""

'''
Avtor:Muslimbek orifjonov
Mavzu: Lug'atlar bilan ishlash.
'''
lugat={'for':'uchun',
       'in':'ichida degan ma\'noni anglatadi',
       'if':'agar',
       'else':'aks holda degan ma\'noni anglatadi' ,
       'elif':'agar,  aks holda',
       'float':'suzuvchi vergulli sonlar ',
       'integer':'butun sonlar',
       'string':'matn'
       }

sorov=input("Siz dasturlashga oid lu'at so'z kiritishingiz mumkin.").lower()
luga=lugat.get(sorov)
if luga==None:    
        print("Siz kiritgan so'z mavjud emas.")
else:
    print(f"Siz kiritgan sozning tarjimasi:{luga} ")