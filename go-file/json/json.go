package json

import (
	"encoding/json"
	"go-file/file"
	"go-file/model"
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

func LoadStruct(_path string) (s model.JsonStruct) {
	content := file.ReadByte(_path)

	if err := json.Unmarshal(content, &s); err != nil {
		log.Fatalln("Error!", err.Error())
	}

	return
}

func LoadUnstruct(_path string) (result map[string]interface{}) {
	content := file.ReadByte(_path)

	if err := json.Unmarshal(content, &result); err != nil {
		log.Fatalln("Error!", err.Error())
	}

	return
}
