data = WC_API.get(f'orders/{order_code}').json()

# Success data examples
data = {'id': 3043838, 'parent_id': 0, 'status': 'completed', 'currency': 'IRT', 'version': '9.3.3', 'prices_include_tax': True, 'date_created': '2024-10-27T09:26:32', 'date_modified': '2024-10-28T16:30:26', 'discount_total': '0', 'discount_tax': '0', 'shipping_total': '0', 'shipping_tax': '0', 'cart_tax': '352182', 'total': '3874000', 'total_tax': '352182', 'customer_id': 2277539, 'order_key': 'wc_order_0Mzt9K6ehdqBD', 'billing': {'first_name': 'مهسا', 'last_name': 'آریا', 'company': '', 'address_1': 'تهرانپارس اتوبان باقری بلوار اردیبهشت شمالی 198 غربی یا شعبانی پلاک 26', 'address_2': 'واحد 4', 'city': 'تهران', 'state': 'THR', 'postcode': '1686915513', 'country': 'IR', 'email': '', 'phone': '09126233201'}, 'shipping': {'first_name': 'مهسا', 'last_name': 'آریا', 'company': '', 'address_1': 'تهرانپارس اتوبان باقری بلوار اردیبهشت شمالی 198 غربی یا شعبانی پلاک 26', 'address_2': 'واحد 4', 'city': 'تهران', 'state': 'THR', 'postcode': '1686915513', 'country': 'IR', 'phone': ''}, 'payment_method': 'WC_Gateway_SnappPay', 'payment_method_title': 'پرداخت اقساطیِ اسنپ پی', 'transaction_id': '', 'customer_ip_address': '178.252.129.210', 'customer_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36', 'created_via': 'checkout', 'customer_note': '', 'date_completed': '2024-10-28T09:31:37', 'date_paid': '2024-10-27T09:28:28', 'cart_hash': 'e4dc95baea00a234dcce9785834e3232', 'number': '3043838', 'meta_data': [{'id': 8398221, 'key': '_billing_melly_code', 'value': '0070099693'}, {'id': 8398222, 'key': '_billing_receiving_invoice', 'value': '1'}, {'id': 8398223, 'key': 'is_vat_exempt', 'value': 'no'}, {'id': 8398224, 'key': '_force_enable_buyer', 'value': 'yes'}, {'id': 8398225, 'key': '_allow_buyer_select_status', 'value': 'no'}, {'id': 8398226, 'key': '_buyer_sms_notify', 'value': 'yes'}, {'id': 8398227, 'key': '_awcfe_order_meta_key', 'value': {'billing': [{'type': 'text', 'meta_id': False, 'name': 'billing_melly_code', 'elementId': 'text-2802267474', 'label': 'کد ملی', 'value': '0070099693', 'priority': '40', 'col': 6, 'show_in_email': True, 'show_in_order_page': True, 'options': False}, {'type': 'text', 'meta_id': False, 'name': 'billing_email', 'elementId': 'text-2892267831', 'label': 'ایمیل', 'value': '', 'priority': '130', 'col': 6, 'show_in_email': True, 'show_in_order_page': True, 'options': False}], 'account': [], 'order': []}}, {'id': 8398228, 'key': '_wc_order_attribution_source_type', 'value': 'typein'}, {'id': 8398229, 'key': '_wc_order_attribution_utm_source', 'value': '(direct)'}, {'id': 8398230, 'key': '_wc_order_attribution_session_entry', 'value': 'https://123kif.com/backpack/mountain-travel-backpack/'}, {'id': 8398231, 'key': '_wc_order_attribution_session_start_time', 'value': '2024-10-27 04:47:12'}, {'id': 8398232, 'key': '_wc_order_attribution_session_pages', 'value': '15'}, {'id': 8398233, 'key': '_wc_order_attribution_session_count', 'value': '1'}, {'id': 8398234, 'key': '_wc_order_attribution_user_agent', 'value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}, {'id': 8398235, 'key': '_wc_order_attribution_device_type', 'value': 'Desktop'}, {'id': 8398236, 'key': '_transactionId', 'value': '1730008608-3043838'}, {'id': 8398237, 'key': '_order_spp_token', 'value': '5764dcf5-4e17-45a1-95ac-255a26e620ec'}, {'id': 8398238, 'key': '_paymentToken', 'value': '5764dcf5-4e17-45a1-95ac-255a26e620ec'}, {'id': 8398241, 'key': 'order_spp_status', 'value': 'SETTLE'}, {'id': 8398244, 'key': 'wip_cart_discount', 'value': {'3020742': 3620000, '3027612': 264000}}, {'id': 8398245, 'key': 'wip_cart_price', 'value': {'3020742': {'regular_price': '7219000', 'sale_price': '3599000'}, '3027612': {'regular_price': '539000', 'sale_price': '275000'}}}, {'id': 8398246, 'key': 'referral_done', 'value': 'yes'}, {'id': 8398716, 'key': 'tracking_column', 'value': ''}, {'id': 8398717, 'key': 'tracking_type', 'value': 'none'}, {'id': 8398718, 'key': '_assign_to_storage', 'value': '1403/8/6'}, {'id': 8398719, 'key': '_assign_to_warehouse_packing_status', 'value': 'yes'}, {'id': 8398720, 'key': '_assign_to_accounting', 'value': 'yes'}], 'line_items': [{'id': 95652, 'name': 'کوله پشتی کوه و سفر پکینیو مدل PEKYNEW-PKN200 (70+10 LITER) - فیروزه ای', 'product_id': 3017688, 'variation_id': 3020742, 'quantity': 1, 'tax_class': '', 'subtotal': '3271818', 'subtotal_tax': '327182', 'total': '3271818', 'total_tax': '327182', 'taxes': [{'id': 1, 'total': '327181.818182', 'subtotal': '327181.818182'}], 'meta_data': [{'id': 726565, 'key': 'pa_color', 'value': 'firozei', 'display_key': 'رنگ', 'display_value': 'فیروزه ای'}, {'id': 726588, 'key': '_reduced_stock', 'value': '1', 'display_key': '_reduced_stock', 'display_value': '1'}], 'sku': '', 'price': 3271818.181818, 'image': {'id': 3020735, 'src': 'https://123kif.com/wp-content/uploads/2024/05/PEKYNEW-200-6.png'}, 'parent_name': 'کوله پشتی کوه و سفر پکینیو مدل PEKYNEW-PKN200 (70+10 LITER)'}, {'id': 95653, 'name': 'کیف پیک نیک مسافرتی فوروارد مدل FCLT44102 - صورتی', 'product_id': 3027603, 'variation_id': 3027612, 'quantity': 1, 'tax_class': '', 'subtotal': '250000', 'subtotal_tax': '25000', 'total': '250000', 'total_tax': '25000', 'taxes': [{'id': 1, 'total': '25000', 'subtotal': '25000'}], 'meta_data': [{'id': 726575, 'key': 'pa_color', 'value': 'sourati', 'display_key': 'رنگ', 'display_value': 'صورتی'}, {'id': 726589, 'key': '_reduced_stock', 'value': '1', 'display_key': '_reduced_stock', 'display_value': '1'}], 'sku': '', 'price': 250000, 'image': {'id': 3027633, 'src': 'https://123kif.com/wp-content/uploads/2024/07/FCLT44102-14.webp'}, 'parent_name': 'کیف پیک نیک مسافرتی فوروارد مدل FCLT44102'}], 'tax_lines': [{'id': 95655, 'rate_code': 'IR-مالیات بر ارزش افزوده-1', 'rate_id': 1, 'label': 'مالیات بر ارزش افزوده', 'compound': False, 'tax_total': '352182', 'shipping_tax_total': '0', 'rate_percent': 10, 'meta_data': []}], 'shipping_lines': [{'id': 95654, 'method_title': 'ارسال با پست ویژه - تبریک! ارسال شما رایگان می باشد.', 'method_id': 'flat_rate', 'instance_id': '20', 'total': '0', 'total_tax': '0', 'taxes': [{'id': 1, 'total': '', 'subtotal': ''}], 'meta_data': [{'id': 726581, 'key': 'موارد', 'value': 'کوله پشتی کوه و سفر پکینیو مدل PEKYNEW-PKN200 (70+10 LITER) - فیروزه ای &times; 1, کیف پیک نیک مسافرتی فوروارد مدل FCLT44102 - صورتی &times; 1', 'display_key': 'موارد', 'display_value': 'کوله پشتی کوه و سفر پکینیو مدل PEKYNEW-PKN200 (70+10 LITER) - فیروزه ای &times; 1, کیف پیک نیک مسافرتی فوروارد مدل FCLT44102 - صورتی &times; 1'}]}], 'fee_lines': [], 'coupon_lines': [], 'refunds': [], 'payment_url': 'https://123kif.com/checkout/order-pay/3043838/?pay_for_order=true&key=wc_order_0Mzt9K6ehdqBD', 'is_editable': False, 'needs_payment': False, 'needs_processing': True, 'date_created_gmt': '2024-10-27T05:56:32', 'date_modified_gmt': '2024-10-28T13:00:26', 'date_completed_gmt': '2024-10-28T06:01:37', 'date_paid_gmt': '2024-10-27T05:58:28', 'currency_symbol': 'تومان', '_links': {'self': [{'href': 'https://123kif.com/wp-json/wc/v3/orders/3043838'}], 'collection': [{'href': 'https://123kif.com/wp-json/wc/v3/orders'}], 'customer': [{'href': 'https://123kif.com/wp-json/wc/v3/customers/2277539'}]}}
data = {'id': 3043964, 'parent_id': 0, 'status': 'processing', 'currency': 'IRT', 'version': '9.3.3', 'prices_include_tax': True, 'date_created': '2024-10-30T02:48:34', 'date_modified': '2024-10-30T02:51:26', 'discount_total': '0', 'discount_tax': '0', 'shipping_total': '200000', 'shipping_tax': '0', 'cart_tax': '39000', 'total': '629000', 'total_tax': '39000', 'customer_id': 2277607, 'order_key': 'wc_order_TI9hOmclzAqJr', 'billing': {'first_name': 'ایرن', 'last_name': 'حسنلو', 'company': '', 'address_1': 'تهران پارس کنار گذر زین الدین نبش خیری ۱۲۹', 'address_2': 'پلاک ۱۳۰ واحد ۴', 'city': 'تهران', 'state': 'THR', 'postcode': '1503195', 'country': 'IR', 'email': '', 'phone': '09396018213'}, 'shipping': {'first_name': 'ایرن', 'last_name': 'حسنلو', 'company': '', 'address_1': 'تهران پارس کنار گذر زین الدین نبش خیری ۱۲۹', 'address_2': 'پلاک ۱۳۰ واحد ۴', 'city': 'تهران', 'state': 'THR', 'postcode': '1503195', 'country': 'IR', 'phone': ''}, 'payment_method': 'WC_Gateway_SnappPay', 'payment_method_title': 'پرداخت اقساطیِ اسنپ پی', 'transaction_id': '', 'customer_ip_address': '5.113.173.31', 'customer_user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1', 'created_via': 'checkout', 'customer_note': '', 'date_completed': None, 'date_paid': '2024-10-30T02:51:26', 'cart_hash': '2e36a28621e9909e421d8602504e58e2', 'number': '3043964', 'meta_data': [{'id': 8402843, 'key': '_billing_melly_code', 'value': '0481125051'}, {'id': 8402844, 'key': '_billing_receiving_invoice', 'value': ''}, {'id': 8402846, 'key': '_force_enable_buyer', 'value': 'yes'}, {'id': 8402847, 'key': '_allow_buyer_select_status', 'value': 'no'}, {'id': 8402848, 'key': '_buyer_sms_notify', 'value': 'yes'}, {'id': 8402849, 'key': '_awcfe_order_meta_key', 'value': {'billing': [{'type': 'text', 'meta_id': False, 'name': 'billing_melly_code', 'elementId': 'text-2802267474', 'label': 'کد ملی', 'value': '0481125051', 'priority': '40', 'col': 6, 'show_in_email': True, 'show_in_order_page': True, 'options': False}, {'type': 'text', 'meta_id': False, 'name': 'billing_email', 'elementId': 'text-2892267831', 'label': 'ایمیل', 'value': '', 'priority': '130', 'col': 6, 'show_in_email': True, 'show_in_order_page': True, 'options': False}], 'account': [], 'order': []}}, {'id': 8402850, 'key': '_wc_order_attribution_source_type', 'value': 'organic'}, {'id': 8402851, 'key': '_wc_order_attribution_referrer', 'value': 'https://www.google.com/'}, {'id': 8402852, 'key': '_wc_order_attribution_utm_source', 'value': 'google'}, {'id': 8402853, 'key': '_wc_order_attribution_utm_medium', 'value': 'organic'}, {'id': 8402854, 'key': '_wc_order_attribution_session_entry', 'value': 'https://123kif.com/sack/travel-sack/'}, {'id': 8402855, 'key': '_wc_order_attribution_session_start_time', 'value': '2024-10-29 23:27:50'}, {'id': 8402856, 'key': '_wc_order_attribution_session_pages', 'value': '22'}, {'id': 8402857, 'key': '_wc_order_attribution_session_count', 'value': '1'}, {'id': 8402858, 'key': '_wc_order_attribution_user_agent', 'value': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'}, {'id': 8402859, 'key': '_wc_order_attribution_device_type', 'value': 'Mobile'}, {'id': 8402860, 'key': '_transactionId', 'value': '1730243974-3043964'}, {'id': 8402861, 'key': '_order_spp_token', 'value': '84fb35a0-034e-4e5b-97fd-0b19bcb26dd4'}, {'id': 8402862, 'key': '_paymentToken', 'value': '84fb35a0-034e-4e5b-97fd-0b19bcb26dd4'}, {'id': 8402863, 'key': 'is_vat_exempt', 'value': 'no'}, {'id': 8402864, 'key': '_wc_order_attribution_source_type', 'value': 'organic'}, {'id': 8402865, 'key': '_wc_order_attribution_referrer', 'value': 'https://www.google.com/'}, {'id': 8402866, 'key': '_wc_order_attribution_utm_source', 'value': 'google'}, {'id': 8402867, 'key': '_wc_order_attribution_utm_medium', 'value': 'organic'}, {'id': 8402868, 'key': '_wc_order_attribution_session_entry', 'value': 'https://123kif.com/sack/travel-sack/'}, {'id': 8402869, 'key': '_wc_order_attribution_session_start_time', 'value': '2024-10-29 23:27:50'}, {'id': 8402870, 'key': '_wc_order_attribution_session_pages', 'value': '24'}, {'id': 8402871, 'key': '_wc_order_attribution_session_count', 'value': '1'}, {'id': 8402872, 'key': '_wc_order_attribution_user_agent', 'value': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'}, {'id': 8402873, 'key': '_wc_order_attribution_device_type', 'value': 'Mobile'}, {'id': 8402876, 'key': 'order_spp_status', 'value': 'SETTLE'}, {'id': 8402878, 'key': 'wip_cart_discount', 'value': {'86554': 466000}}, {'id': 8402879, 'key': 'wip_cart_price', 'value': {'86554': {'regular_price': '895000', 'sale_price': '429000'}}}, {'id': 8402880, 'key': 'referral_done', 'value': 'yes'}], 'line_items': [{'id': 95876, 'name': 'کوله پشتی اسپرت مدل SPORT 5030 - ارتشی', 'product_id': 86547, 'variation_id': 86554, 'quantity': 1, 'tax_class': '', 'subtotal': '390000', 'subtotal_tax': '39000', 'total': '390000', 'total_tax': '39000', 'taxes': [{'id': 1, 'total': '39000', 'subtotal': '39000'}], 'meta_data': [{'id': 728198, 'key': 'pa_color', 'value': 'arteshi', 'display_key': 'رنگ', 'display_value': 'ارتشی'}, {'id': 728211, 'key': '_reduced_stock', 'value': '1', 'display_key': '_reduced_stock', 'display_value': '1'}], 'sku': 'کوله پشتی اسپورت کد sport 5030', 'price': 390000, 'image': {'id': 3008387, 'src': 'https://123kif.com/wp-content/uploads/2023/10/sport5030-1.webp'}, 'parent_name': 'کوله پشتی اسپرت مدل SPORT 5030'}], 'tax_lines': [{'id': 95878, 'rate_code': 'IR-مالیات بر ارزش افزوده-1', 'rate_id': 1, 'label': 'مالیات بر ارزش افزوده', 'compound': False, 'tax_total': '39000', 'shipping_tax_total': '0', 'rate_percent': 10, 'meta_data': []}], 'shipping_lines': [{'id': 95877, 'method_title': 'ارسال فوری با پیک', 'method_id': 'local_pickup', 'instance_id': '28', 'total': '200000', 'total_tax': '0', 'taxes': [], 'meta_data': [{'id': 728204, 'key': 'موارد', 'value': 'کوله پشتی اسپرت مدل SPORT 5030 - ارتشی &times; 1', 'display_key': 'موارد', 'display_value': 'کوله پشتی اسپرت مدل SPORT 5030 - ارتشی &times; 1'}]}], 'fee_lines': [], 'coupon_lines': [], 'refunds': [], 'payment_url': 'https://123kif.com/checkout/order-pay/3043964/?pay_for_order=true&key=wc_order_TI9hOmclzAqJr', 'is_editable': False, 'needs_payment': False, 'needs_processing': True, 'date_created_gmt': '2024-10-29T23:18:34', 'date_modified_gmt': '2024-10-29T23:21:26', 'date_completed_gmt': None, 'date_paid_gmt': '2024-10-29T23:21:26', 'currency_symbol': 'تومان', '_links': {'self': [{'href': 'https://123kif.com/wp-json/wc/v3/orders/3043964'}], 'collection': [{'href': 'https://123kif.com/wp-json/wc/v3/orders'}], 'customer': [{'href': 'https://123kif.com/wp-json/wc/v3/customers/2277607'}]}}
data = {'id': 3024533, 'parent_id': 0, 'status': 'pending', 'currency': 'IRT', 'version': '9.0.2', 'prices_include_tax': True, 'date_created': '2024-07-02T15:46:23', 'date_modified': '2024-07-02T15:46:47', 'discount_total': '0', 'discount_tax': '0', 'shipping_total': '0', 'shipping_tax': '0', 'cart_tax': '0', 'total': '0', 'total_tax': '0', 'customer_id': 0, 'order_key': 'wc_order_fdc2GZ1WodeLu', 'billing': {'first_name': '', 'last_name': '', 'company': '', 'address_1': '', 'address_2': '', 'city': '', 'state': '', 'postcode': '', 'country': '', 'email': '', 'phone': ''}, 'shipping': {'first_name': '', 'last_name': '', 'company': '', 'address_1': '', 'address_2': '', 'city': '', 'state': '', 'postcode': '', 'country': '', 'phone': ''}, 'payment_method': '', 'payment_method_title': '', 'transaction_id': '', 'customer_ip_address': '', 'customer_user_agent': '', 'created_via': 'admin', 'customer_note': '', 'date_completed': None, 'date_paid': None, 'cart_hash': '', 'number': '3024533', 'meta_data': [{'id': 7504949, 'key': 'tracking_column', 'value': ''}, {'id': 7504950, 'key': 'tracking_type', 'value': 'none'}, {'id': 7504964, 'key': '_assign_to_storage', 'value': ''}, {'id': 7504965, 'key': '_assign_to_warehouse_packing_status', 'value': 'no'}, {'id': 7504966, 'key': '_assign_to_accounting', 'value': 'no'}, {'id': 7504971, 'key': '_billing_receiving_invoice', 'value': ''}, {'id': 7504974, 'key': '_wc_order_attribution_source_type', 'value': 'admin'}, {'id': 7504975, 'key': '_force_enable_buyer', 'value': 'yes'}, {'id': 7504976, 'key': '_allow_buyer_select_status', 'value': 'no'}, {'id': 7504977, 'key': '_buyer_sms_notify', 'value': 'yes'}, {'id': 7504978, 'key': '_buyer_sms_status', 'value': ['processing', 'refunded']}, {'id': 7504979, 'key': 'post-tracking-code', 'value': '324300'}, {'id': 7504980, 'key': '_post-tracking-code', 'value': 'field_6669446c09bfb'}], 'line_items': [], 'tax_lines': [], 'shipping_lines': [], 'fee_lines': [], 'coupon_lines': [], 'refunds': [], 'payment_url': 'https://123kif.com/checkout/order-pay/3024533/?pay_for_order=true&key=wc_order_fdc2GZ1WodeLu', 'is_editable': True, 'needs_payment': False, 'needs_processing': False, 'date_created_gmt': '2024-07-02T11:16:23', 'date_modified_gmt': '2024-07-02T11:16:47', 'date_completed_gmt': None, 'date_paid_gmt': None, 'currency_symbol': 'تومان', '_links': {'self': [{'href': 'https://123kif.com/wp-json/wc/v3/orders/3024533'}], 'collection': [{'href': 'https://123kif.com/wp-json/wc/v3/orders'}]}}
data = {'id': 3043961, 'parent_id': 0, 'status': 'cancelled', 'currency': 'IRT', 'version': '9.3.3', 'prices_include_tax': True, 'date_created': '2024-10-29T21:34:52', 'date_modified': '2024-10-30T03:20:25', 'discount_total': '0', 'discount_tax': '0', 'shipping_total': '85000', 'shipping_tax': '0', 'cart_tax': '24455', 'total': '354000', 'total_tax': '24455', 'customer_id': 2277600, 'order_key': 'wc_order_7WI5e1pq0nk98', 'billing': {'first_name': 'عباس', 'last_name': 'فرخی', 'company': '', 'address_1': 'سه راه بروجردی مجتمع فرخی', 'address_2': 'طبقه همکف', 'city': 'فیروزآباد', 'state': 'FRS', 'postcode': '7471646403', 'country': 'IR', 'email': '', 'phone': '09176201364'}, 'shipping': {'first_name': 'عباس', 'last_name': 'فرخی', 'company': '', 'address_1': 'سه راه بروجردی مجتمع فرخی', 'address_2': 'طبقه همکف', 'city': 'فیروزآباد', 'state': 'FRS', 'postcode': '7471646403', 'country': 'IR', 'phone': ''}, 'payment_method': 'melli_pay', 'payment_method_title': 'بانک ملی', 'transaction_id': '', 'customer_ip_address': '5.214.101.121', 'customer_user_agent': 'Mozilla/5.0 (Linux; Android 10; FRL-L22; HMSCore 6.14.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/15.0.4.312 Mobile Safari/537.36', 'created_via': 'checkout', 'customer_note': '', 'date_completed': None, 'date_paid': None, 'cart_hash': '1d2c2527f9c9b62c7e32752979e2d48a', 'number': '3043961', 'meta_data': [{'id': 8402722, 'key': '_billing_melly_code', 'value': '2452138551'}, {'id': 8402723, 'key': '_billing_receiving_invoice', 'value': ''}, {'id': 8402724, 'key': 'is_vat_exempt', 'value': 'no'}, {'id': 8402725, 'key': '_force_enable_buyer', 'value': 'yes'}, {'id': 8402726, 'key': '_allow_buyer_select_status', 'value': 'no'}, {'id': 8402727, 'key': '_buyer_sms_notify', 'value': 'yes'}, {'id': 8402728, 'key': '_awcfe_order_meta_key', 'value': {'billing': [{'type': 'text', 'meta_id': False, 'name': 'billing_melly_code', 'elementId': 'text-2802267474', 'label': 'کد ملی', 'value': '2452138551', 'priority': '40', 'col': 6, 'show_in_email': True, 'show_in_order_page': True, 'options': False}, {'type': 'text', 'meta_id': False, 'name': 'billing_email', 'elementId': 'text-2892267831', 'label': 'ایمیل', 'value': '', 'priority': '130', 'col': 6, 'show_in_email': True, 'show_in_order_page': True, 'options': False}], 'account': [], 'order': []}}, {'id': 8402729, 'key': '_wc_order_attribution_source_type', 'value': 'utm'}, {'id': 8402730, 'key': '_wc_order_attribution_utm_campaign', 'value': 'PPC_result_adv'}, {'id': 8402731, 'key': '_wc_order_attribution_utm_source', 'value': 'Torob'}, {'id': 8402732, 'key': '_wc_order_attribution_utm_medium', 'value': 'PPC'}, {'id': 8402733, 'key': '_wc_order_attribution_session_entry', 'value': 'https://123kif.com/product/fclt4446-organize-box/?utm_medium=PPC&utm_source=Torob&utm_campaign=PPC_result_adv'}, {'id': 8402734, 'key': '_wc_order_attribution_session_start_time', 'value': '2024-10-29 17:21:03'}, {'id': 8402735, 'key': '_wc_order_attribution_session_pages', 'value': '3'}, {'id': 8402736, 'key': '_wc_order_attribution_session_count', 'value': '2'}, {'id': 8402737, 'key': '_wc_order_attribution_user_agent', 'value': 'Mozilla/5.0 (Linux; Android 10; FRL-L22; HMSCore 6.14.0.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 HuaweiBrowser/15.0.4.312 Mobile Safari/537.36'}, {'id': 8402738, 'key': '_wc_order_attribution_device_type', 'value': 'Mobile'}], 'line_items': [{'id': 95865, 'name': 'نظم دهنده سفری و کمد فوروارد Forward مدل FCLT4446 ORGANIZE BOX - فیروزه ای', 'product_id': 96301, 'variation_id': 96313, 'quantity': 1, 'tax_class': '', 'subtotal': '244545', 'subtotal_tax': '24455', 'total': '244545', 'total_tax': '24455', 'taxes': [{'id': 1, 'total': '24454.545455', 'subtotal': '24454.545455'}], 'meta_data': [{'id': 728112, 'key': 'pa_color', 'value': 'firozei', 'display_key': 'رنگ', 'display_value': 'فیروزه ای'}], 'sku': '1410251001491', 'price': 244545.454545, 'image': {'id': 3023944, 'src': 'https://123kif.com/wp-content/uploads/2024/01/FCLT4446-FORWARD-11.webp'}, 'parent_name': 'نظم دهنده سفری و کمد فوروارد Forward مدل FCLT4446 ORGANIZE BOX'}], 'tax_lines': [{'id': 95867, 'rate_code': 'IR-مالیات بر ارزش افزوده-1', 'rate_id': 1, 'label': 'مالیات بر ارزش افزوده', 'compound': False, 'tax_total': '24455', 'shipping_tax_total': '0', 'rate_percent': 10, 'meta_data': []}], 'shipping_lines': [{'id': 95866, 'method_title': 'ارسال با پست ویژه', 'method_id': 'flat_rate', 'instance_id': '21', 'total': '85000', 'total_tax': '0', 'taxes': [], 'meta_data': [{'id': 728118, 'key': 'موارد', 'value': 'نظم دهنده سفری و کمد فوروارد Forward مدل FCLT4446 ORGANIZE BOX - فیروزه ای &times; 1', 'display_key': 'موارد', 'display_value': 'نظم دهنده سفری و کمد فوروارد Forward مدل FCLT4446 ORGANIZE BOX - فیروزه ای &times; 1'}]}], 'fee_lines': [], 'coupon_lines': [], 'refunds': [], 'payment_url': 'https://123kif.com/checkout/order-pay/3043961/?pay_for_order=true&key=wc_order_7WI5e1pq0nk98', 'is_editable': False, 'needs_payment': False, 'needs_processing': True, 'date_created_gmt': '2024-10-29T18:04:52', 'date_modified_gmt': '2024-10-29T23:50:25', 'date_completed_gmt': None, 'date_paid_gmt': None, 'currency_symbol': 'تومان', '_links': {'self': [{'href': 'https://123kif.com/wp-json/wc/v3/orders/3043961'}], 'collection': [{'href': 'https://123kif.com/wp-json/wc/v3/orders'}], 'customer': [{'href': 'https://123kif.com/wp-json/wc/v3/customers/2277600'}]}}
data = {'id': 3026277, 'parent_id': 0, 'status': 'on-hold', 'currency': 'IRT', 'version': '9.1.2', 'prices_include_tax': True, 'date_created': '2024-07-13T16:57:04', 'date_modified': '2024-07-24T13:55:33', 'discount_total': '0', 'discount_tax': '0', 'shipping_total': '50000', 'shipping_tax': '0', 'cart_tax': '81364', 'total': '945000', 'total_tax': '81364', 'customer_id': 2265063, 'order_key': 'wc_order_Nje8CprajKrg0', 'billing': {'first_name': 'زهرا', 'last_name': 'منفرد', 'company': '', 'address_1': 'تهران بلوار فردوس شرق خیابان وفا آذر جنوبی کوچه معانی پلاک 40 واحد 8یا 2', 'address_2': '', 'city': 'تهران', 'state': 'THR', 'postcode': '1481995658', 'country': 'IR', 'email': '', 'phone': '09124494421'}, 'shipping': {'first_name': 'زهرا', 'last_name': 'منفرد', 'company': '', 'address_1': 'تهران بلوار فردوس شرق خیابان وفا آذر جنوبی کوچه معانی پلاک 40 واحد 8یا 2', 'address_2': '', 'city': 'تهران', 'state': 'THR', 'postcode': '1481995658', 'country': 'IR', 'phone': ''}, 'payment_method': 'WC_Gateway_SnappPay', 'payment_method_title': 'پرداخت اقساطیِ اسنپ پی', 'transaction_id': '', 'customer_ip_address': '5.52.65.101', 'customer_user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1', 'created_via': 'checkout', 'customer_note': '', 'date_completed': '2024-07-14T10:55:32', 'date_paid': '2024-07-13T16:58:24', 'cart_hash': '0006c717fea0819c1d2ffd6710bf8add', 'number': '3026277', 'meta_data': [{'id': 7547637, 'key': '_billing_real_legal', 'value': 'حقیقی'}, {'id': 7547638, 'key': '_billing_melly_code', 'value': '0010553835'}, {'id': 7547639, 'key': '_billing_floor', 'value': '4 واحد 8 یا 2'}, {'id': 7547640, 'key': '_billing_real_email', 'value': ''}, {'id': 7547641, 'key': '_billing_receiving_invoice', 'value': ''}, {'id': 7547642, 'key': 'is_vat_exempt', 'value': 'no'}, {'id': 7547643, 'key': '_force_enable_buyer', 'value': 'yes'}, {'id': 7547644, 'key': '_allow_buyer_select_status', 'value': 'no'}, {'id': 7547645, 'key': '_buyer_sms_notify', 'value': 'yes'}, {'id': 7547646, 'key': '_thwcfe_ship_to_billing', 'value': '1'}, {'id': 7547647, 'key': '_thwcfe_disabled_fields', 'value': 'billing_legal_code_eghtesadi,billing_legal_sabt_number,shenase_melli_hogh'}, {'id': 7547648, 'key': 'billing_real_legal', 'value': 'حقیقی'}, {'id': 7547649, 'key': 'billing_melly_code', 'value': '0010553835'}, {'id': 7547650, 'key': 'billing_phone', 'value': '09124494421'}, {'id': 7547651, 'key': 'billing_floor', 'value': '4 واحد 8 یا 2'}, {'id': 7547652, 'key': '_wc_order_attribution_source_type', 'value': 'referral'}, {'id': 7547653, 'key': '_wc_order_attribution_referrer', 'value': 'https://pl.snapp.ir/'}, {'id': 7547654, 'key': '_wc_order_attribution_utm_source', 'value': 'pl.snapp.ir'}, {'id': 7547655, 'key': '_wc_order_attribution_utm_medium', 'value': 'referral'}, {'id': 7547656, 'key': '_wc_order_attribution_utm_content', 'value': '/'}, {'id': 7547657, 'key': '_wc_order_attribution_session_entry', 'value': 'https://123kif.com/product/fclt8000/'}, {'id': 7547658, 'key': '_wc_order_attribution_session_start_time', 'value': '2024-07-13 11:41:05'}, {'id': 7547659, 'key': '_wc_order_attribution_session_pages', 'value': '17'}, {'id': 7547660, 'key': '_wc_order_attribution_session_count', 'value': '1'}, {'id': 7547661, 'key': '_wc_order_attribution_user_agent', 'value': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1'}, {'id': 7547662, 'key': '_wc_order_attribution_device_type', 'value': 'Mobile'}, {'id': 7547663, 'key': '_transactionId', 'value': '1720873644-3026277'}, {'id': 7547664, 'key': '_order_spp_token', 'value': '89d3d22b-9b1d-48f1-b675-c47d69a596a1'}, {'id': 7547665, 'key': '_paymentToken', 'value': '89d3d22b-9b1d-48f1-b675-c47d69a596a1'}, {'id': 7547668, 'key': 'order_spp_status', 'value': 'SETTLE'}, {'id': 7547670, 'key': 'wip_cart_discount', 'value': {'90221': 954000}}, {'id': 7547671, 'key': 'wip_cart_price', 'value': {'90221': {'regular_price': '1849000', 'sale_price': '895000'}}}, {'id': 7547672, 'key': 'referral_done', 'value': 'yes'}, {'id': 7548042, 'key': 'tracking_column', 'value': ''}, {'id': 7548043, 'key': 'tracking_type', 'value': 'none'}, {'id': 7548044, 'key': '_assign_to_storage', 'value': '1403/4/23'}, {'id': 7548045, 'key': '_assign_to_warehouse_packing_status', 'value': 'yes'}, {'id': 7548046, 'key': '_assign_to_accounting', 'value': 'yes'}], 'line_items': [{'id': 57080, 'name': 'کوله پشتی اسپرت فوروارد مدل FCLT6010 SPORT COLLECTION - مشکی', 'product_id': 90183, 'variation_id': 90221, 'quantity': 1, 'tax_class': '', 'subtotal': '813636', 'subtotal_tax': '81364', 'total': '813636', 'total_tax': '81364', 'taxes': [{'id': 1, 'total': '81363.636364', 'subtotal': '81363.636364'}], 'meta_data': [{'id': 445249, 'key': 'pa_color', 'value': 'meshki', 'display_key': 'رنگ', 'display_value': 'مشکی'}, {'id': 462843, 'key': '_reduced_stock', 'value': '1', 'display_key': '_reduced_stock', 'display_value': '1'}], 'sku': '1310201001642', 'price': 813636.363636, 'image': {'id': 3019973, 'src': 'https://123kif.com/wp-content/uploads/2023/11/FCLT6010-FORWARD-1.png'}, 'parent_name': 'کوله پشتی اسپرت فوروارد مدل FCLT6010 SPORT COLLECTION'}], 'tax_lines': [{'id': 57082, 'rate_code': 'IR-مالیات بر ارزش افزوده-1', 'rate_id': 1, 'label': 'مالیات بر ارزش افزوده', 'compound': False, 'tax_total': '81364', 'shipping_tax_total': '0', 'rate_percent': 10, 'meta_data': []}], 'shipping_lines': [{'id': 57081, 'method_title': 'ارسال با پست', 'method_id': 'flat_rate', 'instance_id': '20', 'total': '50000', 'total_tax': '0', 'taxes': [], 'meta_data': [{'id': 445255, 'key': 'آیتم\u200cها', 'value': 'کوله پشتی اسپرت فوروارد مدل FCLT6010 SPORT COLLECTION - مشکی &times; 1', 'display_key': 'آیتم\u200cها', 'display_value': 'کوله پشتی اسپرت فوروارد مدل FCLT6010 SPORT COLLECTION - مشکی &times; 1'}]}], 'fee_lines': [], 'coupon_lines': [], 'refunds': [], 'payment_url': 'https://123kif.com/checkout/order-pay/3026277/?pay_for_order=true&key=wc_order_Nje8CprajKrg0', 'is_editable': True, 'needs_payment': False, 'needs_processing': True, 'date_created_gmt': '2024-07-13T12:27:04', 'date_modified_gmt': '2024-07-24T09:25:33', 'date_completed_gmt': '2024-07-14T06:25:32', 'date_paid_gmt': '2024-07-13T12:28:24', 'currency_symbol': 'تومان', '_links': {'self': [{'href': 'https://123kif.com/wp-json/wc/v3/orders/3026277'}], 'collection': [{'href': 'https://123kif.com/wp-json/wc/v3/orders'}], 'customer': [{'href': 'https://123kif.com/wp-json/wc/v3/customers/2265063'}]}}

'''
Show received data item keys :
len(keys) = 47 for all success status
'''
k = data.keys()
keys = [x for x in k]

# All Keys for success status
keys = [
    'id',
    'parent_id',
    'status',
    'currency',
    'version', 
    'prices_include_tax',
    'date_created',
    'date_modified',
    'discount_total',
    'discount_tax',
    'shipping_total',
    'shipping_tax',
    'cart_tax',
    'total',
    'total_tax',
    'customer_id',
    'order_key',
    'billing',
    'shipping',
    'payment_method',
    'payment_method_title',
    'transaction_id',
    'customer_ip_address',
    'customer_user_agent',
    'created_via',
    'customer_note',
    'date_completed',
    'date_paid',
    'cart_hash',
    'number',
    'meta_data',
    'line_items',
    'tax_lines',
    'shipping_lines',
    'fee_lines',
    'coupon_lines',
    'refunds',
    'payment_url',
    'is_editable',
    'needs_payment',
    'needs_processing',
    'date_created_gmt',
    'date_modified_gmt',
    'date_completed_gmt',
    'date_paid_gmt',
    'currency_symbol',
    '_links'
    ]
