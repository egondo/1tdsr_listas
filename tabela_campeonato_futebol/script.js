const botao = document.querySelector("#botao")

botao.addEventListener("click", () => {
    console.log("teste")
    fetch("http://127.0.0.1:5000/times").
        then(json => json.data).
        then(console.log(json))
})
