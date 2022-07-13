import base64


class Converter:
    __instance = None
    @staticmethod 
    def getInstance():
      """ Static access method. """
      if Converter.__instance == None:
         Converter()
      return Converter.__instance
        
    def __init__(self):        
        if Converter.__instance == None:
            Converter.__instance = self
                    
    def toBase64(self,source_file_path,destination_file_path):        
        excel_file = self.__open_target_file(source_file_path)
        encoded_excel = self.__encode_file(excel_file)
        self.__write_file(destination_file_path,encoded_excel)               
        
    def fromBase64(self,source_file_path,destination_file_path):
        excel_file = self.__open_target_file(source_file_path)
        decoded_excel = self.__decode_file(excel_file)
        self.__write_file(destination_file_path,decoded_excel)  

    def __open_target_file(self,target_path):
        with open(target_path,"rb") as excel_file:
            return excel_file.read()

    def __encode_file(self,excel_file):
        return base64.b64encode(excel_file)

    def __decode_file(self,excel_file):
        return base64.b64decode(excel_file)
    
    def __write_file(self,destination_file_path, excel):
         with open(destination_file_path, "wb") as write_file:
            write_file.write(excel)
            
