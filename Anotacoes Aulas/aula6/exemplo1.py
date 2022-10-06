import json

data = {}

data["sp"] = "São Paulo"
data["rj"] = "Rio de Janeiro"
data["mg"] = "Minas Gerais"

#faz a escrita do arquivo json
file = open("arq/exemplo1.json", "w", encoding= "utf-8")
#file = open("arq/exemplo1.json", "w")

#json.dump(data, file, sort_keys = True, indent = 4)
json.dump(data, file, sort_keys = True, indent = 4, ensure_ascii = False)
file.close()

#faz a leitura do arquivo
file = open("arq/exemplo1.json", "r")
data = json.load(file)

file.close
print(data)