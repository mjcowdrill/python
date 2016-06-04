# C# example

from mjc.mjc.mjcMsgActive import *

with mjcMsgActive() as a:

       a.someWork();                  # enqueues work

       a.moreWork();                  # enqueues work

# waits for work to complete and joins with private thread

