
def read_file(file_path):
    input_file = open(file_path,'rb')

    data = b''
    data = input_file.read()
    return data

def write_to_file(file_path,data):
    output_file = open(file_path,'wb')
    output_file.write(data)
