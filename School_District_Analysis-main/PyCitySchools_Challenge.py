#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[2]:


# Add the Pandas dependency.
import pandas as pd
import os


# In[3]:


# Files to load
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")
clean_data_to_load = os.path.join("Resources", "clean_students_complete.csv")


# In[4]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[5]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()


# In[6]:


# Determine if there are any missing values in the school data.
school_data_df.count()


# In[7]:


# Determine if there are any missing values in the student data.
student_data_df.count()


# In[8]:


# Determine if there are any missing values in the school data.
school_data_df.isnull()


# In[9]:


# Determine if there are any missing values in the student data.
student_data_df.isnull()


# In[10]:


# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# In[11]:


# Determine if there are not any missing values in the school data.
school_data_df.notnull()


# In[12]:


# Determine if there are not any missing values in the student data.
student_data_df.notnull().sum()


# In[13]:


# Determine data types for the school DataFrame.
school_data_df.dtypes


# In[14]:


# Determine data types for the student DataFrame.
student_data_df.dtypes


# In[15]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[16]:


# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")


# In[17]:


student_data_df[0:10]


# In[18]:


# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# In[19]:


# Get the total number of students.
student_count = school_data_complete_df.count()
student_count


# In[20]:


school_data_complete_df["Student ID"].count()


# In[21]:


# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count


# In[22]:


# Calculate the total number of schools
school_count_2 = school_data_complete_df["school_name"].unique()
school_count_2


# In[23]:


# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget


# In[24]:


# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[25]:


# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[26]:


passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70


# In[27]:


# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()


# In[28]:


# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]


# In[29]:


passing_math["student_name"].count()


# In[30]:


# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()
print(passing_math_count)


# In[31]:


# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()
print(passing_reading_count)


# In[32]:


# Calculate the students who passed both math and reading.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

passing_math_reading.head()


# In[33]:


# Calculate the number of students who passed both math and reading.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_math_reading_count


# In[34]:


# Calculate the overall passing percentage.
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
overall_passing_percentage


# In[35]:


district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count, 
          "Total Students": student_count, 
          "Total Budget": total_budget,
          "Average Math Score": average_math_score, 
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


# In[ ]:


# Define a function that calculates the percentage of students that passed both # math and reading and prints the passing percentage to the output when the
# function is called.
def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100


# In[ ]:


passing_math_count = 29370
total_student_count = 39170


# In[ ]:


# Call the function
passing_math_percent(passing_math_count, total_student_count)


# In[ ]:


# A list of my grades.
my_grades = ['B', 'C', 'B' , 'D']


# In[ ]:


# Import pandas.
import pandas as pd
# Convert the my_grades to a Series
my_grades = pd.Series(my_grades)
my_grades


# In[ ]:


# Change the grades by one letter grade.
my_grades.map({'B': 'A', 'C': 'B', 'D': 'C'})


# In[ ]:


# Using the format() function.
my_grades = [92.34, 84.56, 86.78, 98.32]

for grade in my_grades:
    print("{:.0f}".format(grade))


# In[ ]:


# Convert the numerical grades to a Series.
my_grades = pd.Series([92.34, 84.56, 86.78, 78.32])
my_grades


# In[ ]:


# Format the grades to the nearest whole number percent.
my_grades.map("{:.0f}".format)


# In[ ]:


# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]


# In[ ]:


# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

district_summary_df["Total Budget"]


# In[ ]:


# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[ ]:


# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df


# In[ ]:


# Determine the school type.
per_school_types = school_data_df.set_index(["school_name"])["type"]
per_school_types


# In[ ]:


# Add the per_school_types into a DataFrame for testing.
df = pd.DataFrame(per_school_types)
df


# In[ ]:


# Calculate the total student count.
per_school_counts = school_data_df["size"]
per_school_counts


# In[ ]:


# Calculate the total student count.
per_school_counts = school_data_df.set_index(["school_name"])["size"]
per_school_counts


# In[ ]:


# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_counts


# In[ ]:


# Calculate the total school budget.
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
per_school_budget


# In[ ]:


# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
per_school_capita


# In[ ]:


# Calculate the math scores.
student_school_math = student_data_df.set_index(["school_name"])["math_score"]


# In[ ]:


# Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
per_school_averages


# In[ ]:


# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]

per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]


# In[ ]:


# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]

per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]


# In[ ]:


# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]


# In[ ]:


# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100

per_school_passing_reading = per_school_passing_reading / per_school_counts * 100
print(per_school_passing_math)


# In[ ]:


# Calculate the students who passed both math and reading.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

per_passing_math_reading.head()


# In[ ]:


# Calculate the number of students who passed both math and reading.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]


# In[ ]:


# Calculate the overall passing percentage.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100


# In[ ]:


# Adding a list of values with keys to create a new DataFrame.
per_school_summary_df = pd.DataFrame({
             "School Type": per_school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})
per_school_summary_df.head()


# In[ ]:


# Format the Total School Budget and the Per Student Budget columns.
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)

per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)


# Display the data frame
per_school_summary_df.head()


# In[ ]:


# Reorder the columns in the order you want them to appear.
new_column_order = ["School Type", "Total Students", "Total School Budget", "Per Student Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
per_school_summary_df = per_school_summary_df[new_column_order]

per_school_summary_df.head()


# In[ ]:


# Sort and show top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[ ]:


# Sort and show top five schools.
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()


# In[ ]:


# Create a grade level DataFrames.
ninth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]

tenth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]

eleventh_graders = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]

twelfth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]


# In[ ]:


# Group each grade level DataFrame by the school name for the average math score.
ninth_grade_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]

tenth_grade_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]

eleventh_grade_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]

twelfth_grade_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]


# In[ ]:


# Group each grade level DataFrame by the school name for the average reading score.
ninth_grade_reading_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]

tenth_grade_reading_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]

eleventh_grade_reading_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]

twelfth_grade_reading_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]


# In[ ]:


# Combine each grade level Series for average math scores by school into a single DataFrame.
math_scores_by_grade = pd.DataFrame({
               "9th": ninth_grade_math_scores,
               "10th": tenth_grade_math_scores,
               "11th": eleventh_grade_math_scores,
               "12th": twelfth_grade_math_scores})

math_scores_by_grade.head()


# In[ ]:


# Combine each grade level Series for average reading scores by school into a single DataFrame.
reading_scores_by_grade = pd.DataFrame({
              "9th": ninth_grade_reading_scores,
              "10th": tenth_grade_reading_scores,
              "11th": eleventh_grade_reading_scores,
              "12th": twelfth_grade_reading_scores})

reading_scores_by_grade.head()


# In[ ]:


# Format each grade column.
math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.1f}".format)

math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.1f}".format)

math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.1f}".format)

math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.1f}".format)

# Make sure the columns are in the correct order.
math_scores_by_grade = math_scores_by_grade[
        ["9th", "10th", "11th", "12th"]]

# Remove the index name.
math_scores_by_grade.index.name = None
# Display the DataFrame.
math_scores_by_grade.head()


# In[ ]:


# Format each grade column.
reading_scores_by_grade["9th"] = reading_scores_by_grade["9th"].map("{:,.1f}".format)

reading_scores_by_grade["10th"] = reading_scores_by_grade["10th"].map("{:,.1f}".format)

reading_scores_by_grade["11th"] = reading_scores_by_grade["11th"].map("{:,.1f}".format)

reading_scores_by_grade["12th"] = reading_scores_by_grade["12th"].map("{:,.1f}".format)

# Make sure the columns are in the correct order.
reading_scores_by_grade = reading_scores_by_grade[
                 ["9th", "10th", "11th", "12th"]]

# Remove the index name.
reading_scores_by_grade.index.name = None
# Display the data frame.
reading_scores_by_grade.head()


# In[ ]:


# Get the descriptive statistics for the per_school_capita.
per_school_capita.describe()


# In[ ]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
pd.cut(per_school_capita, spending_bins)


# In[ ]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
per_school_capita.groupby(pd.cut(per_school_capita, spending_bins)).count()


# In[ ]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 630, 645, 675]
per_school_capita.groupby(pd.cut(per_school_capita, spending_bins)).count()


# In[ ]:


# Establish the spending bins and group names.
spending_bins = [0, 585, 630, 645, 675]
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]


# In[ ]:


# Categorize spending based on the bins.
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels=group_names)

per_school_summary_df


# In[ ]:


# Calculate averages for the desired columns.
spending_math_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]

spending_reading_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]

spending_passing_math = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]

spending_passing_reading = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]

overall_passing_spending = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]


# In[ ]:


# Assemble into DataFrame.
spending_summary_df = pd.DataFrame({
          "Average Math Score" : spending_math_scores,
          "Average Reading Score": spending_reading_scores,
          "% Passing Math": spending_passing_math,
          "% Passing Reading": spending_passing_reading,
          "% Overall Passing": overall_passing_spending})

spending_summary_df


# In[ ]:


# Formatting
spending_summary_df["Average Math Score"] = spending_summary_df["Average Math Score"].map("{:.1f}".format)

spending_summary_df["Average Reading Score"] = spending_summary_df["Average Reading Score"].map("{:.1f}".format)

spending_summary_df["% Passing Math"] = spending_summary_df["% Passing Math"].map("{:.0f}".format)

spending_summary_df["% Passing Reading"] = spending_summary_df["% Passing Reading"].map("{:.0f}".format)

spending_summary_df["% Overall Passing"] = spending_summary_df["% Overall Passing"].map("{:.0f}".format)

spending_summary_df


# In[ ]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[ ]:


# Categorize spending based on the bins.
per_school_summary_df["School Size"] = pd.cut(per_school_summary_df["Total Students"], size_bins, labels=group_names)

per_school_summary_df.head()


# In[ ]:


# Calculate averages for the desired columns.
size_math_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]

size_reading_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]

size_passing_math = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]

size_passing_reading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]

size_overall_passing = per_school_summary_df.groupby(["School Size"]).mean()["% Overall Passing"]


# In[ ]:


# Assemble into DataFrame.
size_summary_df = pd.DataFrame({
          "Average Math Score" : size_math_scores,
          "Average Reading Score": size_reading_scores,
          "% Passing Math": size_passing_math,
          "% Passing Reading": size_passing_reading,
          "% Overall Passing": size_overall_passing})

size_summary_df


# In[ ]:


# Formatting.
size_summary_df["Average Math Score"] = size_summary_df["Average Math Score"].map("{:.1f}".format)

size_summary_df["Average Reading Score"] = size_summary_df["Average Reading Score"].map("{:.1f}".format)

size_summary_df["% Passing Math"] = size_summary_df["% Passing Math"].map("{:.0f}".format)

size_summary_df["% Passing Reading"] = size_summary_df["% Passing Reading"].map("{:.0f}".format)

size_summary_df["% Overall Passing"] = size_summary_df["% Overall Passing"].map("{:.0f}".format)

size_summary_df


# In[ ]:


# Calculate averages for the desired columns.
type_math_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Math Score"]

type_reading_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Reading Score"]

type_passing_math = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Math"]

type_passing_reading = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Reading"]

type_overall_passing = per_school_summary_df.groupby(["School Type"]).mean()["% Overall Passing"]


# In[ ]:


# Assemble into DataFrame.
type_summary_df = pd.DataFrame({
          "Average Math Score" : type_math_scores,
          "Average Reading Score": type_reading_scores,
          "% Passing Math": type_passing_math,
          "% Passing Reading": type_passing_reading,
          "% Overall Passing": type_overall_passing})

type_summary_df


# In[ ]:


# Formatting
type_summary_df["Average Math Score"] = type_summary_df["Average Math Score"].map("{:.1f}".format)

type_summary_df["Average Reading Score"] = type_summary_df["Average Reading Score"].map("{:.1f}".format)

type_summary_df["% Passing Math"] = type_summary_df["% Passing Math"].map("{:.0f}".format)

type_summary_df["% Passing Reading"] = type_summary_df["% Passing Reading"].map("{:.0f}".format)

type_summary_df["% Overall Passing"] = type_summary_df["% Overall Passing"].map("{:.0f}".format)

type_summary_df


# In[ ]:


# Step 1 - Use the code snippet provided in Step 1 to import the NumPy module:
import numpy as np


# In[ ]:


# Step 2 - select all the ninth-grade reading scores at Thomas High School, use the following steps to write code inside the brackets of the loc method:
ninth_thomasHS_reading = student_data_df.loc[(student_data_df["grade"] == "9th") & (student_data_df["school_name"] == "Thomas High School"), ["reading_score"]] = "NaN" 

ninth_thomasHS_reading


# In[ ]:


# Step 3 - Refactor the code in Step 2 to replace the math scores with NaN.
ninth_thomasHS_math = student_data_df.loc[(student_data_df["grade"] == "9th") & (student_data_df["school_name"] == "Thomas High School"), ["math_score"]]  = "NaN"

ninth_thomasHS_math


# In[ ]:


# Step 4 - Check the student data for NaN's.
student_data_df


# In[ ]:


# Deliverable 2 - Repeat the School District Analysis
# Combine the data into a single dataset

school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])


# In[ ]:


# Calculate the Totals (Schools and Students)
school_count = len(school_data_complete_df["school_name"].unique())
student_count = school_data_complete_df["Student ID"].count()

# Calculate the Total Budget
total_budget = school_data_df["budget"].sum()


# In[ ]:


# Calculate the Average Scores using the "clean_student_data".
clean_student_data = school_data_complete_df.drop(school_data_complete_df.loc[(school_data_complete_df["grade"] == "9th") 
                                                                              & (school_data_complete_df["school_name"] 
                                                                                 == "Thomas High School")].index)

average_reading_score = clean_student_data["reading_score"].mean()
average_math_score = clean_student_data["math_score"].mean()


# In[ ]:


# Step 1. Get the number of students that are in ninth grade at Thomas High School
# These students have no grades
thomasHS_ninth_count = student_data_df.loc[(student_data_df["grade"] == "9th") 
                                           & (student_data_df["school_name"] == "Thomas High School"), ["Student ID"]].count()
#thomasHS_ninth_count

# Get the total student count 
student_count = school_data_complete_df["Student ID"].count()


# In[ ]:


# Step 2. Subtract the number of students that are in ninth grade at Thomas High School from the total student count to get 
# the new total student count
new_total_student_count = student_count - thomasHS_ninth_count
new_total_student_count


# In[ ]:


# Calculate the passing rates using the "clean_student_data".
passing_math_count = clean_student_data[(clean_student_data["math_score"] >= 70)].count()["student_name"]
passing_reading_count = clean_student_data[(clean_student_data["reading_score"] >= 70)].count()["student_name"]


# In[ ]:


# Step 3. Calculate the passing percentages with the new total student count.
# Percentage of students passing math
passing_math_percentage = passing_math_count / float(new_total_student_count) * 100
passing_math_percentage


# In[ ]:


# Percentage of students passing reading
passing_reading_percentage = passing_reading_count / float(new_total_student_count) * 100
passing_reading_percentage


# In[ ]:


# Calculate the students who passed both reading and math.
passing_math_reading = clean_student_data[(clean_student_data["math_score"] >= 70) 
                                          & (clean_student_data["reading_score"] >= 70)]

# Calculate the number of students that passed both reading and math.
overall_passing_math_reading = passing_math_reading["student_name"].count()


# Step 4.Calculate the overall passing percentage with new total student count.
overall_passing_percentage = overall_passing_math_reading / float(new_total_student_count) * 100
overall_passing_percentage


# In[ ]:


# Create a DataFrame
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count, 
          "Total Students": student_count, 
          "Total Budget": total_budget,
          "Average Math Score": average_math_score, 
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
          "% Passing Reading": passing_reading_percentage,
          "% Overall Passing": overall_passing_percentage}])



# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
# Format the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)
district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)
district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.1f}".format)
district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.1f}".format)
district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.1f}".format)

# Display the data frame
district_summary_df


# In[ ]:


# Determine the School Type
per_school_types = school_data_df.set_index(["school_name"])["type"]

# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()

# Calculate the total school budget and per capita spending
per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]

# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts

# Calculate the average test scores.
clean_student_data["math_score"] = clean_student_data["math_score"].astype(dtype=int)
per_school_math = clean_student_data.groupby(["school_name"]).mean()["math_score"]

clean_student_data["reading_score"] = clean_student_data["reading_score"].astype(dtype=int)
per_school_reading = clean_student_data.groupby(["school_name"]).mean()["reading_score"]

# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = clean_student_data[(clean_student_data["math_score"] >= 70)]
per_school_passing_reading = clean_student_data[(clean_student_data["reading_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100

# Calculate the students who passed both reading and math.
per_passing_math_reading = clean_student_data[(clean_student_data["reading_score"] >= 70) 
                                                 & (clean_student_data["math_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100


# In[ ]:


# Create the DataFrame
per_school_summary_df = pd.DataFrame({
    "School Type": per_school_types,
    "Total Students": per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": per_overall_passing_percentage})


# In[ ]:


# Format the Total School Budget and the Per Student Budget
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

# Display the data frame
per_school_summary_df


# In[ ]:


# Step 5.  Get the number of 10th-12th graders from Thomas High School (THS).
tenth_twelth_ths_count = clean_student_data.loc[(clean_student_data["school_name"] == "Thomas High School")].count() ["Student ID"]
#tenth_twelth_ths_count

total_budget_ths = clean_student_data.loc[(clean_student_data["school_name"] == "Thomas High School")].sum() ["budget"]
total_budget_ths


# In[ ]:


# Step 6. Get all the students passing math from THS
passing_math_ths = clean_student_data.loc[(clean_student_data["school_name"] == "Thomas High School") & (clean_student_data["math_score"] >= 70)].count()["student_name"]

average_passing_math_ths = clean_student_data.loc[(clean_student_data["school_name"] == "Thomas High School") & (clean_student_data["math_score"] >= 70)].mean()["math_score"]


# In[ ]:


# Step 7. Get all the students passing reading from THS
passing_reading_ths = clean_student_data.loc[(clean_student_data["school_name"] == "Thomas High School") & (clean_student_data["reading_score"] >= 70)].count()["student_name"]


average_passing_reading_ths = clean_student_data.loc[(clean_student_data["school_name"] == "Thomas High School") & (clean_student_data["reading_score"] >= 70)].mean()["reading_score"]


# In[ ]:


# Step 8. Get all the students passing math and reading from THS
passing_math_reading_ths_count = clean_student_data.loc[(clean_student_data["school_name"] == "Thomas High School") 
                                                       & ((clean_student_data["math_score"] >= 70) & (clean_student_data["reading_score"] >= 70))].count()["student_name"]
passing_math_reading_ths_count


# In[ ]:


# Step 9. Calculate the percentage of 10th-12th grade students passing math from Thomas High School. 
percent_passing_math_ths = passing_math_ths / float(tenth_twelth_ths_count) * 100
percent_passing_math_ths


# In[ ]:


# Step 10. Calculate the percentage of 10th-12th grade students passing reading from Thomas High School.
percent_passing_reading_ths = passing_reading_ths / float(tenth_twelth_ths_count) * 100
percent_passing_reading_ths


# In[ ]:


# Step 11. Calculate the overall passing percentage of 10th-12th grade from Thomas High School. 
overall_passing_percentage_ths = passing_math_reading_ths_count / float(tenth_twelth_ths_count) * 100
overall_passing_percentage_ths


# In[ ]:


# Step 12. Replace the passing math percent for Thomas High School in the per_school_summary_df.
# Create a DataFrame
district_summary_df_ths = pd.DataFrame([{
    "Total Schools": tenth_twelth_ths_count, 
    "Total Students": tenth_twelth_ths_count, 
    "Total Budget": total_budget_ths,
    "Average Math Score": average_passing_reading_ths, 
    "Average Reading Score": average_passing_reading_ths,
    "% Passing Math": percent_passing_math_ths,
    "% Passing Reading": percent_passing_reading_ths,
    "% Overall Passing": overall_passing_percentage_ths}])



# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df_ths["Total Students"] = district_summary_df_ths["Total Students"].map("{:,}".format)
# Format the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
district_summary_df_ths["Total Budget"] = district_summary_df_ths["Total Budget"].map("${:,.2f}".format)
# Format the columns.
district_summary_df_ths["Average Math Score"] = district_summary_df_ths["Average Math Score"].map("{:.1f}".format)
district_summary_df_ths["Average Reading Score"] = district_summary_df_ths["Average Reading Score"].map("{:.1f}".format)
district_summary_df_ths["% Passing Math"] = district_summary_df_ths["% Passing Math"].map("{:.1f}".format)
district_summary_df_ths["% Passing Reading"] = district_summary_df_ths["% Passing Reading"].map("{:.1f}".format)
district_summary_df_ths["% Overall Passing"] = district_summary_df_ths["% Overall Passing"].map("{:.1f}".format)

# Display the data frame
district_summary_df_ths


# In[ ]:


# Step 13. Replace the passing reading percentage for Thomas High School in the per_school_summary_df.
# Step 14. Replace the overall passing percentage for Thomas High School in the per_school_summary_df.
per_school_summary_df


# In[ ]:


# Sort and show top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[ ]:


# Sort and show top five schools.
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()


# In[ ]:


# Create a Series of scores by grade levels using conditionals.
#complete_students_data_df

ninth_graders = complete_students_data_df[(complete_students_data_df["grade"] == "9th")]

tenth_graders = complete_students_data_df[(complete_students_data_df["grade"] == "10th")]

eleventh_graders = complete_students_data_df[(complete_students_data_df["grade"] == "11th")]

twelfth_graders = complete_students_data_df[(complete_students_data_df["grade"] == "12th")]

# Group each school Series by the school name for the average math score.

ninth_grade_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]

tenth_grade_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]

eleventh_grade_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]

twelfth_grade_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]


# Group each school Series by the school name for the average reading score.
ninth_grade_reading_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]

tenth_grade_reading_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]

eleventh_grade_reading_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]

twelfth_grade_reading_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]
 


# In[ ]:


# Combine each Series for average math scores by school into single data frame.

math_scores_by_grade = pd.DataFrame({
               "9th": ninth_grade_math_scores,
               "10th": tenth_grade_math_scores,
               "11th": eleventh_grade_math_scores,
               "12th": twelfth_grade_math_scores})

math_scores_by_grade.head()


# In[ ]:


# Combine each Series for average reading scores by school into single data frame.
reading_scores_by_grade = pd.DataFrame({
              "9th": ninth_grade_reading_scores,
              "10th": tenth_grade_reading_scores,
              "11th": eleventh_grade_reading_scores,
              "12th": twelfth_grade_reading_scores})

reading_scores_by_grade.head()


# In[ ]:


# Format each grade column.
math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.1f}".format)

math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.1f}".format)

math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.1f}".format)

math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.1f}".format)

  # Make sure the columns are in the correct order.
math_scores_by_grade = math_scores_by_grade[
    ["9th", "10th", "11th", "12th"]]


# In[ ]:


# Remove the index.
math_scores_by_grade.index.name = None

# Display the data frame
math_scores_by_grade.head() 


# In[ ]:


# Format each grade column.
reading_scores_by_grade["9th"] = reading_scores_by_grade["9th"].map("{:.1f}".format)

reading_scores_by_grade["10th"] = reading_scores_by_grade["10th"].map("{:.1f}".format)

reading_scores_by_grade["11th"] = reading_scores_by_grade["11th"].map("{:.1f}".format)

reading_scores_by_grade["12th"] = reading_scores_by_grade["12th"].map("{:.1f}".format)
## Remove the index.
reading_scores_by_grade.index.name = None

# Display the data frame
reading_scores_by_grade.head()


# In[ ]:


# Establish the spending bins and group names.
# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()

# Calculate the total school budget and per capita spending
per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]
# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts


#Get the descriptive statistics for the per_school_capita.
per_school_capita.describe()

# Categorize spending based on the bins.

spending_bins = [0, 585, 615, 645, 675]
pd.cut(per_school_capita, spending_bins)
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]


per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels=group_names)
per_school_summary_df


# In[ ]:


# Calculate averages for the desired columns. 
spending_math_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]

spending_reading_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]

spending_passing_math = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]

spending_passing_reading = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]

overall_passing_spending = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]


# In[ ]:


# Create the DataFrame

spending_summary_df = pd.DataFrame({
          "Average Math Score" : spending_math_scores,
          "Average Reading Score": spending_reading_scores,
          "% Passing Math": spending_passing_math,
          "% Passing Reading": spending_passing_reading,
          "% Overall Passing": overall_passing_spending})

spending_summary_df


# In[ ]:


# Format the DataFrame 

spending_summary_df["Average Math Score"] = spending_summary_df["Average Math Score"].map("{:.1f}".format)

spending_summary_df["Average Reading Score"] = spending_summary_df["Average Reading Score"].map("{:.1f}".format)

spending_summary_df["% Passing Math"] = spending_summary_df["% Passing Math"].map("{:.0f}".format)

spending_summary_df["% Passing Reading"] = spending_summary_df["% Passing Reading"].map("{:.0f}".format)

spending_summary_df["% Overall Passing"] = spending_summary_df["% Overall Passing"].map("{:.0f}".format)

spending_summary_df


# In[ ]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
# Categorize spending based on the bins.
per_school_summary_df["School Size"] = pd.cut(per_school_summary_df["Total Students"], size_bins, labels=group_names)


# In[ ]:


# Calculate averages for the desired columns. 
size_math_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]

size_reading_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]

size_passing_math = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]

size_passing_reading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]

size_overall_passing = per_school_summary_df.groupby(["School Size"]).mean()["% Overall Passing"]


# In[ ]:


# Assemble into DataFrame. 
size_summary_df = pd.DataFrame({
          "Average Math Score" : size_math_scores,
          "Average Reading Score": size_reading_scores,
          "% Passing Math": size_passing_math,
          "% Passing Reading": size_passing_reading,
          "% Overall Passing": size_overall_passing})

size_summary_df


# In[ ]:


# Format the DataFrame  
size_summary_df["Average Math Score"] = size_summary_df["Average Math Score"].map("{:.1f}".format)

size_summary_df["Average Reading Score"] = size_summary_df["Average Reading Score"].map("{:.1f}".format)

size_summary_df["% Passing Math"] = size_summary_df["% Passing Math"].map("{:.0f}".format)

size_summary_df["% Passing Reading"] = size_summary_df["% Passing Reading"].map("{:.0f}".format)

size_summary_df["% Overall Passing"] = size_summary_df["% Overall Passing"].map("{:.0f}".format)

size_summary_df


# In[ ]:


# Calculate averages for the desired columns. 
type_math_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Math Score"]

type_reading_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Reading Score"]

type_passing_math = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Math"]

type_passing_reading = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Reading"]

type_overall_passing = per_school_summary_df.groupby(["School Type"]).mean()["% Overall Passing"]


# In[ ]:


# Assemble into DataFrame. 
type_summary_df = pd.DataFrame({
          "Average Math Score" : type_math_scores,
          "Average Reading Score": type_reading_scores,
          "% Passing Math": type_passing_math,
          "% Passing Reading": type_passing_reading,
          "% Overall Passing": type_overall_passing})

type_summary_df


# In[ ]:


# # Format the DataFrame 
type_summary_df["Average Math Score"] = type_summary_df["Average Math Score"].map("{:.1f}".format)

type_summary_df["Average Reading Score"] = type_summary_df["Average Reading Score"].map("{:.1f}".format)

type_summary_df["% Passing Math"] = type_summary_df["% Passing Math"].map("{:.0f}".format)

type_summary_df["% Passing Reading"] = type_summary_df["% Passing Reading"].map("{:.0f}".format)

type_summary_df["% Overall Passing"] = type_summary_df["% Overall Passing"].map("{:.0f}".format)

type_summary_df 


# In[ ]:





# In[ ]:




