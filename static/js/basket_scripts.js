"use strict";

window.onload = function () {
    console.log('Дом загружен')
    $('.basket_record').on('change', 'input[type="number"]', function (event) {
        let quantity = event.target.value
        let productPk = event.target.name
        console.log(quantity, productPk)
    })
}