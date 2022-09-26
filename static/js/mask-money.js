function maskMoney() {
    element = document.getElementById('cadastroPrecoProduto');
    price = element.value;

    price = price.replace(/-?\D/g, '');
    price = price.replace(/(\d{1,2})$/, ',$1');
    price = price.replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.');

    element.value = price
}