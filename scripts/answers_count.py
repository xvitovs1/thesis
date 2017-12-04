import pandas as pd
import sys

if(len(sys.argv) != 2):
    print('Usage: python instructions_count.py file_name')
    exit(0)

np = pd.read_csv(sys.argv[1], ' ')

timeout = np.query("result=='TIMEOUT'")['result'].count()
true = np.query("result=='TRUE'")['result'].count()
false = np.query("result=='FALSE'")['result'].count()
unknown = np.query("result=='UNKNOWN'")['result'].count()
print('True')
print(true)
print('False')
print(false)
print('Unknown')
print(unknown)
print('Timeout')
print(timeout)



