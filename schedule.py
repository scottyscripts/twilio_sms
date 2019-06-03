# time.time()
#     - time since epoch (time.gmtime(0))


# time.gmtime(time.time())
#   - UTC time
# time.localtime(time.time())
#   - localtime check time.tzname
#
# time.gmtime()
#   - uses time.time() for default

scheduler.enterabs(time, priority, action, argument=(), kwargs={})

time argument should be a numeric type compatible with the return value of the timefunc function passed to the constructor

we use time.time() so we want to pass it seconds

import sched, time
s = sched.scheduler(time.time, time.sleep)
