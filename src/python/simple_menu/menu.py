import os
import logging
from typing import TypedDict
from pathlib import Path, PosixPath

class C:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Ctx(TypedDict):
    path: str
    quick_execution: list
    user_input: str
    exit: bool


class MainMenu:
    def __init__(self, menu_path: str):
        if not self._is_dir(menu_path):
            raise Exception(f"{menu_path} is not a directory!!! Exiting...")
        self.menu_path = menu_path

    @staticmethod
    def _is_exe(fpath: str):
        if not os.path.isfile(fpath):
            return False
        if not os.access(fpath, os.X_OK):
            logging.warning(f"{fpath} is not executable")
            return False
        return True

    @staticmethod
    def _is_dir(fpath: str):
        return os.path.isdir(fpath)

    @staticmethod
    def _exit():
        print("Done!")
        exit(0)

    def _help(self):
        print("bash  - run bash")
        print("clear - clears the terminal window")
        print("top   - go to top menu")
        print("up    - go to upper menu")
        print("exit, quit  - exit iks")

    def _analize_user_input(self, ctx: Ctx) -> Ctx:
        user_inputs = list(filter(lambda x: len(x) > 0, ctx.get("user_input").split(" ")))
        if len(user_inputs) == 1:
            if user_inputs[0] == 'up':
                if ctx['path'] != self.menu_path:
                    ctx['path'] = os.path.dirname(ctx['path'])
            elif user_inputs[0] == 'top':
                ctx['path'] = self.menu_path
            elif user_inputs[0] == 'exit'  or user_inputs[0] == 'quit':
                self._exit()
            elif user_inputs[0] == 'clear':
                os.system("clear")
            elif user_inputs[0] == 'bash':
                os.system("/usr/local/bin/bash")
            elif user_inputs[0] == '?':
                self._help()
        if len(user_inputs) > 1:
            ctx['quick_execution'] = user_inputs
            ctx['user_input'] = ""
        return ctx

    def run(self, quick_execution: list = []):
        ctx: Ctx = {
            "path": self.menu_path,
            "quick_execution": quick_execution,
            "user_input": "",
            "exit": True if quick_execution else False
        }

        menu = Menu()
        while True:

            ctx = self._analize_user_input(ctx)

            if self._is_exe(ctx.get("path")):
                os.system(ctx.get("path"))
                if ctx['exit']:
                    self._exit()
                ctx['path'] = os.path.dirname(ctx['path'])

            ctx = menu.run(ctx=ctx)


class Menu:

    def _show_menu(self, ctx: Ctx, menu_items: dict):
        print("---v")
        for command, menu_item in menu_items.items():
            print(f"{C.HEADER}{command:10}{C.ENDC}{menu_item[0]}")
        print("---^")
        print(f"{C.BOLD}{'?':5}{C.ENDC}help")

    def _prepare_menu_item(self, name: PosixPath):
        return name.name.split("__")[:2]

    def _prepare_menu_items(self, path: str) -> dict:
        menu_items = dict()
        p = Path(path)
        for name in p.glob('[!\.]*__*__item*'):
            command, label = self._prepare_menu_item(name=name)
            menu_items[command] = (label, str(name))

        return menu_items

    def run(self, ctx: Ctx):

        menu_items = self._prepare_menu_items(ctx['path'])
        # if not ctx['exit']:
        if ctx['quick_execution']:
            user_input = ctx['quick_execution'][0]
            if user_input in menu_items.keys():
                ctx['quick_execution'] = ctx['quick_execution'][1:]
            else:
                ctx['quick_execution'] = []

        else:
            self._show_menu(ctx=ctx, menu_items=menu_items)
            user_input = input(f"{C.BOLD}>{C.ENDC} ")
            if user_input == "":
                os.system("clear")

        if user_input in menu_items.keys():
            ctx['path'] = menu_items[user_input][1]
            ctx['user_input'] = ""
        else:
            ctx['user_input'] = user_input
        return ctx
