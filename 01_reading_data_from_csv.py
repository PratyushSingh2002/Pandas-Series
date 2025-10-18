import pandas as pd

# 1️⃣ CSV file ko read karna
df = pd.read_csv("/home/pratyush/Desktop/Pandas/global_population_stats_2024.csv")

# 2️⃣ Pure DataFrame print karna (warning: large dataset ho toh terminal clutter ho sakta hai)
print("==== Pure DataFrame ====")
print(df)

# 3️⃣ Starting 5 rows
print("\n==== First 5 rows ====")
print(df.head(5))

# Last 5 rows
print("\n==== Last 5 rows ====")
print(df.tail(5))

# 4️⃣ Rows slicing: row 4 se 6 (Python indexing 0 se start hoti hai)
print("\n==== Rows 4 to 6 ====")
rows_subset = df[3:6]  # 3 index = row 4, 6 excluded
print(rows_subset)

# 5️⃣ Specific columns select karna (e.g., 'Country' aur 'Population')
print("\n==== Specific Columns: Country & Population ====")
columns_subset = df[['Country', 'Population Aged 0 to 14 (%)']]
print(columns_subset.head())  # sirf first 5 rows for display

# 6️⃣ Rows + Columns dono select karna
# Using loc (row labels included)
print("\n==== Rows 3 to 6 and Columns Country & Population using loc ====")
subset_loc = df.loc[3:6, ['Country', 'Population Aged 0 to 14 (%)']]
print(subset_loc)

# Using iloc (index based)
print("\n==== Rows 3 to 5 and Columns index 0 & 2 using iloc ====")
subset_iloc = df.iloc[3:6, [0, 2]]
print(subset_iloc)


