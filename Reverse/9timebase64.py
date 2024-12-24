import math
import time
import base64

# # Math.floor(new Date().getTime() / 1000)
time1 = math.floor(time.time() * 1000)
mcode = base64.b64encode(str(time1).encode()).decode()
print(mcode)