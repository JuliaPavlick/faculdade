// Exercício 5 - Sistema Completo de Eventos

const evento = {
  nome: "Workshop Angular",
  local: "Laboratório 5",
  data: new Date("2026-09-10"),
  participantes: []
};

function exibirEvento(e) {
  console.log(`Evento: ${e.nome}`);

  if (e.local) {
    console.log(`Local: ${e.local}`);
  }

  console.log();

  const dia = String(e.data.getUTCDate()).padStart(2, "0");
  const mes = String(e.data.getUTCMonth() + 1).padStart(2, "0");
  const ano = e.data.getUTCFullYear();
  console.log(`${dia}/${mes}/${ano}`);

  console.log();
  console.log(`Participantes: ${e.participantes.length}`);
  console.log();

  if (e.participantes.length === 0) {
    console.log("Nenhum participante cadastrado");
  } else {
    console.log(`Local cadastrado: ${"local" in e}`);
  }

  console.log();

  for (const chave in e) {
    console.log(`${chave}: ${typeof e[chave]}`);
  }
}

exibirEvento(evento);
