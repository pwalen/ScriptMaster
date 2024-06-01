import pandas as pd
import numpy as np

# here are ten different performance test names
text = '''
Load Testing
Stress Testing
Spike Testing
Endurance Testing
Scalability Testing
Volume Testing
Capacity Testing
Reliability Testing
Benchmark Testing
Soak Testing
'''

# From the text above, please create a list of 20 names. Each name should contain the test name in ALL UPPERCASE, with underscores instead of spaces. After the name, please add an underscore followed by '0' and '5' (each of the 10 names in 2 variants).

text = text.upper().replace(' ', '_').strip()
words = text.split('\n')
test_names = [f'{word}_{num}' for word in words for num in [0, 5]]

# Create 4 column names
headers = ['distro', 'temp_a', 'temp_b', 'end_value']

### Create a data frame, where:
# 1. column names == column_names,
# 2. 1st column is float, other int
### Fill it with random numbers, where:
# 3. 1st col: XXXX.XXX, 2nd and 3th: XX, 4th: XXXX
### Ranges:
# 4. 1st col: 1000.000 - 9999.999, 2nd and 3th: 70 - 80, 4th: 1300 - 1400

def create_df(headers, test):
    data = {
        headers[0]: np.round(np.random.uniform(1000, 9999.999, size=10), 3),
        headers[1]: np.random.randint(70, 80, size=10),
        headers[2]: np.random.randint(70, 80, size=10),
        headers[3]: np.random.randint(1300, 1400, size=10),        
    }
    df = pd.DataFrame(data)
    df.to_csv(f'{test}.csv', index=False)

for test in test_names:
    create_df(headers, test)