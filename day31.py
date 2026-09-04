#(array operations and broadcasting)

import numpy as np 
prices=np.array([500,1000,1500,5000])
disconted_prices= prices-(prices*0.10)
print(disconted_prices)

import numpy as np 
stationary_items_prices=np.array([900,800,700,980])
discounted_prices=stationary_items_prices-(stationary_items_prices*0.20)
print(discounted_prices)