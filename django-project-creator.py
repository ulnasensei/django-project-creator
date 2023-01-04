#!/usr/bin/env python

from venv import create
import urllib.request
from subprocess import check_call, run, DEVNULL
import sys
import os
import logging
import signal
import secrets
import platform


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def exit_handler(signum, frame):
    exit(1)


def main():
    signal.signal(signal.SIGINT, exit_handler)
    windows = True if platform.system() == "Windows" else False
    macos = True if platform.system() == "Darwin" else False
    git_bash = False
    if windows and os.environ.get("SHELL"):
        git_bash = True

    if windows:
        os.system("color")

    logfile = f'{os.path.expanduser("~")}/django-project-creator.log'
    logging.basicConfig(
        filename=logfile,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )
    logger = logging.getLogger("django-project-creator")

    logger.info("------------START OF LOG------------")
    logger.info("Starting Django Project Creator")
    print(
        f"{bcolors.BOLD}{bcolors.HEADER}Starting Django Project Creator...{bcolors.ENDC}\n"
    )

    project_name = ""
    try:
        project_name = sys.argv[1]
        logger.info(f"Project name: {project_name}\n")
    except IndexError as ex:
        logger.info('No project name was provided. Using "django-project".')
        print(
            f'{bcolors.WARNING}No project name was provided. Using "django-project".{bcolors.ENDC}\n'
        )
        project_name = "django-project"

    try:
        os.mkdir(project_name)
        print(
            f"{bcolors.OKGREEN}Created project directory: {bcolors.BOLD}{bcolors.OKBLUE}{project_name}{bcolors.ENDC}"
        )
        logger.info(f"Created project directory: {project_name}")
    except FileExistsError as ex:
        print(
            f"{bcolors.FAIL}Project already exists: {bcolors.BOLD}{project_name}{bcolors.ENDC}"
        )
        logger.fatal(ex)
        exit(1)
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)
    try:
        os.chdir(project_name)
        print(
            f"{bcolors.OKGREEN}Changed active directory to project directory: {bcolors.BOLD}{bcolors.OKBLUE}{project_name}{bcolors.ENDC}"
        )
        logger.info(f"Changed active directory to project directory: {project_name}")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        create(".venv")
        print(
            f"{bcolors.OKGREEN}Created virtual environment: {bcolors.BOLD}{bcolors.OKBLUE}{project_name}/.venv{bcolors.ENDC}"
        )
        logger.info(f"Created virtual environment: {project_name}/.venv")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Installing pip...{bcolors.ENDC}")
        if windows:
            run(
                f".\\.venv\\Scripts\\python -m ensurepip --upgrade",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        else:
            run(
                f"./.venv/bin/python -m ensurepip --upgrade",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        print(f"{bcolors.OKGREEN}Installed pip.{bcolors.ENDC}")
        logger.info("Installed pip.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Updating pip...{bcolors.ENDC}")
        if windows:
            run(
                f".\\.venv\\Scripts\\python -m pip install --upgrade pip",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        else:
            run(
                f"./.venv/bin/python -m pip install --upgrade pip",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        print(f"{bcolors.OKGREEN}Updated pip.{bcolors.ENDC}")
        logger.info("Updated pip.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        if windows or git_bash:
            run(".\\.venv\\Scripts\\activate", stdout=DEVNULL, shell=True, check=True)
        else:
            run(". ./.venv/bin/activate", stdout=DEVNULL, shell=True, check=True)
        print(
            f"{bcolors.OKGREEN}Activated virtual environment: {bcolors.BOLD}{bcolors.OKBLUE}{project_name}/.venv{bcolors.ENDC}"
        )
        logger.info(f"Activated virtual environment: {project_name}/.venv")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Installing Django Rest Framework...{bcolors.ENDC}")
        if windows:
            run(
                f".\\.venv\\Scripts\\python -m pip install djangorestframework",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        else:
            run(
                f"./.venv/bin/python -m pip install djangorestframework",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        print(f"{bcolors.OKGREEN}Installed Django Rest Framework.{bcolors.ENDC}")
        logger.info("Installed Django Rest Framework.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Installing Python-Decouple...{bcolors.ENDC}")
        if windows:
            run(
                f".\\.venv\\Scripts\\python -m pip install python-decouple",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        else:
            run(
                f"./.venv/bin/python -m pip install python-decouple",
                shell=True,
                stdout=DEVNULL,
                check=True,
            )
        print(f"{bcolors.OKGREEN}Installed Python-Decouple.{bcolors.ENDC}")
        logger.info("Installed Python-Decouple.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating requirements.txt...{bcolors.ENDC}")
        if windows:
            run(
                ".\\.venv\\Scripts\\python -m pip freeze > requirements.txt",
                shell=True,
                check=True,
            )
        else:
            run(
                "./.venv/bin/python -m pip freeze > requirements.txt",
                shell=True,
                check=True,
            )
        print(f"{bcolors.OKGREEN}Created requirements.txt.{bcolors.ENDC}")
        logger.info("Created requirements.txt.")
        with open("requirements.txt", "r") as reqs:
            print(
                f"\n{bcolors.BOLD}{bcolors.UNDERLINE}{bcolors.HEADER}Required packages:{bcolors.ENDC}\n"
            )
            print(f"{bcolors.HEADER}{reqs.read()}{bcolors.ENDC}")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Generating Django Secret Key...{bcolors.ENDC}")

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(-_=+)"

        secret_key = "".join(secrets.choice(chars) for i in range(50))

        print(f"{bcolors.OKCYAN}Creating '.env' file...{bcolors.ENDC}")
        with open("./.env", "w") as file:
            file.write(f"SECRET_KEY={secret_key}")

        print(f"{bcolors.OKCYAN}Created '.env' file.{bcolors.ENDC}")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating Django project 'core'...{bcolors.ENDC}")

        if windows:
            run(
                ".\\.venv\\Scripts\\python -m django startproject core .",
                shell=True,
                check=True,
            )
        else:
            run("./.venv/bin/django-admin startproject core .", shell=True, check=True)
        print(f"{bcolors.OKGREEN}Created Django project 'core'.{bcolors.ENDC}")
        logger.info("Created Django project 'core'.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating Django app 'main'...{bcolors.ENDC}")

        if windows:
            run(
                ".\\.venv\\Scripts\\python -m django startapp main",
                shell=True,
                check=True,
            )
        else:
            run("./.venv/bin/django-admin startapp main", shell=True, check=True)
        print(f"{bcolors.OKGREEN}Created Django app 'main'.{bcolors.ENDC}")
        logger.info("Created Django app 'main'.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating 'forms.py'...{bcolors.ENDC}")

        with open("./main/forms.py", "w") as f:
            pass
        print(f"{bcolors.OKGREEN}Created 'forms.py'.{bcolors.ENDC}")
        logger.info("Created 'forms.py'.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating template directory...{bcolors.ENDC}")

        os.mkdir("./main/templates")
        print(f"{bcolors.OKGREEN}Created template directory.{bcolors.ENDC}")
        logger.info("Created template directory.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating sample index.html...{bcolors.ENDC}")

        index_html = """<html>
  <head>
   <title>$project</title>
  </head>
  <body>
    <div class="container">
      <h1>Welcome to your Create Django App</h1>
    </div>
  </body>
</html>"""
        with open("main/templates/index.html", "w") as f:
            f.write(index_html)

        print(f"{bcolors.OKGREEN}Created sample index.html.{bcolors.ENDC}")
        logger.info("Created sample index.html.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Adding app 'main' to settings.py...{bcolors.ENDC}")
        with open("./core/settings.py", "r") as file:
            filedata = file.read()

        filedata = filedata.replace(
            "'django.contrib.staticfiles',",
            "'django.contrib.staticfiles',\n\n    # my apps\n    'main',",
        ).replace(
            '"django.contrib.staticfiles",',
            '"django.contrib.staticfiles",\n\n    # my apps\n    "main",',
        )

        with open("./core/settings.py", "w") as file:
            file.write(filedata)

        print(f"{bcolors.OKCYAN}Updated settings.py{bcolors.ENDC}")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Adding restframework to settings.py...{bcolors.ENDC}")
        with open("./core/settings.py", "r") as file:
            filedata = file.read()

        filedata = filedata.replace(
            "'django.contrib.staticfiles',",
            "'django.contrib.staticfiles',\n\n    # 3rd party apps\n    'rest_framework',",
        ).replace(
            '"django.contrib.staticfiles",',
            '"django.contrib.staticfiles",\n\n    # 3rd party apps\n    "rest_framework",',
        )

        with open("./core/settings.py", "w") as file:
            file.write(filedata)

        print(f"{bcolors.OKCYAN}Updated settings.py{bcolors.ENDC}")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(
            f"{bcolors.OKCYAN}Editing settings.py to use '.env' variables...{bcolors.ENDC}"
        )
        with open("./core/settings.py", "r") as file:
            filedata = file.read()

        filedata = filedata.replace(
            "from pathlib import Path",
            "from pathlib import Path\nfrom decouple import config",
        )
        new_data = ""
        for line in filedata.splitlines():
            if "SECRET_KEY" in line:
                new_data += 'SECRET_KEY = config("SECRET_KEY")\n'
            else:
                new_data += line + "\n"

        with open("./core/settings.py", "w") as file:
            file.write(new_data)

        print(f"{bcolors.OKCYAN}Updated settings.py{bcolors.ENDC}")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating sample view...{bcolors.ENDC}")
        with open("./main/views.py", "w") as file:
            file.write(
                """from django.shortcuts import render
from django.http import HttpResponse


# def home(request):
#     return HttpResponse("<h1>Welcome to the Django.</h1>")


def home(request):
    return render(request, "index.html")"""
            )

        print(f"{bcolors.OKCYAN}Created sample view...{bcolors.ENDC}")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Starting Django migration...{bcolors.ENDC}")
        if windows:
            run(".\\.venv\\Scripts\\python manage.py migrate", shell=True, check=True)
        else:
            run("./.venv/bin/python manage.py migrate", shell=True, check=True)
        print(f"{bcolors.OKGREEN}Django migration is successful.{bcolors.ENDC}")
        logger.info("Django migration is successful.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(f"{bcolors.OKCYAN}Creating superuser...{bcolors.ENDC}")
        if windows:
            run(
                ".\\.venv\\Scripts\\python manage.py createsuperuser",
                shell=True,
                check=True,
            )
        else:
            run("./.venv/bin/python manage.py createsuperuser", shell=True, check=True)
        print(f"{bcolors.OKGREEN}Created superuser.{bcolors.ENDC}")
        logger.info("Created superuser.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)

    try:
        print(
            f"{bcolors.OKCYAN}Downloading .gitignore for Django project...{bcolors.ENDC}"
        )
        gitignore_url = "https://www.toptal.com/developers/gitignore/api/django"
        if macos:  # I don't like this solution.
            run(f'curl {gitignore_url} --output ".gitignore"', shell=True, check=True)
        else:
            opener = urllib.request.build_opener()
            opener.addheaders = [
                (
                    "User-Agent",
                    "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
                )
            ]

            with opener.open(gitignore_url) as url_file:
                url_content = url_file.read()
                with open(".gitignore", "wb") as gitignore:
                    gitignore.write(url_content)

        print(f"{bcolors.OKGREEN}Downloaded .gitignore successfully.{bcolors.ENDC}")
        logger.info("Downloaded .gitignore successfully.")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)
    print(f"\n{bcolors.BOLD}{bcolors.OKGREEN}Created Django project.{bcolors.ENDC}\n")
    logger.info("-------------END OF LOG-------------\n")

    try:
        print(
            f"{bcolors.OKCYAN}Running the server on port {bcolors.BOLD}8081...{bcolors.ENDC}\n"
        )
        if windows:
            check_call(
                ".\\.venv\\Scripts\\python manage.py runserver 8081",
                shell=True,
            )
        else:
            check_call("./.venv/bin/python manage.py runserver 8081", shell=True)
        logger.info("Running the server on port 8081")
    except Exception as ex:
        print(f"{bcolors.BOLD}{bcolors.FAIL}{ex}{bcolors.ENDC}")
        logger.fatal(ex)
        exit(1)


if __name__ == "__main__":
    main()
