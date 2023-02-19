class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_lvl_1(txt: str) -> None:
    print(f"{BColors.OKBLUE}::{BColors.ENDC} {txt}")


def print_lvl_2(txt: str) -> None:
    print(f" {txt}")


def print_lvl_3(txt: str) -> None:
    print(f"  {txt}")
