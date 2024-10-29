'''
functions for post_tracker script
++>> Some helpful driver functions include :
    {
      0. init function of class for inital driver.
      1. test function for run all driver tests.
      2. screenshot shot of page.
      3. quit function for close driver session.
      4. run function do full tasks with use parent class functions returns
    }

dev: Unique174
github: https://github.com/irAbs174/post_tracker
nft market: https://getgems.io/unique-nft

BE HAPPY :)
'''

#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from colorama import Fore
from pathlib import Path
from time import sleep


class DriverFunctions:
    def __init__(self, address, tracking_code):
        # inital driver with given address and tracking_code
        print(
            Fore.WHITE,
            f"\n-> ++>> {address} for tacking {tracking_code} \n"
        )
        
        try:
            ''' Define web driver (Chrome by default) '''
            # with GUI (such as local host) :
            self.driver = Chrome()
            # with CLI (such as production server) :
            '''
            options = Options()
            #options.add_argument('--headless')
            #options.add_argument('--no-sandbox')
            #options.add_argument('--disable-dev-shm-usage')
            #self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
            '''
            self.address = address
            self.tracking_code = tracking_code
            self.driver.get(self.address)
            print(
                Fore.GREEN,
                f"\n ++>> Site {self.address} initial successfuly! \n"
            )
        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
            )
        
    def screenshot(self):
        # save page screen shot and store with tracking_code name
        try:
            self.path = f"{Path.home()}/Pictures/post/{self.tracking_code}.png"
            self.driver.save_screenshot(self.path)
            
        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
            )
        
    def set_data(self):
        self.driver.mobile
        input = self.driver.find_element(By.ID, "txtbSearch")
        input.send_keys(self.tracking_code)
        btn = self.driver.find_element(By.ID, "btnSearch")
        btn.click()
        
        
    def test(self):
        try:
            for i in range(1):
                sleep(1)
                print(
                    Fore.RED,
                    f'\n =>    sleeped {i} secend ...'
                )
                
        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
            )
            
        
    def run(self):
        try:
            print(
                Fore.BLUE,
                f"\n => => Full Detail for {self.address} with code {self.tracking_code}\n"
            )
            self.set_data()
            self.screenshot()
            self.title = self.driver.title
            self.url = self.driver.current_url
            output = f"""\n
            ------------------------------
            Page title: {self.title}
            url : {self.url}
            Screen shot : Screen shot stored to path :
                => {self.path}
            ------------------------------"""
            print(
                Fore.GREEN,
                output
            )
        except Exception as error:
            print(
                Fore.GREEN,
                f"\n :( Error: \n {error} \n"
                )
            output = None
            
        self.quit()
        return output
        
    def quit(self):
        try:
            self.driver.quit()
            print(
                Fore.MAGENTA,
                "\n -----------Chrome WebDriver Closed successfuly-----------\n"
            )
        except Exception as error:
            print(
                Fore.RED,
                f"\n :( Error: \n {error} \n"
                )
        
    
# Main function for excute script as single file
def main():
    # Script options
    options = {
        0: "Run",
        1: "Take screen shot",
        2: "Test"
    }
    
    #Show options
    print(Fore.MAGENTA + "\nAvailable Options:")
    for key, value in options.items():
        print(
            Fore.BLUE + f"{key}: {value}"
            )
    
    # Give job option
    selected_option = input("\n=> Select an Option: ")
    
    # Give address
    address = input("\n => Enter address: ")
        
    # Give tracking code
    tracking_code = input("\n Enter Tracking Code: ")
    
    # Doing job according to the selected opotion
    try:
        if selected_option == '0':
            # Call run function on DriverFunctions class
            DriverFunctions(
                address,
                tracking_code
                ).run()
            
        elif selected_option == '1':
            # Call screenshot function on DriverFunctions class
            DriverFunctions(
                address,
                tracking_code
                ).screenshot()
            
        elif selected_option == '2':
            # Call test function on DriverFunctions class
            DriverFunctions(
                address,
                tracking_code
                ).test()
            
    except Exception as error:
        print(
            Fore.RED,
            f'Please select a valid option \n +> {error}',
            )
        

# Note: uncomment if you want execute as python3 file.py
'''
if __name__ == '__main__':
    main()
'''