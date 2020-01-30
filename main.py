# -*- coding: utf-8 -*-

import human as hm

w = hm.Woman()
m = hm.Man()

print("-------Reproduction-------")
print(w.age, w.hy)
m.add_age()
w.add_age()
w.set_hy()
print("男人的年龄：{}岁".format(m.age))
print(w.age, w.hy)

