# autoplotlib
Create matplotlib plots from language prompt (e.g. "create plot with x-axis time"). Experimental package.

> **Warning**
> This package is experimental. The package can execute code output from language models and is thus to be used with care.

## Installation

```
pip install autoplotlib
```

## Usage

```python
# set the OpenAI API key
import os
os.environ["OPENAI_API_KEY"] = <YOUR_API_KEY>

import autoplotlib as aplt
import pandas as pd

# example dataframe
data = pd.DataFrame(
    [
        [29, 177],
        [33, 186],
        [48, 161],
        [53, 173],
        [67, 152],
    ],
    index=["Alice", "Bob", "Charlie", "Dave", "Eve"],
    columns=["age", "height"],
)

figure_description = """
Plot the data as scatterplot between height and age.
Add the names as labels next to the data points.
Ensure the labels don't overlap.
Mark people taller than 170 with a star instead of a point.
"""

code, fig, llm_response = aplt.plot(figure_description, data=data)
```

## Development

### Setup

1. Fork the repository.

2. Clone the repository:
    ```
    git clone <yourforkpath>
    ```

3. Install the package in development mode:
    ```
    pip install -e ".[dev]"
    ```

## TODOs

- [ ] Add sandboxing of code execution ([see here](https://stackoverflow.com/questions/3068139/how-can-i-sandbox-python-in-pure-python#3068475))