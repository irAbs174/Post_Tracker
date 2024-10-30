from core.SEC import WC_API

class OrderDetail:
    def __init__(self, order_code):
        self.ctx = {}
        self.order_code = int(order_code)
        
    def get_order(self):
        response = WC_API.get(f'orders/{self.order_code}').json()
        if response.get('status') is not None:
            # personal details
            first_name = response['shipping']['first_name']
            last_name = response['shipping']['last_name']
            self.ctx['full_name'] = f"{first_name} {last_name}"
            # billing / shipping details
            city = response['billing']['city']
            phone = response['billing']['phone']
            address = response['billing']['address_1']
            unit = response['billing']['address_2']
            postcode = response['shipping']['postcode']
            self.ctx['shipping_method'] = response['shipping_lines'][0]['method_title']
            self.ctx['shipping_total'] = response['shipping_lines'][0]['total']
            self.ctx['full_address'] = f"شهر {city} / {address} / {unit} / کدپستی: {postcode}"
            # invoke details
            self.ctx['products'] = [{
                'name': i[0].split(' - ')[0],
                'color': i[0].split(' - ')[1],
                'qty': i[1].split(" ")[1]
                }for i in [
                    x.split('&times;') for x in response['shipping_lines'][0]['meta_data'][0]['display_value'].split(',')
                    ]]
            self.ctx['payment_method_title'] = response['payment_method_title']
            self.ctx['total'] = response['total']
            
        return self.ctx