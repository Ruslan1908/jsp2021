import time
import os
now = time.strftime("%Y_%m_%d")
print(now)
cos = "plik_"+now+".txt"
print(cos)
os.rmdir("katalog")
