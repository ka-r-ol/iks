import sys
import os
import logging
from simple_menu import MainMenu

if __name__ == "__main__":
    try:
        #menu_path = sys.argv[1]
        menu_path = os.environ['IKS_MENU_DIR']
        if not menu_path:
            print("no IKS_MENU_DIR set")
            exit(0)
        quick_execution = []
        if len(sys.argv) > 1:
            quick_execution = sys.argv[1:]
        menu = MainMenu(menu_path=menu_path)
        menu.run(quick_execution=quick_execution)
    except KeyboardInterrupt:
        print("\nBye bye")
        exit(0)
    except Exception as err:
        logging.error(f"Somethings gone wrong: {str(err)}", exc_info=True)
