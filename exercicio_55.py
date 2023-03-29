class Livro:
    def __init__(self, nome, autor, editora, paginas) -> None:
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def get_nome(self):
        print(f"Nome: {self.nome}")
    
    def get_autor(self):
        print(f"Autor: {self.autor}")

    def get_editora(self):
        print(f"Editora: {self.editora}")
    
    def get_paginas(self):
        print(f"Paginas: {self.paginas}")
    
    def set_editora(self, nova_editora):
        self.editora = nova_editora
    
livro1 = Livro("Sonho de uma noite de Verão", "Shakespeare", "Varias", "915")
livro1.get_nome()
livro1.get_autor()
livro1.get_paginas()
livro1.get_editora()

print("--------------------------------")

livro1.set_editora('Outras')
print(f"Editora Alterada para: {livro1.editora}")
