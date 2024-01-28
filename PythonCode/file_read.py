# This provides various ways to read a file in Python

def read_file_method_1(filename:str) -> None:

    # A good approach is to check whether the file with the given filename is available in the given directory
    file_descriptor = open(filename, 'r', encoding='utf-8')      
    # file descriptor is text interface to a buffered raw stream such as a text file containing strings 
    # mode: read (read only),   
    # write (write the contents into the file), 
    # append (append strings to the existing file, if found or create and write),
    # encoding = 'utf-8' - UTF-8, which stands for "Unicode Transformation Format - 8-bit", is a way to 
    # represent characters in electronic communication. It's essentially the language that 
    # computers use to understand and display text across different languages and platforms


    # Considering only Text-based object: It provides methods for common text operations, such as:
    # read(): Reads all or part of the file's contents as a string.
    # readline(): Reads a single line from the file.
    # readlines(): Reads all lines from the file and returns them as a list of strings.
    # write(): Writes a string to the file.
    # close(): Closes the file, releasing resources. 

    # Read the contents of the file as strings into the variable text
    text:str = file_descriptor.read()

    print(text)

    # Once used it is a good idea to close the file_descriptor
    file_descriptor.close()

    # the file_descriptor is no longer available, the following statements will throw an exception
    # ValueError: I/O operation on closed file.
    # print(file_descriptor.read())

def read_file_method_2(filename:str) -> list:
    #Another method to read the file. In this approach, the file_descriptor is released automatically
    # after the block
    # There is no need close manually using file_descriptor.close()
    with open(filename, 'r', encoding='utf-8') as file_descriptor:
        sentences:list = file_descriptor.readlines()
    return sentences

if __name__ == '__main__':
    # open a file in the current directory using the mode "read only"
    input_file = input('Input file: ')
    # read_file_method_1(input_file)

    sentences = read_file_method_2(input_file)
    dict = {}
    for i, sentence in enumerate(sentences):
        dict[i] = sentence.split(' ')
    print(dict)

    