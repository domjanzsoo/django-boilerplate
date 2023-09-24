import sys
import shutil
import os
from termcolor import colored
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from django.core.management.utils import get_random_secret_key

colorama_init()

def create_env_file(data: dict):
    print(f'{Fore.GREEN}Creating application environment file.{Style.RESET_ALL}')
    try:
        env_file = open("./.env", "w+")
        for variable in data:
            env_file.write(variable.upper() + "=" + data[variable] + "\n")

        print(f'{Fore.GREEN}Environment file successfully created{Style.RESET_ALL}')
        env_file.close()
    except:
        print(f'{Fore.RED}Environment file creation failed{Style.RESET_ALL}')

def rename_project(name: str):
    print(f'{Fore.GREEN}Renaming directories.{Style.RESET_ALL}')

    os.rename('./project', f'./{name}')

    os.chdir('..')

    os.rename('./project', f'./{name}')

env_data = {}

env_data['debug'] = "True"

env_data['project_name'] = input(f'{Fore.GREEN}Project name (default: project){Style.RESET_ALL}' or "project")
env_data['db_name'] = input(f'{Fore.GREEN}Database name (press enter if want it blank){Style.RESET_ALL}' or "")
env_data['db_engine'] = input(f'{Fore.GREEN}Database engine (default: django.db.backends.mysql){Style.RESET_ALL}' or "django.db.backends.mysql")
env_data['db_user ']= input(f'{Fore.GREEN}Database user (press enter if want it blank){Style.RESET_ALL}' or "")
env_data['db_password'] = input(f'{Fore.GREEN}Database password (press enter if want it blank){Style.RESET_ALL}' or "")
env_data['db_host'] = input(f'{Fore.GREEN}Database host (default: localhost){Style.RESET_ALL}' or "localhost")
env_data['db_port'] = input(f'{Fore.GREEN}Database port (default: 3306){Style.RESET_ALL}' or "3306")

env_data['secret_key'] = get_random_secret_key()

print(f'{Fore.GREEN}Secret key {env_data["secret_key"]} was generated{Style.RESET_ALL}')

create_env_file(env_data)
rename_project(env_data['project_name'])

# env = sys.argv[1]
#
# print(f'Creating local setting file for {env}')
#
# current_dir = path.dirname(__file__)
#
# print(current_dir)
#
# this_dir = path.dirname(__file__)
# filename = path.realpath("{0}/settings/prod_settings.py".format(this_dir))
#
# file_setting_path = path.join(current_dir, f'settings\\{env}_settings.py')
# target_path = r'./local_settings.py'
#
# print(filename)
# if not path.isfile(filename):
#     print(f'{Fore.RED}No settings file found for the given environment{Style.RESET_ALL}')
#     quit()


# shutil.copyfile(file_setting_path, target_path)

# print('Setting file created')




