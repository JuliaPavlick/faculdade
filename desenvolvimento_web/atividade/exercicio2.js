// Exercício 2 - Sistema de Matrícula Acadêmica

const disciplinas = ["Banco de Dados", "", "TCC", "Redes"];

for (let i = 0; i < disciplinas.length; i++) {
  if (disciplinas[i] === "") {
    continue;
  }

  console.log(disciplinas[i]);

  if (disciplinas[i] === "TCC") {
    console.log();
    console.log("Laço interrompido");
    break;
  }
}

console.log();
console.log(`Total: ${disciplinas.filter(d => d !== "").length}`);
console.log();

if (disciplinas.includes("JavaScript")) {
  console.log("Aluno cursa JavaScript");
} else {
  console.log("Aluno não cursa JavaScript");
}

disciplinas.push("Nova Disciplina");
