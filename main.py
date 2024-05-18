

from    src.utils       import  (
                                Config ,
                                )

from    src.ipc         import  (
                                SharedData ,
                                Events ,
                                )

from    src.logging     import  Logger
from    src.exceptions  import  CriticalError
from    src.jobs        import  ReceiveJobs




# REMINDER --> NrOfNodes == -1 -> All Nodes of selected Node type




class ErrorManagement:

    Events          = None
    SharedData      = None
    Logger          = None


    @classmethod
    def init(cls, Events, SharedData, Logger):
        cls.Events      = Events
        cls.SharedData  = SharedData
        cls.Logger      = Logger


    @classmethod
    def work(cls):
        while not cls.Events.Shutdown.is_set():
            try:
                raise cls.SharedData.CriticalErrors.get()

            except CriticalError.ReceiveJobs:
                cls.receive_jobs_critical_error()

            except KeyboardInterrupt:
                cls.keyboard_interrupt()


    @classmethod
    def receive_jobs_critical_error(cls):
        cls.Logger.Main.error("Error Management - Receive Jobs Critical Error detected")
        # maybe retry ???
        cls.init_shutdown()


    @classmethod
    def keyboard_interrupt(cls):
        cls.Logger.Main.warning("Error Management - Keyboard Interrupt detected")
        cls.init_shutdown()


    @classmethod
    def init_shutdown(cls):
        cls.Logger.Main.critical("Error Management - Initializing Shutdown")
        cls.Events.Shutdown.set()




class Main:

    @classmethod
    def run(cls):
        Config.init()
        Logger.init(Config)

        # Just here for fun
        # TODO Put in Threads
        ReceiveJobs.init(Config, Logger, SharedData, Events)    
        ReceiveJobs.work()
        if Events.Shutdown.is_set():
            ReceiveJobs.close()




if __name__ == "__main__":
    Main.run()


    
            
            