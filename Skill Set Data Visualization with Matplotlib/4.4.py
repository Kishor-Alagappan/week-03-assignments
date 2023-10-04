import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student': ['Student1', 'Student2', 'Student3', 'Student4', 'Student5'],
    'Marks': [85, 92, 78, 65, 55]
}

df = pd.DataFrame(data)

plt.style.use('seaborn')

# Create and style the histogram
plt.hist(df['Marks'], bins=5, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Student Marks')

# Save the histogram as a PNG image
plt.savefig('histogram.png')

# Create and style the box plot
plt.figure()
plt.boxplot(df['Marks'])
plt.xlabel('Marks')
plt.title('Box Plot of Student Marks')

# Save the box plot as a PNG image
plt.savefig('boxplot.png')

# Create and style the pie chart
plt.figure()
grade_counts = df['Marks'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D' if x >= 60 else 'F')
grade_counts = grade_counts.value_counts()
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribution of Grades')

# Save the pie chart as a PNG image
plt.savefig('piechart.png')

plt.show()
