'''
The tracking_post script have a class Tracker and some functions
for tracking a package detail sended by Islamic republic of iran post co

functions of Tracker class :
    {
      0. init
      1. run
    }
dev: Unique174
github: https://github.com/irAbs174/post_tracker
nft market: https://getgems.io/unique-nft

BE HAPPY :)
'''

from driver_functions import DriverFunctions

class Tracker:
    def __init__(self, tracking_code):
        self.tracking_code = tracking_code
        self.run()
        
    def run(self):
        # Use class DriverFunctions for run post tracker detail runner
        DriverFunctions(
            "https://tracking.post.ir",
            self.tracking_code
        ).run()
        
    
def main():
    tracking_code = input("\n Enter Tracking code: ")
    Tracker(tracking_code)

# Note: uncomment if you want execute as python3 file.py
'''
if __name__ == '__main__':
    main()
'''
        