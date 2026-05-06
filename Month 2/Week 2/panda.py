import pandas as pd

data = {
    "name": ["Prajwal", "Rohit", "Mosin"],
    "marks": [85, 90, 88]
}
# Creating Dataframe
df = pd.DataFrame(data)
print(df)

# Getting row with index
print("Getting value of index 0 :\n",df.loc[0])
print("\n----------------------\n")



print("Dataframe Heads : \n",df.head())
print("\n----------------------\n")
print("Dataframe Tails : \n",df.tail())
print("\n----------------------\n")
print("Dataframe Info : \n",df.info())
print("\n----------------------\n")
print("Dataframe Discription : \n",df.describe())
print("\n----------------------\n")


# Series
l = [1, 7, 2]
s = pd.Series(l)
print("Series :\n",s)
print("\n----------------------\n")


# Giving Labels to Series
s = pd.Series(l, index = ["x","y", "z"])
print("Labeled Series : \n",s)
print("Value of 'y' : ",s["y"])
print("\n----------------------\n")

# Key-Value to Series
numbers = {"one" : 1, "two" : 2, "three" : 3}
s = pd.Series(numbers)
print("Dict to series : \n", s)
print("\n----------------------\n")



data = {
    "name": ["Rohit", "Raj", "Rahul", "Rajesh", "Rohit"],
    "marks": [85, 90, 88, None, 85]
}

df = df.fillna(0)       # replace nulls
df = df.dropna()        # remove nulls

df = df.drop_duplicates()   # removing duplicates

df.rename(columns={"marks": "score"}, inplace=True) # Renaming column

print("New DF : \n",df)
print("\n----------------------\n")


# Filter students with marks > 85
filtered = df[df["score"] > 85]
print("Filtered DF : \n",filtered)
print("\n----------------------\n")


# Add new column
df["grade"] = df["score"].apply(lambda x: "A" if x > 85 else "B")
print("With Grade Column : \n", df)
print("\n----------------------\n")

df.to_csv("output.csv", index=False)