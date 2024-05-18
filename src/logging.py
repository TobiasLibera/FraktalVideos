
import  logging
import  logging.config
import  logging.handlers

from    pathlib     import Path

from    utils       import  Paths




class Logger:

    Config  =   None

    Main    =   None
    Calc    =   []


    @classmethod
    def init(cls, Config):
        cls.Config = Config

        Main = logging.getLogger(
                cls.Config.Logging["Names"].get("Main")
                                )
        
        Main.addHandler (
                logging.handlers.RotatingFileHandler(
                        filename    =   (
                                Paths.LOGGING_DIR / 
                                Path(cls.Config.Logging["Files"].get("Main"))
                                        ) ,
                        maxBytes    = cls.Config.Logging["Handlers"].getint("MaxBytes") ,
                        backupCount = cls.Config.Logging["Handlers"].getint("BackupCount") ,
                                                    ).setFormatter  (
                                logging.Formatter   (
                                    fmt     =  cls.Config.Logging["Formatter"].get("Format") ,
                                    datefmt =  cls.Config.Logging["Formatter"].get("DateFormat") ,
                                                    )
                                                                    )
                        )
