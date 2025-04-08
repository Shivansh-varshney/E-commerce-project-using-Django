$("#reviewform").submit(function (element) {
    element.preventDefault()

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),

        success: function (response) {

            if (response.bool == true) {
                $("#review-res").html("Review Added successfully!!");
                $(".hide-review-form").hide();

                let _html = '<div class="mb-2 border border-warning pt-3 px-3">'
                _html += '<span><strong>' + response.context.user
                for (var i = 1; i <= response.context.rating; i++) {
                    _html += "⭐"
                }
                _html += '</span></strong><p>'
                _html += response.context.review + '<br /><small class="text-danger">' + response.context.date + '</small>'
                _html += '</p>'
                _html += '</div>'

                $(".review-list").prepend(_html)

            }
        }
    })
})


// add to cart functionality
$(".button-add-to-cart").on("click", function () {

    let this_val = $(this)
    let index = this_val.attr("data-index")

    let quantity = $("#product-quantity").val();
    let product_id = $(".product-id-" + index).val();
    let product_title = $(".product-title-" + index).val();
    let product_price = $(".product-price-" + index).text();


    $.ajax(
        {
            url: "/cart/add_to_cart",
            data: {
                'id': product_id,
                'quantity': quantity,
                'title': product_title,
                'price': product_price
            },
            dataType: 'json',

            success: function (response) {

                if (response.bool == true) {
                    this_val.html("<a><i class='fa-solid fa-check'></i></a>");
                }
                else if (response.bool == false) {
                    this_val.hide()
                    $('#response-data-' + product_id).html("Please Login First");
                }
            }
        }
    )
})

// delete product from cart
$(document).on("click", '.delete-product', function () {

    let this_val = $(this)
    let product_id = this_val.attr('data-index');

    $.ajax(
        {
            url: "/cart/delete_from_cart",
            data: {
                "id": product_id
            },
            dataType: "json",
            beforeSend: function () {
                this_val.hide()
            },
            success: function (response) {
                this_val.show()
                $("#cart-list").html(response.data)
            }
        }
    )

})


// update product in cart
$(document).on("click", '.update-cart', function () {

    let this_val = $(this)
    let product_id = this_val.attr('data-index');
    let quantity = $("#product-quantity-" + product_id).val()

    $.ajax(
        {
            url: "/cart/update_cart",
            data: {
                "id": product_id,
                "quantity": quantity
            },
            dataType: "json",
            beforeSend: function () {
                this_val.hide()
            },
            success: function (response) {
                this_val.show()
                $("#cart-list").html(response.data)
            }
        }
    )

})


// delete address
$(document).on("click", '.delete-address', function () {

    let this_val = $(this)
    let address_id = this_val.attr('data-index');

    $.ajax(
        {
            url: "/user/delete_address/",
            data: {
                "aid": address_id
            },
            dataType: "json",
            beforeSend: function () {
                this_val.hide()
            },
            success: function (response) {
                this_val.show()
                $("#addresslist").html(response.data)
            }
        }
    )

})

// make default address
$(document).on("click", '.default-address', function () {

    let this_val = $(this)
    let address_id = this_val.attr('data-index');

    $.ajax(
        {
            url: "/user/make_default/",
            data: {
                "aid": address_id
            },
            dataType: "json",
            beforeSend: function () {
                this_val.hide()
            },
            success: function (response) {
                this_val.show()
                $("#addresslist").html(response.data)
            }
        }
    )

})

// change shipping address
$(document).on("click", '.change-address', function () {

    let this_val = $(this)
    let address_id = this_val.attr('data-index');

    $.ajax(
        {
            url: "/payments/shipping_address/",
            data: {
                "aid": address_id
            },
            dataType: "json",
            success: function (response) {
                $(".shipping-address").html(response.data)
            }
        }
    )

})

// edit saved address
$(document).on("click", '.edit-address', function () {

    let this_val = $(this)
    let address_id = this_val.attr('data-index');


    $.ajax(
        {
            url: "/user/get_address/",
            data: {
                "aid": address_id
            },
            dataType: "json",
            success: function (response) {
                $(".address").html(response.data)
            }
        }
    )

})

$(document).on("click", '.delete-vendor-product', function () {

    let this_val = $(this)
    let product_id = this_val.attr('data-prd-id');


    $.ajax(
        {
            url: "/vendor/delete_product/",
            data: {
                "pid": product_id
            },
            dataType: "json",
            success: function (response) {
                $(".products").html(response.data)
            }
        }
    )

})

$(document).on("click", '.vendor-weekly-earnings', function () {

    $.ajax(
        {
            url: "/vendor/weekly/",
            dataType: "json",
            success: function (response) {
                $(".earnings").html(response.data)
            }
        }
    )

})

$(document).on("click", '.vendor-monthly-earnings', function () {

    $.ajax(
        {
            url: "/vendor/monthly/",
            dataType: "json",
            success: function (response) {
                $(".earnings").html(response.data)
            }
        }
    )

})

$(document).on("click", '.vendor-daily-earnings', function () {

    $.ajax(
        {
            url: "/vendor/daily/",
            dataType: "json",
            success: function (response) {
                $(".earnings").html(response.data)
            }
        }
    )

})


$(document).on("click", '.show-product-reviews', function () {

    let this_val = $(this)
    let product_id = this_val.attr('data-index');

    $.ajax(
        {
            url: "/vendor/vendor_product_reviews/",
            data: {
                "prd_id": product_id
            },
            dataType: "json",
            success: function (response) {
                this_val.show()
                $(".productreview-" + product_id).html(response.data)
            }
        }
    )

})

$(document).on("click", '.close-product-reviews', function () {

    let this_val = $(this)
    let product_id = this_val.attr('data-index');

    $(".productreview-" + product_id).html('')

})