
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
                    <h6> Test </h6>
                    `)
                // start ajax request
                $.ajax({
                    url: 'http://127.0.0.1:8000/report',
                    method: "POST",
                    data: {
                        'order_code': order_code
                    },
                    success: function(data){
                        alert(data)
                        loader_power('hide')
                    },
                    error: function(data){
                        alert(data)
                        loader_power('hide')
                    }
                })
                // end ajax request
            }else{
                sweet_alert('info', 'شماره سفارش خود را وارد نمایید')
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
