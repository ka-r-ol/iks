import os
import logging
from typing import TypedDict
from pathlib import Path, PosixPath
from .global_context import global_ctx


class C:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Ctx(TypedDict):
    header: str
    path: str
    quick_execution: list
    user_input: str
    exit: bool


def _is_exe(fpath: str):
    if not os.path.isfile(fpath):
        return False
    if not os.access(fpath, os.X_OK):
        logging.warning(f"{fpath} is not executable")
        return False
    return True


class MainMenu:
    @staticmethod
    def _exit():
        print("Done!")
        exit(0)

    def _help(self):
        print("shell  - run shell")
        print("e      - run editor")
        print("clear - clears the terminal window")
        print("top   - go to top menu")
        print("up    - go to upper menu")
        print("exit, quit  - exit iks")

    def _analize_user_input(self, ctx: Ctx) -> Ctx:
        user_inputs = list(
            filter(lambda x: len(x) > 0, ctx.get("user_input").split(" "))
        )
        if len(user_inputs) == 1:
            if user_inputs[0] == "up":
                if ctx["path"] != global_ctx.menu_path:
                    ctx["path"] = os.path.dirname(ctx["path"])
                    ctx["header"] = ctx["header"][: ctx["header"].rfind("/")]
            elif user_inputs[0] == "top":
                ctx["header"] = "/"
                ctx["path"] = global_ctx.menu_path
            elif user_inputs[0] in ["exit", "quit"]:
                self._exit()
            elif user_inputs[0] == "clear":
                os.system("clear")
            elif user_inputs[0] == "shell":
                os.system(global_ctx.shell)
            elif user_inputs[0] == "e":
                os.system(f"{global_ctx.editor} {ctx['path']}")
            elif user_inputs[0] in ["?", "help"]:
                self._help()
        if len(user_inputs) > 1:
            ctx["quick_execution"] = user_inputs
            ctx["user_input"] = ""
        return ctx

    def run(self, quick_execution: list = []):
        ctx: Ctx = {
            "header": "/",
            "path": global_ctx.menu_path,
            "quick_execution": quick_execution,
            "user_input": "",
            "exit": True if quick_execution else False,
        }

        menu = Menu()
        while True:
            ctx = self._analize_user_input(ctx)

            if _is_exe(ctx.get("path")):
                os.system(ctx.get("path"))
                if ctx["exit"]:
                    self._exit()
                ctx["path"] = os.path.dirname(ctx["path"])

            ctx = menu.run(ctx=ctx)


class Menu:
    def _get_header(self, path):
        list1 = os.path.normpath(path[len(global_ctx.menu_path) :]).split(os.sep)
        list2 = filter(lambda x: len(x) > 1, list1)
        header = list(map(lambda x: x.split("__")[:1][0], list2))

        return f": {C.BOLD}[ {' / '.join(header)} ]{C.ENDC}"

    def _show_menu(self, ctx: Ctx, menu_items: dict):
        header = self._get_header(ctx.get("path"))
        print(f"---v{header}")
        for command, menu_item in sorted(menu_items.items(), key=lambda x: x[0]):
            print(f"{C.HEADER}{command:10}{C.ENDC}{menu_item[0]}")
        print("---^")
        print(f"{C.BOLD}{'?':5}{C.ENDC}help")

    def _prepare_menu_item(self, name: PosixPath):
        return name.name.split("__")[:2]

    def _prepare_menu_items(self, ctx: Ctx, path: str) -> dict:
        menu_items = dict()
        p = Path(path)
        for name in p.glob("[!\.]*__*__item*"):
            command, label = self._prepare_menu_item(name=name)
            menu_items[command] = (label, str(name))

        return menu_items

    def run(self, ctx: Ctx):
        menu_items = self._prepare_menu_items(ctx, ctx["path"])
        if ctx["quick_execution"]:
            user_input = ctx["quick_execution"][0]
            if user_input in menu_items.keys():
                ctx["quick_execution"] = ctx["quick_execution"][1:]
            else:
                ctx["quick_execution"] = []

        else:
            self._show_menu(ctx=ctx, menu_items=menu_items)
            user_input = input(f"{C.BOLD}>{C.ENDC} ")
            if user_input == "":
                os.system("clear")

        if user_input in menu_items.keys():
            ctx["path"] = menu_items[user_input][1]
            ctx["user_input"] = ""
        else:
            ctx["user_input"] = user_input
        return ctx
