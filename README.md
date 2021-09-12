Cargo API
==

This project implements a REST API for a system with the following structure:

- Fleet Model:
```json
{
  "id": "FL_001",
  "name": "Den Haag"
}
```
- Bike Model:
```json
{
  "id": "BK_001",
  "fleet": "FL_001",
  "status": "unlocked",
  "location": {
    "latitude": 52.08466738004343,
    "longitude": 4.3185523728791075
  }
}
```

## Setup
### Requirements
All the dev dependencies are managed by [Poetry](https://python-poetry.org/). Most of the commands can be executed with the prefix `poetry run` or entering in the python virtual environment through the command `poetry shell`.


Once this tool is installed, you can execute the command:

- `poetry install`

to install the project dependencies specified in the file `pyproject.toml`

### Load initial data

To load the initial sample data for this project, run the command (from the project root):

```bash
poetry run cargo/manage.py importdata misc/data.json
```

## Tests

There are unit tests for teh basic flow that be executed with the command:

```bash
poetry run cargo/manage.py test cargo
```

## Running the server

To run a local server, run the command below:

```bash
poetry run cargo/manage.py runserver
```
The server API will be available in `http://127.0.0.1:8000/api/`. You need to access the specific namespace from each resource (bikes and fleets) in order use them. Check the live documentation for more details.

## Documentation

The API is docummented in the live documentation available (when the server is up) in `http://127.0.0.1:8000/docs/`. You can check the available resources and their attributes there.
