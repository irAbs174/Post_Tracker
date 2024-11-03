$(function(){
    // Loader action on window load
    $(window).on("load", function() {
        loader_power('show');
        $("#loader").fadeOut("slow", function() {
            loader_power('hide');
        });
    });
    
    // Toggle visibility on button click
    $(".btn-show").on("click", function() {
        const order_code = $('.order-input').val();
        send_input(order_code);
    });

    // Panel action for sending codes
    $(".send-codes-panel").on("click", function() {
        $('.frame2').html(`
            <p><strong>شماره سفارش:</strong></p>
        `);
        $('<input>', {
            type: 'text',
            class: 'order-send order-input-send',
            placeholder: 'کد سفارش مشتری گیرنده'
        }).appendTo('.frame2');
        
        $('.frame2').append(`
            <p><strong>نام و نام خانوادگی:</strong></p>
        `);
        $('<input>', {
            type: 'text',
            class: 'order-send full_name-send',
            placeholder: 'نام کامل گیرنده پیامک | مثل: یاور یاوری'
        }).appendTo('.frame2');
        
        $('.frame2').append(`
            <p><strong>کد رهگیری مرسوله پستی:</strong></p>
        `);
        $('<input>', {
            type: 'text',
            class: 'order-send tracking_code-send',
            placeholder: 'بارکد ۱۶ الی ۲۴ رقمی پستی'
        }).appendTo('.frame2');
        
        $('.frame2').append(`
            <p><strong>شماره تماس:</strong></p>
        `);
        $('<input>', {
            type: 'text',
            class: 'order-send phone_number-send',
            placeholder: 'شماره تماس گیرنده پیامک'
        }).appendTo('.frame2');
        
        $('<button>', {
            class: 'btn-send-code',
            text: 'ثبت کد مرسوله',
            click: function() {
                let order_code= $('.order-input-send').val()
                let full_name = $('.full_name-send').val()
                let tracking_code = $('.tracking_code-send').val()
                let phone_number = $('.phone_number-send').val()
                loader_power('show')
                $.ajax({
                    url: 'new_code',
                    method: "POST",
                    data: {
                        'order_code': order_code,
                        'full_name': full_name,
                        'tracking_code': tracking_code,
                        'phone_number': phone_number,

                    },
                    success: function(order) {
                            sweet_alert('success', 'کد با موفقیت ثبت و ارسال شد');
                            loader_power('hide');
                        },
                    error: function() {
                        sweet_alert('error', "خطا: ارتباط با سرور برقرار نیست");
                        loader_power('hide');
                    }
                });
                
                    
                    
                    
                    

            }
        }).appendTo('.frame2');
    });
        
    // Show/Hide loader
    function loader_power(option) {
        if (option === "show") {
            $(".tracking-card").hide();
            $(".loader").fadeIn("slow");
            $(".loading_text").show();
        } else {
            $(".tracking-card").fadeIn("slow");
            $(".loader").hide();
            $(".loading_text").hide();
        }
    }

    // AJAX request function
    function send_input(order_code) {
        if (order_code) {
            loader_power('show');
            $('.loading_text').html(`
                <h3> در حال دریافت اطلاعات </h3><hr>
                <h6>سامانه هوشمند رهگیری مرسولات پستی</h6>
            `);
            $.ajax({
                url: 'report',
                method: "POST",
                data: {'order_code': order_code},
                success: function(order) {
                    if (order.full_name) {
                        set_order_content(order, order_code);
                    } else {
                        sweet_alert('error', 'شماره سفارش معتبر نیست');
                    }
                    loader_power('hide');
                },
                error: function() {
                    sweet_alert('error', "Error during received report data");
                    loader_power('hide');
                }
            });
        } else {
            sweet_alert('info', 'شماره سفارش خود را وارد نمایید');
        }
    }

    function init_table(products) {
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
        products.forEach((product) => {
            $('.product_table').append(`
                <tr>
                    <td>${product.name}</td>
                    <td>${product.color}</td>
                    <td>${product.qty}</td>
                </tr>
            `);
        });
    }

    // Tracking post number function
    function tracking_post_number(order_code) {
        $.ajax({
            url: 'track',
            method: "POST",
            data: {'order_code': order_code},
            success: function(data) {
                if (data.tracking_number) {
                    $('.frame2').append(`
                        <small>کد رهگیری مرسوله پستی شما:</small>
                        <strong><b>${data.tracking_number}</strong><hr>
                        <div class="screenshot-loader"><div>
                    `);
                    $('.screenshot-loader').append(`
                        <p>در حال دریافت اطلاعات مرسوله از سامانه ملی رهگیری پست</p>
                        <div class="spinner-border text-primary" role="status"></div>
                    `);
                    $.ajax({
                        url: "take_shot",
                        method: "POST",
                        data: {'tracking_code': data.tracking_number},
                        success: function(response) {
                            const { img } = response.result;
                            const path = window.location.pathname;
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
                            `);
                        },
                    });
                } else {
                    $('.frame2').append(`
                        <hr>
                        <b><small>وضعیت سفارش:</small>
                        <small>تاخیر شرکت ملی پست در ارائؑه بارکد مرسوله</small>
                        <strong><b>سفارش شما هم اکنون در روند ارسال می باشد...</strong><hr>
                        <strong>علت وقفه یک/دو روزه کاری در ارسال بارکد مرسولات:</strong>
                        <p>توجه داشته باشید که تمام بسته های پستی...</p>
                        <small>.صمیمانه از شما برای انتخاب بهترین ها تشکر میکنیم.</small>
                        <div class="screenshot-loader"><div>
                    `);
                }
            }
        });
    }

    // Set order content function
    function set_order_content(order, order_code) {
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
            <p>پرداخت با: <strong>${order.payment_method_title}</strong></p>
            <p>جمع کل فاکتور: <strong>${order.total}</strong></p>
        `);
        
        if (['تکمیل پردازش و خروج از انبار های ۱۲۳ کیف', 'در حال پردازش سفارش', 'لغو شده'].includes(order.status)) {
            init_table(order.products);
            if (order.status === 'تکمیل پردازش و خروج از انبار های ۱۲۳ کیف') {
                tracking_post_number(order_code);
            }
        }
    }

    // Sweet alert function
    function sweet_alert(icon, text) {
        Swal.fire({
            title: text,
            icon: icon,
        });
    }
});
