import click
from rich import print
from datetime import datetime

from labor.api import _sign_in, _sign_out, _tasks, _reports, _wage
from labor.config import write, load
from labor.beautify import printTasks, print_reports

from click.exceptions import Abort
from labor.controllers.login import LoginController
from labor.controllers.tasks import TasksController
from labor.utils.screen import Screen

@click.group()
def cli():
    ...


@cli.command(help="Login to Labor")
def sign_in():
    try:
        LoginController().sign_in()
    except Abort:
        Screen.goodbye_message()


@cli.command(help="Show opened tasks")
def opened():
    TasksController().opened_task()

@cli.command(help="Logout from Labor")
def sign_out():
    logged_user = load()
    headers = logged_user['saved_headers']
    status = _sign_out(headers)
    if status == 200:
        write({})
    else: 
        print('Error while signing out')


@cli.command(help="Default is current month, use month and year in numbers")
@click.argument("month", required=False)
@click.argument("year", required=False)
def tasks(month, year):
    try:
        if not year:
            year = datetime.now().year
        if not month: 
            month = datetime.now().month
        logged_user = load()
        data, status, projects = _tasks(logged_user, month, year)
        wage, wage_status = _wage(logged_user)
        if status == 200 and wage_status == 200: 
            print(printTasks(dict.items(data), projects, wage))
        else: 
            print(f"Error while retrieving data: {status}")
    except OSError: 
        print(f"You need to login first, error: {OSError}")

@cli.command(help="Get reports")
@click.argument("year", required=False)
def reports(year):
    try: 
        if not year:
            year = datetime.now().year
        logged_user = load()
        data, status = _reports(logged_user, year)
        if status == 200:
            print(print_reports(data))
    except:
        print("You need to login first")

if __name__ == "__main__":
    cli()
