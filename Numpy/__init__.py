import numpy as np

# Can be used for photos
np.zeros(3)
np.empty(3)
np.linspace(2, 10, 5) # From 2 to 10 with 5 elements [2., 4., 6., 8., 10.]
a_list = [1, 2, 3, 4, 5, 6]
a = np.array(a_list)

np.shape

np.random.randint(10, size=6)

a_sin = np.sin(a)
a_sum = np.sum(a)

# print(a > 3)
a[a > 3]

# print(a_sum)

b = np.where(a > 3, 5, 0)

a @ b # . product of the two

a.T  # Transpose - interchanges rows and columns

np.sort(a)

