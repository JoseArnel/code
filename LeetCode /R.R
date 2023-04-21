install.packages("tidyverse")
install.packages("skimr")

library(tidyverse)
library(skimr)

stocks_data <- read(".csv")

#
#viewing data
head(stocks_data)
str(stocks_data)
colnames(stocks_data)

# Useful Functions
# Packages 
installed.packages()
install.packages("tidyverse")
ggplot2, tibble, tidyr, readr, purr, dplyr, stinger, forcats
library(tidyverse)
library(lubridate)
'''
# Viewing Data
'''
head(diamonds)
str(diamonds)
colnames(diamonds)
'''
# Cleaning data
''' 
rename_with()
clean_names()
rename()
glimpse()
select()
skim_without_charts
rename(diamonds, carat_new = carat)
rename(diamonds, carat_new = carat, cut_new = cut)
summarize(diamonds, mean_carat = mean(carat))
'''
#Visualizing Data
'''
ggplot(data = diamonds, aes(x = carat, y = price)) + geom_point()
ggplot(data = diamonds, aes(x = carat, y = price, color = cut)) + geom_point()
ggplot(data = diamonds, aes(x = carat, y = price, color = cut)) + geom_point() + facet_wrap(~cut)

# readr
read_csv()

# Cleaning
summarize()

# Organize funtions
summarize()
mean()
max()
drop_na()
arrange()
group_by()
filter()
filter(species == "Adelie")

# Transform Data
spearate()
separate(emplyee, name, into=c('first_name', 'last_name'), sep = ' ')
unite()
unite(employee, 'name', first_name, last_name, sep='')
mutate()
  penguins %>% 
    mutate(body_mass_kg=body_mass_g/1000)

#Excel
library(readxl)
excel_sheets(readxl_example("type-me.xlsx"))
read_excel(readxl_example("type-me.xlsx"), sheet = "numeric_coercion")


# Changing your Data
#https://d3c33hcgiwev3.cloudfront.net/osHCTXtSSd2Bwk17Ukndiw_4c290cdedaab4ba0ae55358416b13ef1_Lesson3_Change.Rmd?Expires=1664409600&Signature=UNKgBWhYTf-L6Gn2aNk9sQl6AOEm7V64r3-9wGByo~wVk7hR62KPrVtdD31eUe4uZI43vDMMq3prj5gX41kZw5ybgFRm3i4LHMoDgECJc94eYIAPCPa4dJ8nebwJyT3C1EZTnmHgzpNvlTzWQiTE3Z3XA~~Y6FzRpqfIXvxx~0o_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
#https://d3c33hcgiwev3.cloudfront.net/2kdGwErrR6SHRsBK69ek2g_7b1b9b3017c24efab910e4bfa3e402f1_Lesson3_Change_Solutions.Rmd?Expires=1664409600&Signature=OCbab5FklItJUOd08MbinTYMUaWmTP7HnnTB6Deaf2zXzU6CFdc3-pKbISkW9pYpJ3vANMXe6Wz2h1sv3SyT3iAthcxlkkDTbeLJae-BKm62dOvjctKl13ek2eulP26PrH8DF~oNGww1ZiBjVqSVcht9F2iYqDDVDr3EY13BJqI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

install.packages("tidyverse")
install.packages("skimr")
install.packages("janitor")

library(tidyverse)
library(skimr)
library(janitor)

hotel_bookings <- read_csv("hotel_bookings.csv")

#mean(hotel_bookings_v2$lead_time)
#mean(hotel_bookings_city$lead_time)

hotel_summary <- 
  hotel_bookings %>%
  group_by(hotel) %>%
  summarise(average_lead_time=mean(lead_time),
            min_lead_time=min(lead_time),
            max_lead_time=max(lead_time))

arrange(hotel_summary)

# Cleaning your Data
install.packages("tidyverse")
install.packages("skimr")
install.packages("janitor")

library(tidyverse)
library(skimr)
library(janitor)

bookings_df <- read_csv("hotel_bookings.csv")

head(bookings_df)
str(bookings_df)
colnames(bookings_df)

#cleaning data
trimmed_df <- bookings_df %>% 
  select(, ,)

trimmed_df %>% 
  select(hotel, is_canceled, lead_time) %>% 
  rename( = hotel)

example_df <- bookings_df %>% 
  select(arrival_date_year, arrival_date_month) %>% 
  unite(arrival_month_year, c("arrival_date_month", "arrival_date_year"), sep = " ")

# another way
example_df <- bookings_df %>% 
  mutate(guests = )
example_df <- bookings_df %>% 
  head(example_df)


example_df <- bookings_df %>%
  summarize(number_canceled = sum(is_canceled),
            average_lead_time = mean(lead_time))

head(example_df)

# Create  Dataframe 
install.packages("tidyverse")
library(tidyverse)

names <- c("Peter", "Jennifer", "Julie", "Alex")
age <- c(15, 19, 21, 25)
people <- data.frame(names, age)

head(people)
str(people)
mutate(people, age_in_20 = age + 20)
fruit <- c("Lemon", "Blueberry", "Grapefruit", "Mango", "Strawberry")
rank <- c(4, 2, 5, 3, 1)
fruit_ranks <- data.frame(fruit, rank)


# quartet 
install.packages("Tmisc")
library("Tmisc")
data(quartet)
View(quartet)

quartet %>% 
  group_by(set) %>% 
  summarize(mean(x), sd(x), mean(y), sd(y), cor(x,y))

ggplot(quartet, aes(x,y)) + geom_plot() + geom_smooth(method=1m,se=FALSE) + facet_wrap(-set)

install.packages('datasauRus')
library('datasauRus')

# Annotations
recordDateinstall.packages("tidyverse")
library("ggplot2")
library("palmerpenguins")

ggplot(data=penguins) + geom_point(mapping=aes(x=flipper_length_mm,y=body_mass_g,color=species)) + 
labs(title="Palmer Penguiins: Body MAss v. Flipper", subtitle = "Sample of Three Penguins", caption="Data Colected by...") +
annotate("text", x=220, y=3500, label="The Gentoos are the Largest",fontface="bold", size=4.5, angle=25)
                            
ggsave("Three Peguin Species.png")

#PNG
png(file = "exampleplot.png", bg = "transparent")
plot(1:10)
rect(1, 5, 3, 7, col = "white")
dev.off()

# PDF
pdf(file = "/Users/username/Desktop/example.pdf",    
    width = 4,     
    height = 4) 
plot(x = 1:10,     
     y = 1:10)
abline(v = 0)
text(x = 0, y = 1, labels = "Random text")
dev.off()

#https://d3c33hcgiwev3.cl

# ToothGrowth_exploration 
install.packages("Tmisc")
library("Tmisc")
data(quartet)
View(quartet)

quartet %>% 
  group_by(set) %>% 
  summarize(mean(x), sd(x), mean(y), sd(y), cor(x,y))

ggplot(quartet, aes(x,y)) + geom_plot() + geom_smooth(method=1m,se=FALSE) + facet_wrap(-set)

install.packages('datasauRus')
library('datasauRus')

# Useful functions 
install.packages("Tmisc")
library("Tmisc")
data(quartet)
View(quartet)

quartet %>% 
  group_by(set) %>% 
  summarize(mean(x), sd(x), mean(y), sd(y), cor(x,y))

ggplot(quartet, aes(x,y)) + geom_plot() + geom_smooth(method=1m,se=FALSE) + facet_wrap(-set)

install.packages('datasauRus')
library('datasauRus')

# ToothGrowth
data("ToothGrowth") 
View(ToothGrowth)

filter_tg <- filter(ToothGrowth, dose==0.5)
View(filter_tg)
arrange(filter_tg, len)

arrange(filter(ToothGrowth, dose ==0.5), len)

filtered_toothgrowth <- ToothGrowth %>% 
  filter(dose == 0.5) %>% 
  group_by(supp) %>% 
  summarize(mean_len = mean(len, na.rm = T), .group="drop ")
