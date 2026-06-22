// Exercício 4 - Sistema de Controle Financeiro

const gastos = ["800", "900", "700"];

function calcularTotal(valores) {
  let total = 0;

  for (const valor of valores) {
    const convertido = parseFloat(valor);

    if (isNaN(convertido)) {
      continue;
    }

    total += convertido;
  }

  return total;
}

const total = calcularTotal(gastos);

console.log(`Total: R$ ${total}`);
console.log();

if (total > 2000) {
  console.log("Limite ultrapassado");
} else {
  console.log("Gastos dentro do limite");
}
