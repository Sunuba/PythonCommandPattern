from CommandPattern.classes.LockTypes import Lock, BackdoorLock
from CommandPattern.classes.RemoteControl import RemoteControl
from CommandPattern.classes.Key import Key


# create a lock object, it is the lock in the main door
lock = Lock()

# create a BackdoorLock object, it is the lock in the backdoor
backdoor_lock = BackdoorLock()

# create a key. It is like a token that works everywhere inside a system
key = Key()

# press a key on the remote control to lock the main door
remote_control = RemoteControl(lock)
key.execute(remote_control)

# press a key on the remote control to lock a backdoor
remote_control = RemoteControl(backdoor_lock)
key.execute(remote_control)
# executing the command twice will unlock the door,
# in this case it unlocks backdoor lock, uncomment the line below to see the effect.
# key.execute(remote_control)
