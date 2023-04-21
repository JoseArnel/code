# Visuals
#https://d3c33hcgiwev3.cloudfront.net/algvdUHgT7iYL3VB4B-49g_f8ffabe1fac842d6872cca560da7c9f1_Lesson2_GGPlot.Rmd?Expires=1664409600&Signature=gzUisFih7S-mqsmgmzuGQLGHwjuTVP5BDhRkrE9bS25TGfkFnuqccBovQj0HpywaOwETiuPqFar7ZS1-4BHOuUlflzyOkJcv8c-jhb-v9QjkocyYUzpcY2O4J9ofZ58Bxst3rYeMYZkIOIvYTLt9L-xaZoePYnRb6xSxOd5z6bs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
# https://d3c33hcgiwev3.cloudfront.net/jTmZc7yMSMW5mXO8jJjF6w_f6509abd385345a494a310d8aaea23f1_Lesson2_GGPlot_Solutions.Rmd?Expires=1664409600&Signature=BFW0qjiR7Fk0WQW6wdXowk4FM0Rw8rg5zN42QSXOGsSJHm2nqJMS~sorWAFwx3SKiOqv6LJaquuBqs4W7e~JEJTB6eeeDBnAzsnKg8wFLe93HVguc3Y~JyAxsvr3voBYgjNz7Qc41IWb3nZme~EinNzn7kX7WVI3wFsMPO8aClU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

install.packages("tidyverse")
library("ggplot2")
library("palmerpenguins")
ggplot(data=penguins) + geom_smooth(mapping=aes(x=flipper_length_mm, y=body_mass_g, linetype = spicies))+ geom_point(mapping = aes (x=flipper_length_mm, y=body_mass_g))
#ggplot(data=penguins) + geom_point(mapping = aes (x=flipper_length_m=,)
#geom_jitter(), geom_alpha

ggplot(data=diamonds) + geom_bar(mapping = aes(x=cut, fill=clarity))

# facet function facet_wrap/facet_grid
ggplot(data=penguins) + geom_point(mapping=aes(x=flipper_length_mm, y=body_mass_g, color=species)) + facet_wrap(~species)
ggplot(data=diamonds) + geom_bar(mapping=aes(x=color,fill=cut)) + facet_wrap(~cut)
ggplot(data=penguins) + geom_point(mapping=aes(x=flipper_length_mm, y=body_mass_g, color=species)) + facet_grid(sex~species)
#https://d3c33hcgiwev3.cloudfront.net/Fd1svexhQ82dbL3sYRPNwA_9fece722572248bda9738cdf7f8633f1_Lesson3_Aesthetics.Rmd?Expires=1664409600&Signature=c9zzQOpBb4iQgxkCyZtNUCCO0oc4SRlo147GsqLrI84cPtXYjBvb68ZZQW7r02gVyhXBYpfgmQiJThtBZ3snv2-53x9ouLWeb3HWu-zQz-MnHPUmjlDlgV0OgJOrQxAm~qPQxgJCfxGJ~D0cW4wUH1PGr4a~xyfVhPRKYi8BlUM_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

install.packages("dplyr")
library("dplyr")
data %>%
  filter(variable1 == "DS") %>%  
  ggplot(aes(x = weight, y = variable2, colour = variable1)) +  
  geom_point(alpha = 0.3,  position = position_jitter()) + stat_smooth(method = "lm")

# Filters
# https://d3c33hcgiwev3.cloudfront.net/w44BXN8tRZ2OAVzfLSWdHg_a8a82a7f1a8c4869818fdd818b333ef1_Lesson3_Filters_Solutions.Rmd?Expires=1664409600&Signature=hOelF-0zBTvCFHwNxpaZWl-zpJxi2U~9-f5qCXP~UDzIiZ8a0u08FS-9H3SBY-BZFWwd~nkVqdbNDzbga5MUQ2eUK8pRe8ILRewK7~RqsWMrSuTq6M0XWhJtyHSis8QRfuzkqeaxAvATtw~5bvVvYQ0wfGnUbChwu~zFNGk6qcs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A
hotel_bookings <- read.csv("hotel_bookings.csv")
ggplot(data = hotel_bookings) +
  geom_point(mapping = aes(x = lead_time, y = children))
ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = hotel, fill = market_segment))
ggplot(data = hotel_bookings) +
  geom_bar(mapping = aes(x = hotel)) +
  facet_wrap(~market_segment)
#filter
onlineta_city_hotels_v2 <- hotel_bookings %>%
  filter(hotel=="City Hotel") %>%
  filter(market_segment=="Online TA")
View(onlineta_city_hotels_v2)
ggplot(data = onlineta_city_hotels) +
  geom_point(mapping = aes(x = lead_time, y = children))
