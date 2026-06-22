// Exercício 3 - Sistema de Biblioteca

const autores = "J. K. Rowling,J. R. R. Tolkien";
const autorBuscado = "Machado de Assis";

const listaAutores = autores.split(",");

listaAutores.forEach(autor => console.log(autor));

console.log();

if (listaAutores.includes(autorBuscado)) {
  console.log("Autor encontrado");
} else {
  console.log("Autor não encontrado");
}

function exibirLivro(titulo, autor) {
  return `Livro: "${titulo}" — Autor: ${autor}`;
}

console.log();
console.log(exibirLivro("Dom Casmurro", "J. K. Rowling"));
console.log();
console.log(listaAutores.join(", "));
