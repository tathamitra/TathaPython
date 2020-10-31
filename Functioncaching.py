import time
from functools import  lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)




if __name__ == "__main__":

 print("calling function")
 some_work(3)
 print("called again")
 some_work(3)
 print("calling done")

