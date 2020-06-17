import numpy as np

randomarray = np.random.rand(20)*20
print(randomarray)

randomarray = randomarray.reshape(4,5)
print (randomarray)

print("After reshape")
print(randomarray)
print('\n')
print('after replacing max values')
print(np.where(randomarray == np.max(randomarray, axis=1).reshape(-1,1), 0, randomarray))


