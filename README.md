# pandaq: An easy pandas query-string builder

[![test](https://github.com/eholic/pandaq/actions/workflows/test.yml/badge.svg)](https://github.com/eholic/pandaq/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/eholic/pandaq/graph/badge.svg?token=ZSTNMVJAAX)](https://codecov.io/gh/eholic/pandaq)
[![PyPI - Version](https://img.shields.io/pypi/v/pandaq.svg)](https://pypi.org/project/pandaq)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pandaq.svg)](https://pypi.org/project/pandaq)

`pandaq` generates the query string of [pandas.DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html).

- [pandaq: An easy pandas query-string builder](#pandaq-an-easy-pandas-query-string-builder)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)

## Installation

```console
pip install pandaq
```

## Usage

`pandaq` provides two ways to select DataFrame rows by query string.

<details>
<summary>1. Generate a query-string</summary>
```python
from pandaq import Q
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
df.query(Q().q(PassengerId=1))
```
</details>

<details>
<summary>2. Extend `pandas.DataFrame` </summary>
```python
import pandaq.patch
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
df.q(PassengerId=1)
```
</details>

| pandaq.q              | equivalent to query                                 |
| --------------------- | --------------------------------------------------- |
| q(a=1)                | "a==1"                                              |
| q(a=True)             | "a==True"                                           |
| q(a="text")           | 'a=="text"'                                         |
| q(a="!text")          | 'a!="text"'                                         |
| q(a="/text")          | 'a.str.contains("text", regex=True, na=False)'      |
| q(a="?text")          | 'a.str.contains("text", regex=False, na=False)'     |
| q(a="!?text")         | 'not a.str.contains("text", regex=False, na=False)' |
| q(a=[1, 2])           | "a==1 or a==2"                                      |
| q(a=(">", 1))         | "a>1"                                               |
| q(a=(">", 1, "<", 3)) | "a>1 and a<3"                                       |
| q(a=1, b=1)           | "a==1 & b==1"                                       |

## License

`pandaq` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
