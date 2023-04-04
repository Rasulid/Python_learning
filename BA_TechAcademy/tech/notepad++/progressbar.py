
from progressbar import ProgressBar
import time

bar = ProgressBar(maxval=10)
bar.start()

for i in range(1, 11):
    bar.update(i)
    time.sleep(i)
    
bar.finish()

