import click
from rich import print
from datetime import datetime

import api
import config
from sensitive_data import email, password
from beautify import printTasks, print_reports

@click.group()
def cli():
    ...


@cli.command(help="Login to Labor")
def login():
    email = click.prompt('Enter your email', type=str)
    password = click.prompt('Enter your password', type=str, hide_input=True)
    data, status, headers = api.login(email, password)

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

    # print(data)
    if status == 200: 
        config.write(config_json)
        print("User logged in successfully")
    else: print("Error logging in")

@cli.command(help="Get tasks, default is current month, use month in numbers, default for year is current year")
@click.argument("month", required=False)
@click.argument("year", required=False)
def tasks(month, year):
    try:
        if not year:
            year = datetime.now().year
        if not month: 
            month = datetime.now().month
        logged_user = config.load()
        data, status, projects = api.tasks(logged_user, month, year)
        if status == 200: 
            print(printTasks(dict.items(data), projects))
        else: 
            print(f"Error while retrieving data: {status}")
    except: 
        print("You need to login first")

@cli.command(help="Get reports")
@click.argument("year", required=False)
def reports(year):
    try: 
        if not year:
            year = datetime.now().year
        logged_user = config.load()
        data, status = api.reports(logged_user, year)
        if status == 200:
            print(print_reports(data))
    except:
        print("You need to login first")

# @cli.command(help="Train station updates")
# @click.argument("station", required=True)
# @click.option(
#     "-f",
#     "--follow",
#     is_flag=True,
#     default=False,
#     help="Keep watching for updates every couple of seconds",
# )
# def live(station, follow):
#     commands.live(station, follow)


if __name__ == "__main__":
    cli()
