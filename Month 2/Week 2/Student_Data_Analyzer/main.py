import pandas as pd

df = pd.read_csv("input.csv", na_values=["None"])

df.drop_duplicates(inplace=True)
df['name'] = df['name'].fillna('Unknown')
int_col = df.select_dtypes(include=['number']).columns
df[int_col] = df[int_col].fillna(0,inplace=True)

df['avg'] = df[['s1','s2','s3']].mean(axis=1)

def get_grade(x):
    if x > 80:
        return "A"
    elif x > 60:
        return "B"
    else:
        return "C"

df['grade'] = df['avg'].apply(get_grade)
print(df)

print("-----------------------------------------------")

print("Topper Students : ")
toppers_df = df.sort_values('avg', ascending=False).head(3)
print(toppers_df)
toppers_df.to_csv("toppers.csv", index=False)