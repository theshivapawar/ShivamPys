class FileOps:

    @staticmethod
    def read_file(file_name):
            # try:
            #     file = open(file_name, 'r')
            #     print(file)
            #     file.close()
            # except:
            #     print('File does not exist.')

            try:
                with open(file_name, 'r') as file:
                    text = file.read()
                    if len(text) != 0:
                        print(text)
            except FileNotFoundError:
                print('File does not exist.')

    @staticmethod
    def write_file(file_name, text):
        with open(file_name, 'w') as file:
            file.write(text)

    @staticmethod
    def append_file(file_name, text):
        with open(file_name, 'a') as file:
            file.write(text)




FileOps.read_file('text.txt')
FileOps.write_file('text.txt', 'Hello, World!')
FileOps.read_file('text.txt')
FileOps.append_file('text.txt', ' How are you!')
FileOps.read_file('text.txt')