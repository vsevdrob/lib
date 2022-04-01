package main

import (
	"go-file/file"
	"log"
)

func main() {

	name := "./test.py"
	name2 := "./test2.py"
	name3 := "./test3.json"

	file.Create(name)
	log.Println(file.GetName(name))

	file.Create(name)
	file.Rename(name, name2)

	file.Create(name)
	file.Remove(name)

	file.Create(name)
	file.Create(name)

	log.Printf("%t\n", file.IsJSON(name3))
}
