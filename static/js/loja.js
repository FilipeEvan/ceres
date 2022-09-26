// scroll horizontal de produtos

let currentScrollPosition = 0;
let scrollAmount = 320;

const sCont = document.querySelector("#cards-container");
const hScroll = document.querySelector(".scroll-horizontal");

const botaoEsquerdo = document.querySelector("#botaoEsquerdo");
const botaoDireito = document.querySelector("#botaoDireito");

botaoEsquerdo.style.opacity = "0";

let maxScroll = -sCont.offsetWidth + hScroll.offsetWidth;


function scrollHorizontal(valor) {
    currentScrollPosition += (valor * scrollAmount);

    if(currentScrollPosition >= 0) {
        currentScrollPosition = 0;
        botaoEsquerdo.style.opacity = "0";
    }else {
        botaoEsquerdo.style.opacity = "1";
    }

    if(currentScrollPosition <= maxScroll){
        currentScrollPosition = maxScroll;
        botaoDireito.style.opacity = "0";
    }else {
        botaoDireito.style.opacity = "1";
    }

    sCont.style.left = currentScrollPosition + "px";
}

let siteAtual = window.location.href;
siteAtual = siteAtual.substr(0, siteAtual.indexOf('/', 8))

function clearViewProduct(){
    document.getElementById('modalName').value = '';
    document.getElementById('modalDescription').value = '';
    document.getElementById('modalCategory').value = '';
    document.getElementById('modalQuantity').value = '';
    document.getElementById('modalPrice').value = '';
}

function viewProduct(id) {
    fetch(`${siteAtual}/product/search/${id}`)
    .then((response) => response.json())
    .then((data) => {
        if (data.id != null) {
            document.getElementById('modalImage').src = data.image
            console.log(data.image)

            document.getElementById('modalName').textContent = data.name;
            document.getElementById('modalDescription').textContent = data.description;
            document.getElementById('modalCategory').textContent = data.category;
            document.getElementById('modalQuantity').textContent = data.quantity;

            space = data.quantity.indexOf(' ')
            unity = data.quantity.slice(space + 1)

            document.getElementById('modalPrice').textContent = `R$ ${data.price} por ${unity}`;
        } else {
            alert('Produto não encontrado')
            clearViewProduct()
        }
    });
}

