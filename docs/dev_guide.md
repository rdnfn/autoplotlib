
# Development guide

## Setup of dev environment

1. Fork the repository.

2. Clone the repository:
    ```
    git clone <yourforkpath>
    ```

3. Install the package in development mode:
    ```
    pip install -e ".[dev]"
    ```

    This will install the package in development mode, i.e. any changes you make to the source code will be reflected in the installed package. It will also install the development dependencies.

## Deploying a new version

A reminder for the maintainers on how to deploy. Follow this checklist (inspired by [this checklist](https://gist.github.com/audreyfeldroy/5990987) and [this packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)):

1. Update `HISTORY.rst` and commit with message like "aux: add changelog for upcoming release 0.1.0"
2. Run

    ```
    bump2version patch # possible: major / minor / patch
    ```

3. Push commits *and tags* ([from here](https://stackoverflow.com/a/66086007)):
    > you can push tags by entering `Ctrl` + `Shift` + `P` and then write `Git: Push Tags`

4. Merge pull request into ``main`` branch.
5. Add release on GitHub (using existing tag)