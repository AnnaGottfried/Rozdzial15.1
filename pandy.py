import pandas as pd

salaries = [
	("Mark", 1000),
	("John", 1500),
	("Daniel", 2300),
	("Greg", 5000)
]

names_series = pd.Series(["Mark", "John", "Daniel", "Greg"])
salary_series = pd.Series([1000, 1500, 2300, 5000])
salary_series.index = names_series
names_series.describe()

names = ["Mark", "John", "Daniel", "Greg"]
salaries = [1000, 1500, 2300, 5000]
salary_series_improved = pd.Series(salaries, index=names)
print(salary_series_improved)

salaries1 = [
	("Mark", 1000, 23),
	("John", 1500, 25),
	("Daniel", 2300, 38),
	("Greg", 5000, 42)
]

df = pd.DataFrame(salaries1)
print(df)

df = pd.DataFrame(salaries1, columns=["name", "salary", "age"])
df = df.set_index("name")
print(df)
print(df.describe())

salary_increased_series = df['salary'].apply(lambda salary: salary + 2000)
df['salary'] = salary_increased_series
print(df)
df['salary'].plot(kind='bar')