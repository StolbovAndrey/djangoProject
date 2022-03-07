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