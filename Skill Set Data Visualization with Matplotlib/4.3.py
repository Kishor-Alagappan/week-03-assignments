import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student': ['Student1', 'Student2', 'Student3', 'Student4', 'Student5'],
    'Marks': [85, 92, 78, 65, 55]
}


df = pd.DataFrame(data)

# Histogram
plt.hist(df['Marks'], bins=5, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Student Marks')
plt.show()

# Boxplot
plt.boxplot(df['Marks'])
plt.xlabel('Marks')
plt.title('Box Plot of Student Marks')
plt.show()
 
# bar chart 
# Define grading criteria
bins = [0, 60, 70, 80, 90, 100]
labels = ['F', 'D', 'C', 'B', 'A']

# Add a new column for grades
df['Grade'] = pd.cut(df['Marks'], bins=bins, labels=labels)

# Calculate the percentage of students in each grade category
grade_counts = df['Grade'].value_counts(normalize=True) * 100

# Plot the pie chart
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Grades')
plt.show()
