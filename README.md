# pandaq: An easy pandas query-string builder

[![test](https://github.com/eholic/pandaq/actions/workflows/test.yml/badge.svg)](https://github.com/eholic/pandaq/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/eholic/pandaq/graph/badge.svg?token=ZSTNMVJAAX)](https://codecov.io/gh/eholic/pandaq)
[![PyPI - Version](https://img.shields.io/pypi/v/pandaq.svg)](https://pypi.org/project/pandaq)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pandaq.svg)](https://pypi.org/project/pandaq)

![](./demo.gif)

This library provides `q` method for easy querying of `pandas.DataFrame`.
Internally, `q` generates the query string for [pandas.DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html).

The goal of `pandaq` is to save time when querying.

## Installation

```console
pip install pandaq
```

## Usage

`pandaq` provides two ways to select `pandas.DataFrame` rows by query string.

#### A. Generate a query-string

```python
from pandaq import Q
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
qstr = Q().q(PassengerId=1)  # -> "PassengerId==1"
df.query(qstr)
```

#### B. Add `q` method to `pandas.DataFrame`

```python
import pandaq.patch
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.q(PassengerId=1)
```

## How to construct a query

### Basics

| Query Type          | How It Works                                                                |
| ------------------- | --------------------------------------------------------------------------- |
| q("str")            | Equivalent to `pd.DataFrame.query("str")`                                   |
| q(dict)             | Works like q(\*\*dict)                                                      |
| q(k=v)              | Where the column named `k` is equal to `v`                                  |
| q(k=[v1, ...])      | Where the column named `k` is in [`v1`, ...]                                |
| q(k=(op1, v1, ...)) | Where the column named `k` meets the condition `k op1 v1 and ...`           |
| q(k="!str")         | Where the column named `k` is NOT `str` (see [Advance](#advance))           |
| q(k="?str")         | Where the column named `k` contains `str` (see [Advance](#advance))         |
| q(k="!?str")        | Where the column named `k` does NOT contain `str` (see [Advance](#advance)) |
| q(k="/str")         | Where the column named `k` match the regex `str` (see [Advance](#advance))  |

#### Example

| Type     | Kind              | pandaq.q                        | Equivalent to query-string                               |
| -------- | ----------------- | ------------------------------- | -------------------------------------------------------- |
| Number   | Equal             | `q(a=1)`                        | `"a==1"`                                                 |
| Number   | Contain           | `q(a=[1, 2])`                   | `"a==1 or a==2"`                                         |
| Number   | Inequality        | `q(a=(">", 1))`                 | `"a>1"`                                                  |
| Number   | Inequality        | `q(a=(">", 1, "<=", 3))`        | `"a>1 and a<=3"`                                         |
| Bool     | Equal             | `q(a=True)`                     | `"a==True"`                                              |
| Str      | Full-Match        | `q(a="text")`                   | `'a=="text"'`                                            |
| Str      | Not Full-Match    | `q(a="!text")`                  | `'a!="text"'`                                            |
| Str      | Partial-Match     | `q(a="?text")`                  | `'a.str.contains("text", regex=False, na=False)'`        |
| Str      | Not Partial-Match | `q(a="!?text")`                 | `'not a.str.contains("text", regex=False, na=False)'`    |
| Str      | Regex-Match       | `q(a="/textA\|textB")`          | `'a.str.contains("textA\|textB", regex=True, na=False)'` |
| Datetime | Equal             | `q(a=dt.date(1970,1,1))`        | `'a=="1970-01-01"'`                                      |
| Datetime | Inequality        | `q(a=(">", dt.date(1970,1,1)))` | `'a>"1970-01-01"'`                                       |

### Combination

| pandaq.q        | Equivalent to query-string |
| --------------- | -------------------------- |
| `q(a=1, b=1)`   | `"(a==1 & b==1)"`          |
| `q(a=1).q(b=1)` | `"a==1 & b==1"`            |

## Advanced Usage

To set the `prefix` individually, configure the following settings.

```python
from pandaq import config

# Default settings
config.str_prefix = StringPrefix(
    neq="!",  # The prefix for not equal
    regex="/",  # The prefix for regular expressions
    partial="?",  # The prefix for partial match
    neq_partial="!?",  # The prefix for not equal partial match
)
```

## License

`pandaq` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
