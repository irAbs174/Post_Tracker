# order srarus
status = data['status']

# personal details
first_name = data['shipping']['first_name']
last_name = data['shipping']['last_name']
full_name = f"{first_name} {last_name}"

# billing / shipping details
city = data['billing']['city']
phone = data['billing']['phone']
address = data['billing']['address_1']
unit = data['billing']['address_2']
postcode = data['shipping']['postcode']
customer_note = data['customer_note']
shipping_method = data['shipping_lines'][0]['method_title']
shipping_total = data['shipping_lines'][0]['total']
full_address = f"شهر {city} / {address} / {unit} / کدپستی: {postcode}"

# invoke details
products = [{
    'name': i[0].split(' - ')[0],
    'color': i[0].split(' - ')[1],
    'qty': i[1].split(" ")[1]
    }for i in [
        x.split('&times;') for x in data['shipping_lines'][0]['meta_data'][0]['display_value'].split(',')
        ]]
payment_method_title = data['payment_method_title']
total = data['total']

# simple usage
result = f'''
order status : {status}\n
customer : {full_name}\n
phone number : {phone}\n
address : {full_address}\n
shipping method : {shipping_method}\n
{payment_method_title}\n
orders : {products}\n
total sell : {total}\n
'''
print(result)
