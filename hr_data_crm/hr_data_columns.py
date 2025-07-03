import pandas as pd
import numpy as np

# loading CSV
df = pd.read_csv('C:/Users/PC/OneDrive/Desktop/hr_data_crm/hr_data.csv')

# assigning job level
def classify_job_level(row):
    if row['number_project'] <= 2 and row['time_spend_company'] <= 2:
        return 'Entry'
    elif 3 <= row['number_project'] <= 5:
        return 'Mid'
    elif row['number_project'] > 5 or row['time_spend_company'] >= 5:
        return 'Senior'
    return 'Mid'

df['job_level'] = df.apply(classify_job_level, axis=1)

# assigning exact salary
def assign_salary(row):
    band, level = row['salary'], row['job_level']
    ranges = {
        'low': {'Entry': (30000, 40000), 'Mid': (40000, 50000), 'Senior': (50000, 60000)},
        'medium': {'Entry': (40000, 50000), 'Mid': (50000, 70000), 'Senior': (70000, 90000)},
        'high': {'Entry': (50000, 60000), 'Mid': (70000, 90000), 'Senior': (90000, 120000)},
    }
    return np.random.randint(*ranges[band][level])

df['exact_salary'] = df.apply(assign_salary, axis=1)

# assigning gender
np.random.seed(42)
df['gender'] = np.random.choice(['Male', 'Female'], size=len(df), p=[0.55, 0.45])

# assigning age
def assign_age(level):
    return {
        'Entry': np.random.randint(22, 30),
        'Mid': np.random.randint(28, 40),
        'Senior': np.random.randint(35, 55)
    }[level]

df['age'] = df['job_level'].apply(assign_age)

# Saving new CSV
df.to_csv('enhanced_hr_data.csv', index=False)
