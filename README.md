# autoplotlib
Create matplotlib plots from language prompt (e.g. "create plot with x-axis time"). Experimental package.

> **Warning**
> This package is experimental. The package can execute code output from language models and is thus to be used with care.

## Installation

```
pip install autoplotlib
```

## Usage

```
import autoplotlib as aplt

# set the OpenAI API key
import os
os.environ["OPENAI_API_KEY"] = <YOUR_API_KEY>

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a plot with x-axis time
aplt.plot("create plot with x-axis time")
```

## Development

### Setup

1. Fork the repository

2. Clone the repository
    ````
    git clone <yourforkpath>
    ```

3. Install the package in development mode
    ```
    pip install -e ".[dev]"
    ```

## TODOs

- [ ] Add sandboxing of code execution ([see here](https://stackoverflow.com/questions/3068139/how-can-i-sandbox-python-in-pure-python#3068475))