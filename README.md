# Implementing Command Pattern in Python

We will try to lock the door if it is open, unlock the door if it is locked. Imagine you are in the 
home and you want to lock the doors without getting out of your bed. We will implement exactly this
case with Command Pattern.


    # create a lock
    lock = Lock()
    # create a key
    key = new Key()
    # tell the key to lock the lock or vice versa.
    remote_control = RemoteControl(lock)
    key.execute(remote_control)

Result: Door is locked.

    ...
    key.execute(remote_control)
    key.execute(remote_control)

Result: Door is locked. Door is unlocked.

You command the key to lock the door and you see a message on your phone screen tells you that
'Door is unlocked. ', then you give one more command and 'Door is locked.'

Now, we remember that we also have a backdoor which needs to be programmed so that we can open/close
it from the app on our phone. 

We create another class named BackdoorLock. Here we have a small problem: When initializing
RemoteControl class we put Lock object as a parameter, meaning parameter should be an instance of
Lock() object. So, we create LockInterface abstract class, so both Lock and BackdoorLock
object extends it. Then we change Lock object in RemoteControl's construct and tell that just 
make sure that you get any sort of lock object, instead of exactly one kind of lock object(which 
was a Lock() initially.). Now we are good to go.

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
    
And the result is: Door is locked. Backdoor is locked.

The beauty here is you can define your own mechanism of locking and unlocking doors for each locks.
For example, on our BackdoorLock() class we can simplify things and use it to only lock the door,
it is all about your fantasy how to implement this pattern.

#### Note:
It can look like a little weird to use this pattern alone in our case above. But the main issue is
to know how to use it. In general you don't want to use Command Pattern just for this case. But
if you think of using this pattern with other patterns in composition, it is a great way to solve
common design problems.
