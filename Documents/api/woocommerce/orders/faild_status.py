data = WC_API.get(f'orders/{order_code}').json()

# Failed requests examples
data = {'code': 'woocommerce_rest_shop_order_invalid_id', 'message': 'شناسه نامعتبر است.', 'data': {'status': 404}}

'''
All Keys for success status
len(keys) = 3 for all Failed status
'''
keys = [
    'code',
    'message',
    'data'
    ]

