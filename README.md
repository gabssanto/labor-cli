# labor-cli
CLI for getLabor

# Install
```
pip install labor
```

# Examples
```
❯ labor sign-in
❯ labor tasks
❯ labor tasks 1 2022
❯ labor reports
❯ labor reports 2021
```

# Commands
```
❯ labor --help
Usage: labor [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  reports   Get reports, default is current year, use year in numbers
  sign-in   Login to Labor
  sign-out  Logout from Labor
  tasks     Default is current month, use month and year in numbers
```

# Development
```
❯ poetry build
```

## Local run
```
❯ python3 labor/cli.py <command>
```

## Publish
```
❯ poetry publish --build
```
