package file

import (
	"io/fs"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func GetInfo(_path string) (fs.FileInfo, error) {
	return os.Stat(_path)
}

func GetName(_path string) string {
	file, err := GetInfo(_path)

	if err != nil {
		log.Fatalln("Error!", err.Error())
	}

	return file.Name()
}

func IsExist(_path string) bool {
	file, err := GetInfo(_path)

	if err == nil {
		name := file.Name()
		log.Printf("File %s already exists.\n", name)

		return true
	} else if os.IsNotExist(err) {
		log.Println("Provided file does not exist.")
		return false
	}

	return false
}

func Create(_path string) {
	if IsExist(_path) == false {
		log.Println("Creating new file ...")

		_, err := os.Create(_path)

		if err != nil {
			log.Fatalln("Error!", err.Error())
		}

		name := GetName(_path)
		log.Printf("File %s is created.\n", name)
	}
}

func ReadString(_path string) string {
	name := GetName(_path)
	content, err := ioutil.ReadFile(_path)

	if err != nil {
		log.Fatalf("Can not read the file %s\n", name)
	}

	return string(content)
}

func ReadByte(_path string) []byte {
	name := GetName(_path)
	content, err := ioutil.ReadFile(_path)

	if err != nil {
		log.Fatalf("Can not read the file %s\n", name)
	}

	return content
}

func Rename(_oldPath string, _newPath string) {
	oldName := GetName(_oldPath)
	err := os.Rename(_oldPath, _newPath)

	if err != nil {
		log.Fatalln("Error!", err.Error())
	}

	newName := GetName(_newPath)

	log.Printf("Successfully renamed (moved) the file %s to %s\n", oldName, newName)
}

func Remove(_path string) {
	name := GetName(_path)

	if err := os.Remove(_path); err != nil {
		log.Fatalln("Error!", err.Error())
	}

	log.Printf("Successfully removed the file %s\n", name)
}

func GetExtension(_path string) string {
	return filepath.Ext(_path)
}

func IsJSON(_path string) bool {
	isJson := strings.HasSuffix(_path, ".json")
	jsonExt := GetExtension(_path)

	if isJson == true && jsonExt == ".json" {
		return true
	} else {
		return false
	}
}