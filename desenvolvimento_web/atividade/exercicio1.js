// Exercício 1 - Sistema de Cadastro de Produtos

const produto = {
  nome: "Monitor",
  categoria: "Informática",
  preco: "899.90",
  estoque: 5
};

function exibirProduto(p) {
  const precoConvertido = parseFloat(p.preco);

  if (isNaN(precoConvertido)) {
    console.log("Preço inválido.");
    return;
  }

  console.log(`Produto: ${p.nome}`);
  console.log(`Categoria: ${p.categoria}`);
  const precoFormatado = Number.isInteger(precoConvertido)
    ? precoConvertido
    : precoConvertido.toFixed(2);
  console.log(`Preço: R$ ${precoFormatado}`);
  console.log();

  if (p.estoque < 10) {
    console.log("Estoque baixo");
  } else {
    console.log("Estoque adequado");
  }

  console.log();
  console.log(Object.keys(p));
  console.log();

  for (const chave in p) {
    console.log(`${chave}: ${typeof p[chave]}`);
  }
}

exibirProduto(produto);
