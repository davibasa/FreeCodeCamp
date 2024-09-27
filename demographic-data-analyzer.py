import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people with a Bachelor's degree?
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    # 4. Percentage of people with advanced education (Bachelors, Masters, or Doctorate) who earn >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = (df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100

    # 5. Percentage of people without advanced education who earn >50K
    lower_education = ~higher_education
    lower_education_rich = (df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100

    # 8. What country has the highest percentage of people that earn >50K?
    country_salary_df = df[df['salary'] == '>50K'].groupby('native-country').size()
    total_people_by_country = df.groupby('native-country').size()
    highest_earning_country_percentage = (country_salary_df / total_people_by_country * 100).idxmax()
    highest_earning_country_percentage_value = (country_salary_df / total_people_by_country * 100).max()

    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_IN_occupation = india_occupations.value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country_percentage)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage_value}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country_percentage,
        'highest_earning_country_percentage': highest_earning_country_percentage_value,
        'top_IN_occupation': top_IN_occupation
    }
