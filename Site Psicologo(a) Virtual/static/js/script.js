      const mensagemInput = document.getElementById("mensagem");

      async function enviarMensagem() {
        const mensagem = mensagemInput.value.trim();
        if (!mensagem) return;

        adicionarMensagem("Você", mensagem);
        mensagemInput.value = "";

        const resposta = await fetch("/enviar", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ mensagem }),
        }).then((res) => res.json());

        adicionarMensagem("Assistente", resposta.resposta);
      }

      mensagemInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
          event.preventDefault();
          enviarMensagem();
        }
      });

      function adicionarMensagem(remetente, texto) {
        const chatBox = document.getElementById("chat-box");
        const mensagemDiv = document.createElement("div");
        mensagemDiv.classList.add(
          remetente === "Você" ? "mensagem-usuario" : "mensagem-assistente"
        );
        mensagemDiv.innerHTML = `<strong>${remetente}:</strong> ${texto}`;
        chatBox.appendChild(mensagemDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
      }