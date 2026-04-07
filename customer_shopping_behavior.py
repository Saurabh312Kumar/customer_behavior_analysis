from sqlalchemy import create_engine
import pandas as pd



pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)


df=pd.read_csv("customer_shopping_behavior.csv")

print(df.info())
print(df.describe())
print(df.head(3))

print(df.isnull().sum())  #checking for null values
#there is null values in Review Rating column, then we are filling null values according to their respective category
df["Review Rating"]=df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum()) # now there is no null value

#coverting column names to camel casing:
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

#creating a new column age_group:
labels=['Young Adult','Adult','Middle Age','Senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age', "age_group"]].head(10))

# create column purchase_frequency_days:
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)
print(df[["frequency_of_purchases","purchase_frequency_days"]].head(10))


#droping column
print(df[['discount_applied','promo_code_used']].head(10))
print((df['discount_applied']==df['promo_code_used']).all())

df=df.drop('promo_code_used',axis=1)
print(df.columns)


#connecting to my sql:
#step1:Mysql connection
username="root"
password="Admin123"
host="localhost"
port="3306"
database="customer_behavior"

engine=create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

#step2:write dataframe to mysql
table_name="customer"
df.to_sql(table_name,engine,if_exists="replace",index=False)

print(f"data successfully loaded into table:{table_name} in database:{database}")

#step3:read back sample(optional)
#pd.read_sql("SELECT * FROM customer LIMIT 5;",engine)



