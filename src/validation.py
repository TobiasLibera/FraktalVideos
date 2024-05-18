
import  json

from    exceptions      import InvalidJobError 




class ValidateDictData:

    data    = None


    @classmethod
    def parse(cls, applicant, data):
        cls.data = data

        cls.data_to_str()
        cls.data_to_dict()
        cls.match_data_with_mask(applicant)
        cls.validate_main_keys()
        cls.validate_types()

        applicant.return_validated_data(cls.data)


    @classmethod
    def data_to_str(cls):
        if type(cls.data) is bytes:
            try:
                cls.data = cls.data.decode().strip()
            except:
                raise InvalidJobError


    @classmethod
    def data_to_dict(cls):
        if type(cls.data) is str: 
            try:
                cls.data = json.loads(cls.data)
            except:
                raise InvalidJobError
            

    @classmethod
    def match_data_with_mask(cls, applicant):
        pass


    @classmethod
    def validate_main_keys(cls):
        if "Ident" not in cls.data.keys():
            raise InvalidJobError
        if type(cls.data["Ident"]) is not str:
            raise InvalidJobError
        
        if "Type" not in cls.data.keys():
            raise InvalidJobError
        if type(cls.data["Type"]) is not str:
            raise InvalidJobError

        if "Priority" not in cls.data.keys():
            raise InvalidJobError
        if type(cls.data["Priority"]) is not int:
            raise InvalidJobError


        if cls.data["Type"] not in cls.data.keys():
            raise InvalidJobError
        if type(cls.data[ cls.data["Type"] ]) is not dict:
            raise InvalidJobError
    

    @classmethod
    def validate_types(cls):
        """
        Add other types if necessary
        """
        if cls.data["Type"] == "fractals":
            cls.validate_type_fractals()
        else:
            raise InvalidJobError


    @classmethod
    def validate_type_fractals(cls):
        if "Type" not in cls.data["fractals"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["Type"]) is not str:
            raise InvalidJobError

        if "Target" not in cls.data["fractals"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["Target"]) is not str:
            raise InvalidJobError


        if "NodeManagement" not in cls.data["fractals"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["NodeManagement"]) is not dict:
            raise InvalidJobError
        
        if "NodeRing" not in cls.data["fractals"]["NodeManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["NodeManagement"]["NodeRing"]) is not str:
            raise InvalidJobError
        
        if "NrOfNodes" not in cls.data["fractals"]["NodeManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["NodeManagement"]["NrOfNodes"]) is not int:
            raise InvalidJobError


        if "FileManagement" not in cls.data["fractals"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["FileManagement"]) is not dict:
            raise InvalidJobError
        
        if "TargetDirectory" not in cls.data["fractals"]["FileManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["FileManagement"]["TargetDirectory"]) is not str:
            raise InvalidJobError
        
        if "FilePrefix" not in cls.data["fractals"]["FileManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["FileManagement"]["FilePrefix"]) is not str:
            raise InvalidJobError
        
        if "FileSuffix" not in cls.data["fractals"]["FileManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["FileManagement"]["FileSuffix"]) is not str:
            raise InvalidJobError
        
        if "FileExtension" not in cls.data["fractals"]["FileManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["FileManagement"]["FileExtension"]) is not str:
            raise InvalidJobError
        
        if "FileType" not in cls.data["fractals"]["FileManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["FileManagement"]["FileType"]) is not str:
            raise InvalidJobError
        
        if "AsBytes" not in cls.data["fractals"]["FileManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["FileManagement"]["AsBytes"]) is not bool:
            raise InvalidJobError


        if "CalcManagement" not in cls.data["fractals"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcManagement"]) is not dict:
            raise InvalidJobError
        
        if "ProcessNr" not in cls.data["fractals"]["CalcManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcManagement"]["ProcessNr"]) is not int:
            raise InvalidJobError
        
        if "WorkDistribution" not in cls.data["fractals"]["CalcManagement"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcManagement"]["WorkDistribution"]) is not bool:
            raise InvalidJobError


        if "CalcParameters" not in cls.data["fractals"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]) is not dict:
            raise InvalidJobError
        
        if "FrameNr" not in cls.data["fractals"]["CalcParameters"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["FrameNr"]) is not int:
            raise InvalidJobError
        
        if "ZoomFactor" not in cls.data["fractals"]["CalcParameters"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["ZoomFactor"]) not in [float, int]:
            raise InvalidJobError
        
        if "ZoomPointSlct" not in cls.data["fractals"]["CalcParameters"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["ZoomPointSlct"]) is not int:
            raise InvalidJobError
        
        if "Resolution" not in cls.data["fractals"]["CalcParameters"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["Resolution"]) is not dict:
            raise InvalidJobError
        
        if "InitZoomPoint" not in cls.data["fractals"]["CalcParameters"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["InitZoomPoint"]) is not dict:
            raise InvalidJobError

        if "IterMap" not in cls.data["fractals"]["CalcParameters"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["IterMap"]) is not int:
            raise InvalidJobError


        if "Width" not in cls.data["fractals"]["CalcParameters"]["Resolution"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["Resolution"]["Width"]) is not int:
            raise InvalidJobError
        
        if "Height" not in cls.data["fractals"]["CalcParameters"]["Resolution"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["Resolution"]["Height"]) is not int:
            raise InvalidJobError
        

        if "x" not in cls.data["fractals"]["CalcParameters"]["InitZoomPoint"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["InitZoomPoint"]["x"]) not in [float, int]:
            raise InvalidJobError
        
        if "y" not in cls.data["fractals"]["CalcParameters"]["InitZoomPoint"].keys():
            raise InvalidJobError
        if type(cls.data["fractals"]["CalcParameters"]["InitZoomPoint"]["y"]) not in [float, int]:
            raise InvalidJobError
