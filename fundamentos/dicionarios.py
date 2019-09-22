pessoa = {"nome": "Prof(a). Ana", "idade": 38, "cursos": ["Ingles", "Portugues"]}

print(type(pessoa))

print(len(pessoa))

print(pessoa)

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cursos"][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get("idade"))

# caso uma prpriedade nao exista
# pode ser retornado um valor default

print(pessoa.get("tags", []))


pessoa2 = {"nome": "Prof. Alberto", "idade": 43, "cursos": ["React", "Python"]}

pessoa2["idade"] = 44
pessoa2["cursos"].append("Angular")

print(pessoa2)

pessoa2.pop("idade")
print(pessoa2)

pessoa2.update({"idade": 40, "sexo": "M"})
print(pessoa2)

del pessoa2["cursos"]
print(pessoa2)

pessoa2.clear()
print(pessoa2)






