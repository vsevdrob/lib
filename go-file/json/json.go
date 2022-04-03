package json

import (
	"encoding/json"
	"go-file/file"
	"log"
	"strings"
)

func IsJSON(_path string) bool {
	isJson := strings.HasSuffix(_path, ".json")
	jsonExt := file.GetExtension(_path)

	if isJson == true && jsonExt == ".json" {
		return true
	} else {
		return false
	}
}

func LoadStruct(_path string, _struct interface{}) (interface{}, error) {
	content, err := file.ReadByte(_path)
	result := _struct

	if err != nil {
		log.Println("Error!", err.Error())
	}

	err = json.Unmarshal(content, &result)

	if err != nil {
		log.Println("Error!", err.Error())
		return nil, err
	}

	return result, err
}

func LoadUnstruct(_path string) (map[string]interface{}, error) {
	content, err := file.ReadByte(_path)
	var result map[string]interface{}

	if err != nil {
		log.Println("Error!", err.Error())
	}

	err = json.Unmarshal(content, &result)

	if err != nil {
		log.Println("Error!", err.Error())
	}

	return result, err
}

func Dump(_path string, _data interface{}) error {
	res, err := json.Marshal(_data)

	if err != nil {
		log.Println("Error!", err.Error())
		return err
	}

	if err := file.Write(_path, res, 0644); err != nil {
		log.Println("Error!", err.Error())
		return err
	}

	return err

}
