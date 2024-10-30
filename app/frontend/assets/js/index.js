
$(function(){
        /* Start DOM */
        // Loader dom action
        $(window).on("load", function() {
            // Hide the loader
            loader_power('show')
            $("#loader").fadeOut("slow", function() {
                loader_power('hide')
            });
        });
        
        // btnshow DOM click
        $(".btn-show").on("click", function() {
            // Toggle the visibility of the additional content
            order_code = $('.order-input').val()
            send_input(order_code)
        });
        
        // Show_Hide loader
        function loader_power(option){
            if (option == "show"){
                $(".tracking-card").hide();
                $(".loader").fadeToggle("slow");
                $(".loading_text").show()
            }else{
                $(".tracking-card").fadeToggle("slow");
                $(".loader").hide();
                $(".loading_text").hide()
            }
        }
        // function send_input for send ajax request to server
        function send_input(order_code){
            if (order_code){
                loader_power('show')
                $('.loading_text').html(`
                    <h3> در حال دریافت اطلاعات </h3><hr>
                    <h6>سامانه هوشمند رهگیری مرسولات پستی</h6>
                    `)
                    // start ajax request
                    $.ajax({
                        url: 'http://127.0.0.1:8000/report',
                        method: "POST",
                        data: {
                            'order_code': order_code
                        },
                        success: function(order){
                            loader_power('hide')
                            set_order_content(order, order_code)
                        },
                        error: function(data){
                            console.log(data)
                            loader_power('hide')
                        }
                    })
                    // end ajax request
                }else{
                    sweet_alert('info', 'شماره سفارش خود را وارد نمایید')
                }
            }

            function init_table(products){
                $('.tracking-card').append(`
                    <div class="table-container d-flex">
                        <table>
                            <thead>
                                <tr>
                                    <th>نام محصول</th>
                                    <th>رنگ</th>
                                    <th>تعداد</th>
                                </tr>
                            </thead>
                            <tbody class="product_table">
                            </tbody>
                        </table>
                    </div>
                `);
                products.forEach((product, index) => {
                    $('.product_table').append(`
                        <tr>
                            <td>${product.name}</td>
                            <td>${product.color}</td>
                            <td>${product.qty}</td>
                        </tr>
                        `)
                });
            }
            // This function send ajax request to tracking post code for camplated orders
            function tracking_post_number(order_code){
                //  start ajax
                $.ajax({
                    url: '',
                })// end ajax
            }
    
            // set order content
            function set_order_content(order, order_code){
                $('.tracking-card').html(`
                <header>
                    <div class="container d-flex justify-content-center mt-3">
                        <img src="https://123kif.com/wp-content/uploads/2020/07/123-logo-1.webp" alt="123KIF Icon" width="200" height="auto" class="img-icon">
                    </div><hr>
                    <h4><strong>${order.full_name}</strong></h4>
                    <p><strong>شماره سفارش: </strong>${order_code}</p>
                    <p><strong>وضعیت سفارش: </strong>${order.status}</p><hr>
                    <p><strong>پرداخت با: </strong>${order.payment_method_title}</p>
                    </header>
                    <div class="frame2">
                    <p><strong>شیوه ارسال : </strong>${order.shipping_method}</p>
                    <p><strong>هزینه حمل و نقل : </strong>${order.shipping_total}</p>
                    <p><strong>آدرس کامل :</strong> ${order.full_address}</p>
                    </div>
                    <p>مجموع پرداختی: <strong>${order.total}<strong></p>
                    `)
                    
                let products = order.products
                if (order.status == 'تکمیل پردازش و خروج از انبار های ۱۲۳ کیف'){
                    init_table(products)
                    // send ajax request to tracking post code for camplated orders
                    tracking_post_number(order_code)
                }else if (order.status == 'در حال پردازش سفارش'){
                    init_table(products)
                }else if (order.status == 'لغو شده'){
                    init_table(products)
                }
                
            } // end fucn
            
            // function sa for Sweet Alert Swal.fire()
            function sweet_alert(icon, text){
                Swal.fire({
                    title: text,
                    icon: icon,
                });
        }
        /* end DOM */
    })
