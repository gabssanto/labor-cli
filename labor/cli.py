import click
from rich import print as rich_print
from datetime import datetime

from api import _sign_in, _sign_out, _tasks, _reports, _wage
from config import write, load
from beautify import printTasks, print_reports


@click.group()
def cli():
    ...


@cli.command(help="Login to Labor")
def sign_in():
    email = click.prompt('Enter your email', type=str)
    password = click.prompt('Enter your password', type=str, hide_input=True)
    data, status, headers = _sign_in(email, password)

    saved_headers = {
        'access-token': headers['access-token'],
        'client': headers['client'],
        'expiry': headers['expiry'],
        'uid': headers['uid'],
        'token-type': headers['token-type']
    }

    config_json = {
        'saved_headers': saved_headers,
        'data': data,
    }

    if status == 200:
        write(config_json)
        rich_print("User logged in successfully")
    else:
        rich_print("Error logging in")


@cli.command(help="Logout from Labor")
def sign_out():
    logged_user = load()
    headers = logged_user['saved_headers']
    status = _sign_out(headers)
    if status == 200:
        write({})
    else:
        rich_print('Error while signing out')


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
            rich_print(printTasks(dict.items(data), projects, wage))
        else:
            rich_print(f"Error while retrieving data: {status}")
    except OSError:
        rich_print(f"You need to login first, error: {OSError}")


@cli.command(help="Get reports")
@click.argument("year", required=False)
def reports(year):
    try:
        if not year:
            year = datetime.now().year
        logged_user = load()
        data, status = _reports(logged_user, year)
        if status == 200:
            rich_print(print_reports(data))
    except:
        rich_print("You need to login first")


# Labor projects
@cli.command(help="List all projects")
def projects():
    try:
        rich_print("List all projects")
    except:
        rich_print("You need to login first")


# Labor add <project> <start> <end> <day> <description>
@cli.command(help="Add a new task")
def add():
    try:
        rich_print("Add a new task")
    except:
        rich_print("You need to login first")


# Labor edit <task_id> <project> <start> <end> <day> <description>
@cli.command(help="Edit a task")
def edit():
    try:
        rich_print("Edit a task")
    except:
        rich_print("You need to login first")


# Labor delete <task_id>
@cli.command(help="Delete a task by ID")
def delete():
    try:
        rich_print("Delete a task by ID")
    except:
        rich_print("You need to login first")


if __name__ == "__main__":
    cli()
