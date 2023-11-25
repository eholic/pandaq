import pandas as pd

import pandaq.patch


def test_df_q():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    assert df.q(a=1).shape[0] == 1
    assert df.q(a=[1, 2]).shape[0] == 2
    assert df.q(b=4).shape[0] == 1
