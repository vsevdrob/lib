//
// Include necessary libraries
//

#include <filesystem>       // Used to interact with filesystem
#include <iostream>         // Used to read and write from/to console
#include <fstream>          // Used to read and write from/to files
#include <string>           // Used to work with string data type

//
// Assigning std libraries
//

// #include <iostream>
using std::cout; using std::endl;
// #include <fstream>
using std::fstream;
// #include <string>
using std::string;

class File {
    public:
        bool exists(string _pathToFile) {
            return std::__fs::filesystem::exists(_pathToFile); // or use std::filesystem::exists
        }
        
        // Return true if file is empty, false if not, false (should be NULL) if file not exist.
        bool is_empty(string _pathToFile) {
            if (std::__fs::filesystem::exists(_pathToFile))
                return std::__fs::filesystem::is_empty(_pathToFile);
            else
                // return NULL; // Implicit conversion of NULL constant to 'bool'
                return false;
        }

        // If file does not exist - create it, otherwise 
        void create(string _pathToFile) {
            if (exists(_pathToFile)) {
                cout << "File exists!" << endl;        
            } else {
                std::ofstream MyFile(_pathToFile);
                MyFile.close();
            }
        }

        // Write data to file.
        void write(string _data, string _pathToFile) {
            fstream file;
            file.open(_pathToFile, std::ios::out); // output (write) mode
            if (file.is_open()) {
                file << _data << "\n"; 
                file.close();
            }
        }

        // Append data to file.
        void append(string _data, string _pathToFile) {
            fstream file;
            file.open(_pathToFile, std::ios::app); // append mode
            if (file.is_open()) {
                file << _data << "\n";
                file.close();
            }
        }

        string read(string _pathToFile) {
            fstream file;
            string data;
            file.open(_pathToFile, std::ios::in); // input (read) mode
            if (file.is_open()) {
                string line;
                // Pull each line of text from file.
                while (getline(file, line)) {
                    data.append(line + "\n");
                }
            }
            file.close();
            return data;
        }        
};
