
$(function(){
        /* Start DOM */
        var input = document.getElementById("order_number");
        input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            document.getElementById("btnShow").click();
        }
        });

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
                    url: 'http://127.0.0.1:8000/track',
                    method: "POST",
                    data: {'order_code':order_code},
                    success: function set_tracking_code(data){
                        if (data.tracking_number){
                            $('.frame2').append(`
                                <small>کد رهگیری مرسوله پستی شما:</small>
                                <strong><b>${data.tracking_number}</strong><hr>
                                <div class="screenshot-loader"><div>
                                `)
                                $('.screenshot-loader').append(`<p>در حال دریافت اطلاعات مرسوله از سامانه ملی رهگیری پست</p>
                                    <div class="spinner-border text-primary" role="status">
                                </div>`)
                                // start ajax
                            $.ajax({
                                url: "http://127.0.0.1:8000/take_shot",
                                method: "POST",
                                data: {'tracking_code': data.tracking_number},
                                success: function set_shot(response){
                                    result = response.result
                                    img = result.img
                                    $('html').css('height', 'auto');
                                    $('.screenshot-loader').html(`
                                        <div class="card flex">
                                        <img src="${img}" class="card-img" alt="screen shot">
                                        <div class="card-body">
                                            <h5 class="card-title">نتیجه رهگیری مرسوله پستی شما</h5>
                                            <div class="d-grid gap-2">
                                            <a type="button" href="${img}" target="_blank" class="btn btn-success">مشاهده و دانلود</a>
                                            </div>
                                        </div>
                                        </div>
                                        `)
                                },
                            }) //end ajax
                        }else{
                            $('.frame2').append(`<hr>
                                <b><small>وضعیت سفارش:</small>
                                <small>تاخیر شرکت ملی پست در اراؽه بارکد مرسوله</small>
                                <strong><b>سفارش شما هم اکنون در روند ارسال می باشد. کد رهگیری مرسوله عموما ظرف مدت (یک الی دو روز کاری پس از ثبت سفارش) برای شما و از سمت ما پیامک خواهد شد</strong><hr>
                                <strong>علت وقفه یک/دو روزه کاری در ارسال بارکد مرسولات:</strong>
                                <p>توجه داشته باشید که تمام بسته های پستی پس از ارسال و تولید بارکد ۱۶ یا ۲۴ رقمی مرسوله و قبل از رسیدن به اولین مرکز مبادلاتی پستی در سامانه رهگیری پستی فاقد اعتبار می باشند.</p>
                                <small>.صمیمانه از شما برای انتخاب بهترین ها تشکر میکنیم.</small>
                                <div class="screenshot-loader"><div>
                                `)
                        }
                    }
                })// end ajax
            }

            // set order content
            function set_order_content(order, order_code){
                $('.tracking-card').html(`
                <header>
                    <div class="container d-flex justify-content-center mt-3">
                        <a href="https://123kif.com" target="_blank"><img src="https://123kif.com/wp-content/uploads/2020/07/123-logo-1.webp" alt="123KIF Icon" width="200" height="auto" class="img-icon"></a>
                    </div>
                    <p><strong>شماره سفارش: </strong>${order_code}</p>
                    </header>
                    <div class="frame2">
                    <strong><h5>${order.full_name}</strong></h5>
                    <p><strong>وضعیت سفارش: </strong>${order.status}</p><hr>
                    <p><strong>آدرس کامل :</strong> ${order.full_address}</p>
                    </div>
                    <p><strong>شیوه ارسال : </strong>${order.shipping_method}</p>
                    <p><strong>هزینه حمل و نقل : </strong>${order.shipping_total}</p>
                    <p>پرداخت با: </strong>${order.payment_method_title}<strong></p>
                    <p>جمع کل فاکتور: <strong>${order.total}<strong></p>
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
    3027593