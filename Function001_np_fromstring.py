import numpy as np

s1='agtcgtaatgc'

s2="cgaa"

a = np.fromstring(s1,'S1')==np.fromstring(s2,'S1').reshape(-1,1)


np.fromstring('1 2 3', dtype=int, sep=' ')
#array([1, 2, 3])

np.fromstring('1,2,3', dtype=int, sep=',')
#array([1, 2, 3])

np.fromstring('123', np.uint8)
#array([49, 50, 51], dtype=uint8)



