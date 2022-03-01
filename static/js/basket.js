window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target = event.target;
        console.log(target)
        let basketID = target.name
        let basketQuantity = target.value
        $.ajax({
            url: '/baskets/basket-edit/' + basketID + '/' + basketQuantity + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })
}

window.onload = function () {
    $('.product_list').on('click', 'input[type="add"]', function () {
        let target = event.target
        console.log(target)
        let productID = target.name
        $.ajax({
            url:'/baskets/basket-add/' + productID + '/',
            success: function (data) {
                $('.product_list').html(data.result)
            }
        })
    })
}