import pandas as pd
from cerinta1 import cerinta1
from cerinta2 import cerinta2
from cerinta3 import cerinta3
from cerinta4 import cerinta4
from cerinta5 import cerinta5
from cerinta6 import cerinta6
from cerinta7 import cerinta7
from cerinta8 import cerinta8
from cerinta9 import cerinta9
from cerinta10 import cerinta10

df = pd.read_csv('./titanic/train.csv', index_col=0)
cerinta1(df)
cerinta2(df)
cerinta3(df)
cerinta4(df)
cerinta5(df)
cerinta6(df)
cerinta7(df)
cerinta8(df)
cerinta9(df)
cerinta10(df)
