import re
from enum import Enum

__author__ = "Adrian Podsiadlowski"
__copyright__ = "Python Interest Group - Diehl Controls"
__credits__ = [""]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Adrian Podsiadlowski"
__email__ = "adrian.podsiadlowski@diehl.com"
__status__ = "Initial"


class Errors(Enum):
    NO_ERROR = 0
    NO_MATCHES = 101
    FILE_NOT_ACCESIBLE = 102


class PartData:
    def __init__(self, _item_number, _descriptor, _ako, _revision, _component_status, _description):
        self.item_number = _item_number
        self.descriptor = _descriptor
        self.ako = _ako
        self.revision = _revision
        self.component_status = _component_status
        self.description = _description


class Parts:
    __items = []
    __patern = re.compile(r"""
    SUBI\s+(        # Find expresion starting with SUBI
    \s*(\d+)        # Component number
    \s*(\w+)        # Designator
    \s*(\d{6})      # AKO number
    \s*(\d{2})      # Revision
    \s*(\w{2})      # Component status
    )""", re.RegexFlag.VERBOSE)

    def parse_line(self, line):
        match = self.__patern.search(line)
        if match:
            res = match.groups()
            return Errors.NO_ERROR, PartData(
                _item_number=res[1],
                _descriptor=res[2],
                _ako=res[3],
                _revision=res[4],
                _component_status=res[5],
                _description=""
            )
        else:
            return Errors.NO_MATCHES, 0


class GetBOM:

    __file = None
    __file_name_path = "../BOM_files/BOM.BOM"               # Default BOM path
    bom = {}
    part = Parts()

    def __open_file(self, file_name_path):
        try:
            self.__file = open(file_name_path, 'r')
            return Errors.NO_ERROR
        except:
            return Errors.FILE_NOT_ACCESIBLE

    def __close_file(self):
        self.__file.close()

    def get_bom_data(self, filename = __file_name_path):
        self.__open_file(filename)                              # Open BOM file
        self.bom = {}
        data = self.__file.read().split('\n')                   # Read BOM file as list of strings
                                # Close BOM file
        for element in data:
            error, data2 = self.part.parse_line(element)
            if error == Errors.NO_ERROR:
                self.bom[data2.descriptor] = data2   # Elements found - no errors
        self.__close_file()
        return Errors.NO_ERROR, self.bom

    def __del__(self):
        if self.__file:
            self.__close_file()

