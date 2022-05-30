# log4me

A simple python logger for personal usage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/nagstable/) to install foobar.

```bash
pip install log4me
```

## Usage

```python
import log4me

# Init the logger                 # Create the dictionary
log = log4me.Logger("ServerLog", "./log/")

# And log
log.info("New Connection", "Address ... joined")

log.success("Created", "New file created")

log.warning("Lates version", "Client have not the latest version")

log.error("File", "Cant write to file")
```

## License
[MIT](https://choosealicense.com/licenses/mit/)