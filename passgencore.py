#!/usr/bin/python3

import random
import itertools
import threading
import time
import sys
import string
import os

# ================================ Function () -_o ==============================

class PassGen():


    def generator_phrase():
        # return "%02x%02x%02x%02x%02x%02x" % (
        return "%s%s%s%s%s%s" % (
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9)
        )


    def id_generator(size=6, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for _ in range(size))


    def id_generator_lower(size=6, chars=string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size))


    def true_phrase(string_var):
        random.shuffle(string_var)
        string_var = ''.join(str(e) for e in string_var)
        return string_var


    def rand_spchar(lenght_spchar):
        spchar = ""
        specialchar = ['@', '!', '/', '*', '>', '+']
        for e in range(0, int(lenght_spchar)):
            i = random.randint(1, 5)
            spchar += specialchar[i]
        return spchar



#==================================================================== main object's =======================================
    def auto_gen():
        s = list(PassGen.generator_phrase() + PassGen.id_generator(10) + PassGen.id_generator_lower(6))
        pph = str(PassGen.true_phrase(s))
        lenght_pph = str(len(pph))
        return(pph)


    def len_gen(lenght_num):
        lenght_num = (int(lenght_num) - 6) // 2
        s = list(PassGen.generator_phrase() + PassGen.id_generator(lenght_num) + PassGen.id_generator_lower(lenght_num))
        pph = str(PassGen.true_phrase(s))
        lenght_pph = str(len(pph))
        return(pph)


    def spc_gen(lenght_num, lenght_spchar):
        lenght_num = (int(lenght_num) - 6) // 2
        s = list(
            PassGen.generator_phrase() + PassGen.id_generator(lenght_num) + PassGen.id_generator_lower(lenght_num) + PassGen.rand_spchar(lenght_spchar))
        pph = str(PassGen.true_phrase(s))
        lenght_pph = str(len(pph))
        return (pph)
