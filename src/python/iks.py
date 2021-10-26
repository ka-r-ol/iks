import logging
from libki import MainMenu, global_ctx

if __name__ == "__main__":
    try:
        MainMenu().run(quick_execution=global_ctx.quick_execution)
    except KeyboardInterrupt:
        print("\nBye bye")
    except Exception as err:
        logging.error(f"Somethings gone wrong: {str(err)}", exc_info=True)
