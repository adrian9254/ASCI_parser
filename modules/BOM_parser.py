
__author__ = "Adrian Podsiadlowski"
__copyright__ = "Python Interest Group - Diehl Controls"
__credits__ = [""]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Adrian Podsiadlowski"
__email__ = "adrian.podsiadlowski@diehl.com"
__status__ = "Initial"


class Get_BOM():

    __file = None
    __file_name_path = "../BOM_files/BOM.BOM"               # Default BOM path
    bom = {}

    def __open_file(self,file_name_path):
        try:
            self.__file = open(file_name_path, 'r')
        except:
            print("BOM file not accesible! Please check file path and content.")    # Error handling - input file not accesible - example message
            quit()

    def __close_file(self):
        self.__file.close()

    def get_bom_data(self, filename = __file_name_path):
        self.__open_file(filename)                              # Open BOM file
        self.bom = {}
        data = self.__file.read().split('\n')                   # Read BOM file as list of strings
        for element in data:
            if element[0:4] == 'SUBI':                          # Look for "SUBI" header
                line = element.split('\t')                      # Split the line
                self.bom[line[2]] = line[3]
        self.__close_file()                                     # Close BOM file
        return self.bom

    def __del__(self):
        if (self.__file):
            self.__close_file()

