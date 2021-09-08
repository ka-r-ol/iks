import sys
import logging
from simple_menu import MainMenu

if __name__ == "__main__":
    try:
        menu_path = sys.argv[1]
        quick_execution = []
        if len(sys.argv) > 2:
            quick_execution = sys.argv[2:]
        menu = MainMenu(menu_path=menu_path)
        menu.run(quick_execution=quick_execution)
    except KeyboardInterrupt:
        print("\nBye bye")
        exit(0)
    except Exception as err:
        logging.error(f"Somethings gone wrong: {str(err)}", exc_info=True)
