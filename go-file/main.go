package main

import (
	"go-file/file"
	"go-file/json"
	"log"
)

func main() {

	name := "./test.py"
	name2 := "./test2.py"
	name3 := "./test3.json"
	name4 := "./test4.json"
	name5 := "./test5.py"

	file.Create(name)
	log.Println(file.GetName(name))

	file.Create(name)
	file.Rename(name, name2)

	file.Create(name)
	file.Remove(name)

	file.Create(name)
	file.Create(name)

	log.Printf("%t\n", json.IsJSON(name3))

	json.LoadUnstruct(name4)

	file.Write(name5, []byte("print('Hello World')"))
}
