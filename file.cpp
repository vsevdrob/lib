// Used to interact with filesystem
#include <filesystem>
// Used to read and write from/to console
#include <iostream>
// Used to read and write from/to files
#include <fstream>
#include <string>

class File {
    public:
        bool exists(std::string _pathToFile) {
            return std::__fs::filesystem::exists(_pathToFile); // or use std::filesystem::exists
        }
        
        // Return true if file is empty, false if not, NULL if file not exist.
        bool is_empty(std::string _pathToFile) {
            if (std::__fs::filesystem::exists(_pathToFile))
                return std::__fs::filesystem::is_empty(_pathToFile);
            else
                // return NULL; // Implicit conversion of NULL constant to 'bool'
                return false;
        }

        // If file does not exist - create it, otherwise 
        void create(std::string _pathToFile) {
            if (exists(_pathToFile)) {
                std::cout << "File exists!" << std::endl;        
            } else {
                std::ofstream MyFile(_pathToFile);
                MyFile.close();
            }
        }

        // Write data to file.
        void write(std::string _data, std::string _pathToFile) {
            std::fstream file;
            file.open(_pathToFile, std::ios::out); // output (write) mode
            if (file.is_open()) {
                file << _data << "\n"; 
                file.close();
            }
        }

        // Append data to file.
        void append(std::string _data, std::string _pathToFile) {
            std::fstream file;
            file.open(_pathToFile, std::ios::app); // append mode
            if (file.is_open()) {
                file << _data << "\n";
                file.close();
            }
        }

        std::string read(std::string _pathToFile) {
            std::fstream file;
            std::string data;
            file.open(_pathToFile, std::ios::in); // input (read) mode
            if (file.is_open()) {
                std::string line;
                // Pull each line of text from file.
                while (getline(file, line)) {
                    data.append(line + "\n");
                }
            }
            file.close();
            return data;
        }        
};
