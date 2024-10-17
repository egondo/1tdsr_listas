const botao = document.querySelector("#botao")
const cad = document.querySelector("#cadastra")

cad.addEventListener("click", () => {
    casa = document.querySelector('[name="casa"]')
    pl_casa = document.querySelector('[name="placar_casa"]')
    visi = document.querySelector('[name="visi"]')
    pl_visi = document.querySelector('[name="placar_visi"]')
    json_dado = {casa: casa.value, visi: visi.value, gc: parseInt(pl_casa.value), gv: parseInt(pl_visi.value), rodada: 3}

    fetch("http://127.0.0.1:5000/partidas", 
        {
            method: "POST",
            body: JSON.stringify(json_dado),
            headers: {"Content-Type": "application/json"}
        })
            .then(response => response.json())
            .then(data => console.log(data))
})


botao.addEventListener("click", () => {
    console.log("teste")
    fetch("http://127.0.0.1:5000/times")
        .then(response => response.json())
        .then(data => {
            dados = JSON.stringify(data)
            alert(dados)
            tab = "<table>"
            data.forEach(function(element){
                //console.log(element.nome);
                //alert(element.nome)
                tab = tab + "<tr><td>" + element.nome + "<td>" + element.pontos + "<td>" + element.jogos 
            });
            tab = tab + "</table>"

            div = document.querySelector("#tab")
            div.innerHTML = tab
        })
})
