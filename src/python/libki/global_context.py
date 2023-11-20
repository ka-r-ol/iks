import sys
import os


class GlobalContext:
    menu_path: str
    editor: str
    shell: str
    quick_execution: list = sys.argv[1:] if len(sys.argv) > 1 else []

    def __init__(self):
        self.menu_path = self._get_env_value(env_param='IKS_MENU_DIR')
        if not os.path.isdir(self.menu_path):
            raise Exception(f"{self.menu_path} is not a directory!!! Exiting...")

        self.editor = self._get_env_value(env_param='EDITOR')
        self.shell = self._get_env_value(env_param='SHELL')

    def _get_env_value(self, env_param: str):
        value = os.environ[env_param]
        if not value:
            print(f"no {env_param} set")
            exit(0)
        return value


global_ctx = GlobalContext()
