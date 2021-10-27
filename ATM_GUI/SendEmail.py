# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:58:54 2020

@author: Arghya
"""

import smtplib

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.starttls()

Password=input()
mail.login('atmstcet2020@gmail.com',Password)
con=
email=input()
mail.sendmail('atmstcet2020@gmail.com',email,con)
mail.quit()