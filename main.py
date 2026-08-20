# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
#plt.scatter(lwd["year"],lwd["EI_women_fridge_p"],color="yellow")

# add a title to the plot
#plt.title("Percent of Women Who are living in a household with a fridge")

#Label the x-axis
#plt.xlabel("Year")

# label the y-axis
#plt.ylabel("Women who are living in a household with a fridge(%)")

# set the range for the y-axis
#plt.ylim(0,14)

# show the plot
#plt.show()
print("==Statement==") 
#setting statements
print("This data compares women in Zimbabwe and Senegel.\n")
print("The data sets examines the relationship between the percentage of women with secondary or higher education and percentage of women who read a newspaper at once a week.\n") 
print("The scatter plot shows Zimbabwe consistently has higher values for both education and newspaper readership than Senegal, suggesting differences in access to education and information.\n")
input("Press Enter to countinue...... ") 

print("==Characters==")
#character statements
print("Women in Senegal and Zimbabwe with different levels of education(Higher or Secondary).\n") 
print("Women whose opportunities for education, access to current affairs vary across countries(depending on the country they live in) ,influencing their awareness,literacy, and access to information.\n") 
input("Press Enter to continue......")

print("==Context==")
#context statements
print("Difference in education systems and media access between countries like Zimbabwe and Senegal can contribute to difference in women’s educational attainment and news paper reading habits.\n")
print("Investing in girl’s education can increase literacy and improve access to current affairs and civic participation.\n")
input("Press Enter to continue......")
      
oneCountryBooleanlist = lwd["country_name"]=="Zimbabwe"
oneCountryData = lwd.loc[oneCountryBooleanlist]
# create a scatter plot for country 1
plt.scatter(oneCountryData["EI_news_week_p"],oneCountryData["ED_attainment_secondary_higher_p"],color="red",label="Zimbabwe")

#for country 2
secondCountryBooleanlist = lwd["country_name"]== "Senegal"
secondCountryData = lwd.loc[secondCountryBooleanlist]

plt.scatter(secondCountryData["EI_news_week_p"],secondCountryData["ED_attainment_secondary_higher_p"],color="green",label="Senegal")

# add a title to the plot
plt.title("Women reading a newspaper vs Women with secondary education or higher education")

#Label the x-axis
plt.xlabel("Women reading a newspaper a least once a week(%)")

# label the y-axis
plt.ylabel("Women with secondary education or higher education(%)")

# set the range for the y-axis
plt.ylim(0,80)
plt.legend()
# show the plot
plt.show()

input("Press Enter to continue.....")
print("Why do women in Zimbabwe have higher newspaper readership than women in Senegal? Is this associated with higher levels of secondary or higher education, differences in access to newspapers, or other country-specific factors?")