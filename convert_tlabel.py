import numpy as np


dt = np.dtype([('age')])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)


annos=[]
img_idx=1
print([img_idx])
#num_example = annos[-1]["name"].shape[0]
num_example = 5
print(np.array(
                [img_idx] * num_example, dtype=np.int64))
annos[-1][0] = np.array(
                [img_idx] * num_example, dtype=np.int64)

print(annos)