## Session 2 - Data Exploration and Prepprocessing

---

## Topics to work on in this session

1. Load data
2. Pandas
3. Dataframes

## Dataframe

Is a bidimentional data structure, similar to a table, used to store and manipulate data efficiently.

#### Key features

1. Organized in row and columns
2. Contains varius types of data
3. Labeled
4. Variable size

```python
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

data = pd.DataFrame({'COL1': [1,2,3],
                     'COL2': [4,5,6],
                     'COL3': [7,8,9]
                    },
                    index=['x', 'y', 'z']
                    )


```

A dataframe in Pandas essentially a collection of Series that share the same index. Each Column is a Series.

## Series

Similar to a column in a spreadsheet or a list of values Unidimentional.

```python
24
25
78
45
34
```

### Key features

1. Stores data of only one type
2. Has an index
3. It can be created fron different data structures (list, tuples, array de Numpy or dictionaries)

```Python
import pandas as pd

numbers = pd.Series([25, 30, 22, 28])
numbers
```

```Text
0 25
1 30
2 22
3 28
dtype: int64
```
