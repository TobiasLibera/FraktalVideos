
from    multiprocessing     import Event, Queue




class SharedData:

    JobActions      = Queue()




class Events:
   
    CriticalError = Event()
    Shutdown      = Event()
