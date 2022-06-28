"use strict";

window.onload = function () {
    console.log('Дом загружен');
    $('.basket_record').on('change', 'input[type="number"]', function (event) {
        let basketItemQuantity = event.target.value;
        let basketItemPk = event.target.name;
        console.log(basketItemQuantity, basketItemPk);
        $.ajax({
            url: '/basket/update/' + basketItemPk + '/' + basketItemQuantity + '/',
            success: function (data) {
                if (data.status) {
                    $('.basket_summary').html(data.basket_summary);
                }
            }
        })
    })
}