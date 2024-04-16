#include <iostream>
#include <fstream>
#include <string>

class FileReader {
public:
    static const char* read_file(const char* filename) {
        std::ifstream file(filename);
        std::cout << "Reading " << filename << std::endl;
        if (!file.is_open()) {
            std::cerr << "Error: Unable to open file " << filename << std::endl;
            return "";
        }

        static std::string content((std::istreambuf_iterator<char>(file)),
                            (std::istreambuf_iterator<char>()));

        file.close();
        return content.c_str();
    }
};

extern "C" {
    FileReader* FileReader_new() {
        return new FileReader();
    }

    const char* FileReader_readFile(FileReader* reader, const char* filename) {
        return reader->read_file(filename);
    }

    void FileReader_delete(FileReader* reader) {
        delete reader;
    }
}