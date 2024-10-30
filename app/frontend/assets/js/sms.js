
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
        order_code = $('.order_code').val()
        full_name = $('.full_name').val()
        tracking_code = $('.tracking_code').val()
        phone_number = $('.phone_number').val()
        
        send_input(
            order_code,
            full_name,
            tracking_code,
            phone_number
        )
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
    function send_input(order_code, full_name, tracking_code, phone_number){
        if (order_code && full_name && tracking_code && phone_number){
            loader_power('show')
            $('.loading_text').html(`
                <h3> در حال دریافت اطلاعات </h3><hr>
                <h6> Test </h6>
                `)
            // start ajax request
            $.ajax({
                url: 'http://127.0.0.1:8000/upload_code/new_code',
                method: "POST",
                data: {
                    'order_code': order_code,
                    'full_name':full_name,
                    'tracking_code': tracking_code,
                    'phone_number':phone_number
                },
                success: function(data){
                    sweet_alert(
                        'success',
                        `
                        سفارش ${order_code}به نام مشتری ${full_name}و با کد رهگیری ${tracking_code}برای شماره تماس ${phone_number}ثبت شد.
                        `
                    )
                    loader_power('hide')
                },
                error: function(data){
                    sweet_alert(
                        'error',
                        `
                        خطای غیر منتظره ای رخ داده
                        لطفا به مدیر سیستم اطلاع رسانی نمایید
                        `
                    )
                    loader_power('hide')
                }
            })
            // end ajax request
        }else{
            sweet_alert('info', 'تمام فیلد ها را پر کنید')
        }
    }

    // function sa for Sweet Alert Swal.fire()
    function sweet_alert(icon, text){
        Swal.fire({
            title: text,
            icon: icon,
          });
    }
    /* end DOM */
})
