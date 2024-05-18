
import  socket

from    validation  import  ValidateDictData

from    exceptions  import  (
                                CriticalError ,
                                InvalidJobError ,
                            )






class Jobs:

    class Job():
        
        def __init__(self, id = None):
            self.id = id

        def get_id(self):
            return self.id        

        def set_id(self, id):
            self.id = id


    class New(Job):

        def __init__(self, data = None, id = None):
            self.data   = data
            self.id     = id 

        def get_data(self):
            return self.data

        def set_data(self, data):
            self.data = data


    class Archive(Job):
        pass


    class Remove(Job):
        pass




class ReceiveJobs:

    Config          = None
    Logger          = None
    SharedData      = None
    Events          = None

    jobs_socket     = None
    jobs_connection = None
  
    new_job         = None


    @classmethod
    def init(cls, Config, Logger, SharedData, Events):
        cls.Config      = Config
        cls.Logger      = Logger
        cls.SharedData  = SharedData
        cls.Events      = Events

        try:
            cls.jobs_socket = socket.socket (
                                    socket.AF_INET ,
                                    socket.SOCK_STREAM ,
                                            )         
            cls.init_socket()

        except OSError:
            cls.close_socket()
            cls.Logger.Main.error("Receive Jobs - Failed to setup socket")
            cls.report_critical_error()


    @classmethod
    def work(cls):
        while not cls.Events.Shutdown.is_set():
            try:
                cls.jobs_connection, _ = cls.jobs_socket.accept()

            except  (
                        OSError ,
                        BlockingIOError ,
                        InterruptedError ,
                        ConnectionAbortedError ,
                    ):
                if cls.Events.Shutdown.is_set():
                    cls.Logger.Main.info("Receive Jobs - Shutting down service")
                    return
                cls.Logger.Main.warning("Receive Jobs - Failed to accept connection")
                continue

            cls.receive_and_process_new_job()


    @classmethod
    def close(cls):
        cls.close_socket()


    @classmethod
    def report_critical_error(cls):
        cls.SharedData.CriticalErrors.put   (
                CriticalError.ReceiveJobs
                                            )


    @classmethod
    def init_socket(cls):
        cls.jobs_socket.listen  (
                cls.Config.Main["Connection"].getint("ReceiveJobBacklog")
                                )
     
        cls.jobs_socket.bind    (
                    (
                    cls.Config.Main["Connection"].get(   "ReceiveJobIP") ,
                    cls.Config.Main["Connection"].getint("ReceiveJobPort") ,
                    )
                                )


    @classmethod
    def send_response_msg(cls, response):
        response = cls.Config.Main  [
                "StatusMessages"
                                ].get(response).encode()
        try:
            cls.jobs_connection.sendall(response)

        except:
            pass
            cls.Logger.Main.warning("Receive Jobs - Failed to respond to client")


    @classmethod
    def receive_and_process_new_job(cls):
        try:
            cls.receive_new_job()    
        except:
            cls.send_response_msg("Error")
            cls.Logger.Main.warning("Receive Jobs - Failed to receive job via TCP")
            return

        try:
            ValidateDictData.parse(cls, cls.new_job)
        except InvalidJobError:
            cls.send_response_msg("Invalid")
            cls.Logger.Main.info("Receive Jobs - Received invalid Job")
            return
             
        cls.push_new_job_to_job_manager()
        
        cls.send_response_msg("Success")
        cls.Logger.Main.info("Receive Jobs - Received valid Job")


    @classmethod
    def push_new_job_to_job_manager(cls):
        cls.SharedData.JobActions.put   (
                Jobs.New(cls.new_job)
                                        )
        

    @classmethod
    def close_socket(cls):
        try:
            cls.jobs_socket.close()
        except:
            pass
        
        cls.jobs_socket = None


    @classmethod
    def receive_new_job(cls):
        cls.new_job = b""
        
        while True:
            new_job_buffer = cls.jobs_connection.recv   (
                    cls.Config.Main["Connection"].getint("ReceiveJobBuffer")
                                                        )
            if not new_job_buffer:
                break
            cls.new_job += new_job_buffer


    @classmethod
    def return_validated_data(cls, valid_job):
        cls.new_job = valid_job
