import base64

def open_target_file(target_path):
    with open(target_path,"rb") as excel_file:
        return excel_file.read()

def encode_file(excel_file):
    return base64.b64encode(excel_file)

def decode_file():
    return base64.b64decode(excel_file)

your_excel_path = "D:\Chola_work\Source\Bank_Details__c1.csv"
destiny_path = "D:\Chola_work\destination\Bank_Details__c1.csv"

excel_file = open_target_file(your_excel_path)
encoded_excel = encode_file(excel_file)
#decoded_excel = decode_file(encoded_excel)

with open(destiny_path, "wb") as encoded_file:
    encoded_file.write(encoded_excel)
    
