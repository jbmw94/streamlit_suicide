#vérifie les 3 dataset sur le nombre de pays, s'ils sont dupliqué ou manquant


import pandas as pd

df_suicide_2016_processed = pd.read_csv('suicide.csv')
df_happy = pd.read_csv('happy.csv')
df_homocide = pd.read_csv('homicide_rate_clean.csv')

def get_len_country(df):
    number_unique_country = len(df.country.unique())
    print(f"- {number_unique_country} unique countries")

def check_if_duplicate(df):
    has_duplicate = df.country.duplicated().any()
    print(f"- has duplicated countries : {has_duplicate}")
    
def get_missing_courntry(set1, set2):
    return list(set1 - set2)
    
def check_similar_country(df1, *args):
    for df in args:
        set_colu_df1, set_colu_df2 = set(df1.country.unique()), set(df.country.unique())
        is_subset = set_colu_df1.issubset(set_colu_df2)
        print(f"All countries in df1 are present in df2 : {is_subset}")
        if not is_subset:
            missing_col = get_missing_courntry(set_colu_df1, set_colu_df2)
            print(f"missing col in df2 {missing_col}")
    
