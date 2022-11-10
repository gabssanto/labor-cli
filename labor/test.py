
import fortune
from click.exceptions import Abort
from labor.controllers.login import LoginController
from labor.utils.screen import Screen

def main():

    LoginController().sign_in()
    
if __name__ == '__main__':

    try:
        main()
    except Abort:

        Screen.goodbye_message()
