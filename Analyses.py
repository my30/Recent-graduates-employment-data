import pandas as pd

all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')
print('2:', all_ages.head(5), recent_grads.head(5))

print('3:', all_ages['Major_category'].unique())


def total_number_in_a_category(dataframe):
    major_category = dataframe['Major_category'].unique()
    major_people_dictionary = {}
    for major in major_category:
        valid_entries = dataframe[dataframe['Major_category'] == major]
        total_number_of_people = valid_entries['Total'].sum()
        major_people_dictionary[major] = total_number_of_people
    return major_people_dictionary


aa_cat_counts = total_number_in_a_category(all_ages)
rg_cat_counts = total_number_in_a_category(recent_grads)
print('3:', rg_cat_counts)

low_wage_percent = recent_grads['Low_wage_jobs'].sum() / recent_grads['Total'].sum()
print('4:', low_wage_percent)

majors = recent_grads['Major'].unique()
rg_lower_count = 0
for major in majors:
    recent_grads_data = recent_grads[recent_grads['Major'] == major]
    all_ages_data = all_ages[all_ages['Major'] == major]
    recent_grads_unemployment_rate = recent_grads_data.iloc[0, 14] # column15 is 'Unemployment_rate'
    all_ages_unemployment_rate = all_ages_data.iloc[0]['Unemployment_rate'] # to play with .iloc
    if recent_grads_unemployment_rate < all_ages_unemployment_rate:
        rg_lower_count += 1

print('5:', rg_lower_count)