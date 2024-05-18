
from    pathlib             import Path
from    configparser        import ConfigParser


from    project_directory   import PROJECT_DIRECTORY




class Paths:

    PROJECT_DIR     = Path(PROJECT_DIRECTORY).resolve()

    CONFIG_DIR      = PROJECT_DIR   / Path("config")
    FRACTALS_DIR    = PROJECT_DIR   / Path("fractals")
    VALIDATION_DIR  = PROJECT_DIR   / Path("validation")
    LOGGING_DIR     = PROJECT_DIR   / Path("logs")

    CONFIG_MAIN     = CONFIG_DIR    / Path("main.cfg")
    CONFIG_LOGGING  = CONFIG_DIR    / Path("logging.cfg")

    JOBS_FILE       = PROJECT_DIR   / Path("jobs.json")
    JOBS_ARCHIVE    = PROJECT_DIR   / Path("jobs.archive.json")




class Config:
    
    Main    = ConfigParser()
    Logging = ConfigParser()
    

    @classmethod
    def init(cls):
        cls.Main.read(   Paths.CONFIG_MAIN)
        cls.Logging.read(Paths.CONFIG_LOGGING)
