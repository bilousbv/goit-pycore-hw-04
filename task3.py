import sys
from pathlib import Path
from colorama import init, Fore, Style

init()
number_of_spaces_per_tab = 2


def list_files_and_directories(directory, level=1):
    try:
        path = Path(directory)
        if not path.is_dir():
            raise NotADirectoryError(f"{directory} is not a valid directory.")

        if level == 1:
            print(f"{Fore.BLUE}{directory}/{Style.RESET_ALL}")
        for item in path.iterdir():
            if item.is_dir():
                print(f"{Fore.BLUE}{' '*(level*number_of_spaces_per_tab)}{item.name}/{Style.RESET_ALL}")
                list_files_and_directories(item, level + 1)
            else:
                print(f"{Fore.GREEN}{' '*(level*number_of_spaces_per_tab)}{item.name}{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{Fore.RED}Error: {directory} not found.{Style.RESET_ALL}")
    except NotADirectoryError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Error: Permission denied for {directory}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Usage: python script.py <directory_path>{Style.RESET_ALL}")
    else:
        directory_path = sys.argv[1]
        list_files_and_directories(directory_path)
