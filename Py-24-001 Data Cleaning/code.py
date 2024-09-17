# Drop rows with missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df_filled = df.fillna(0)

# Fill missing values with the mean, median, or mode of the column
df['column_name'].fillna(df['column_name'].mean(), inplace=True)
df['column_name'].fillna(df['column_name'].median(), inplace=True)
df['column_name'].fillna(df['column_name'].mode()[0], inplace=True)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows where a value is beyond 3 standard deviations from the mean
df = df[(np.abs(df['column_name'] - df['column_name'].mean()) <= (3*df['column_name'].std()))]

# Convert a column to datetime format (invalid dates will become NaT)
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')
# Convert a column to numeric (invalid values will become NaN)
df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')
# Convert a column to string
df['string_column'] = df['string_column'].astype(str)
# Convert a column to boolean (non-zero values become True, zero becomes False)
df['boolean_column'] = df['boolean_column'].astype(bool)
# Convert a column to integer (non-integer values will raise an error unless 'coerce' is used)
df['integer_column'] = pd.to_numeric(df['integer_column'], errors='coerce').fillna(0).astype(int)
# Convert a column to float
df['float_column'] = df['float_column'].astype(float)
# Convert a column with binary-like values to boolean (e.g., 'yes'/'no', 1/0)
df['binary_column'] = df['binary_column'].map({'yes': True, 'no': False, 1: True, 0: False})
# Convert currency formatted string (e.g., '$1,234.56') to float
df['currency_column'] = df['currency_column'].replace({'\$': '', ',': ''}, regex=True).astype(float)
# Convert numeric to currency formatted string (e.g., '$1,234.56')
df['currency_column'] = df['currency_column'].apply(lambda x: f"${x:,.2f}")
# Convert percentage formatted string (e.g., '75%') to float
df['percentage_column'] = df['percentage_column'].replace({'%': ''}, regex=True).astype(float) / 100
# Convert numeric to percentage formatted string (e.g., '75%')
df['percentage_column'] = df['percentage_column'].apply(lambda x: f"{x * 100:.2f}%")
# Convert fraction formatted string (e.g., '1/2') to float
from fractions import Fraction
df['fraction_column'] = df['fraction_column'].apply(lambda x: float(Fraction(x)))
# Convert numeric to fraction formatted string (e.g., '1/2')
from fractions import Fraction
df['fraction_column'] = df['fraction_column'].apply(lambda x: str(Fraction(x).limit_denominator()))
# Convert scientific notation string (e.g., '1e-3') to float
df['scientific_column'] = df['scientific_column'].astype(float)
# Convert float to scientific notation string (e.g., '1.00e+03')
df['scientific_column'] = df['scientific_column'].apply(lambda x: f"{x:.2e}")


# Strip leading/trailing whitespaces
df['string_column'] = df['string_column'].str.strip()

# Convert to lowercase
df['string_column'] = df['string_column'].str.lower()

# Replace specific characters or patterns
df['string_column'] = df['string_column'].str.replace('-', ' ', regex=False)

# Rename columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)
# Replace spaces in column names with underscores
df.columns = df.columns.str.replace(' ', '_')

# Save to CSV. Change 'cleaned_data to file name of your choice
df_cleaned.to_csv('cleaned_data.csv', index=False)
# Save to Excel. Change 'cleaned_data to file name of your choice
df_cleaned.to_excel('cleaned_data.xlsx', index=False)

