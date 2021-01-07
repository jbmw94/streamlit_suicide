
import pandas as pd
#scrapping des donnée
url = "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate"
df_list = pd.read_html(url)
df = df_list[4]
df
df.to_csv('homocide_rate.csv', index = False)

#création du dataset homocide
df_homocide = pd.read_csv('homocide_rate.csv')
homicid_col = ["Country (or dependent territory, subnational area, etc.)", "Rate", "Count"]
df_homocide = df_homocide[homicid_col]
df_homocide.columns = ['country', "homicide_rate", "homicide_count"]
df_homocide.to_csv('homicide_rate_clean.csv',index=False)
 
#création du dataset happy
df_happy = pd.read_csv('2015.csv')
df_happy.rename(columns={"Country": "country"}, inplace=True)
df_happy.to_csv('happy.csv', index=False)

from utils.df_suicide import suicide_df

df_suicide_2016_processed = suicide_df('master.csv')


from utils.whole_concat import get_len_country, check_if_duplicate, check_similar_country, get_missing_courntry
d = {
    "df_suicide_2016_processed":df_suicide_2016_processed,
    "df_happy":df_happy,
    "df_homocide":df_homocide,
} 
for name, df in d.items():
    print(name)
    get_len_country(df)
    check_if_duplicate(df)
    
check_similar_country(df_suicide_2016_processed, df_happy, df_homocide)



#concaténe les 3 dataset

first_merge = df_suicide_2016_processed.merge(df_happy,on="country")
final_df = first_merge.merge(df_homocide,on="country")
# final_df.to_csv('whole_data.csv', index = False)
final_df("master.csv")

from utils.csv_sql import for_sql
for_sql(final_df)

