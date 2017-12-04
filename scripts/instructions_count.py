import pandas as pd
import sys

if(len(sys.argv) != 2):
    print('Usage: python instructions_count.py file_name')
    exit(0)

np = pd.read_csv(sys.argv[1], ' ')

# total sums
beforeTotal = np['beforeI'].sum()
afterTotal = np['afterI'].sum()
print('Total before instrumentation')
print(beforeTotal)
print('Total after instrumentation')
print(afterTotal)

# sum of inserted calls
insertedTotal = afterTotal - beforeTotal
print('Sum of inserted calls')
print(insertedTotal)

# mean of inserted calls
insertedAvg = insertedTotal / np['beforeI'].count()
print('Avg of inserted calls')
print(insertedAvg)



