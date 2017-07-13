setwd("D:/github/city_function/r")
library(gravity)
library(GeNetIt)
library(stargazer)

dt = read.csv("../output/gravity_model_data.csv",header=T)

dt$traffic = dt$traffic + 1
dt$origin_out_traffic = dt$origin_out_traffic + 1
dt$origin_in_traffic = dt$origin_in_traffic + 1
dt$destination_out_traffic = dt$destination_out_traffic + 1
dt$destination_in_traffic = dt$destination_in_traffic + 1
dt$origin_employee = dt$origin_employee + 1
dt$fd1 = dt$fd1 * 10 + 1
dt$fd2 = dt$fd1 * 100 + 1
dt$destination_employee = dt$destination_employee + 1

dt$log_origin_residential_population = log(dt$origin_residential_population)
dt$log_destination_residential_population = log(dt$destination_residential_population)
dt$log_origin_out_traffic = log(dt$origin_out_traffic)
dt$log_destination_in_traffic = log(dt$destination_in_traffic)
dt$log_origin_tweet = log(dt$origin_tweet)
dt$log_destination_tweet = log(dt$destination_tweet)
dt$log_origin_employee = log(dt$origin_employee)
dt$log_destination_employee = log(dt$destination_employee)
dt$log_functional_distance_public_record_data = log(dt$fd1)
dt$log_functional_distance_sns = log(dt$fd2)
dt$log_traffic = log(dt$traffic)
dt$log_distance = log(dt$distance)


lm_result1 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance, data=dt)
lm_result2 = lm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance, data=dt)
lm_result3 = lm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance, data=dt)
lm_result4 = lm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance, data=dt)

lm_result5 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance + log_functional_distance_public_record_data, data=dt)
lm_result6 = lm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_public_record_data, data=dt)
lm_result7 = lm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data, data=dt)
lm_result8 = lm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance + log_functional_distance_public_record_data, data=dt)

lm_result9 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance + log_functional_distance_sns, data=dt)
lm_result10 = lm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_sns, data=dt)
lm_result11 = lm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_sns, data=dt)
lm_result12 = lm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance + log_functional_distance_sns, data=dt)

lm_result13 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)
lm_result14 = lm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)
lm_result15 = lm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)
lm_result16 = lm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)

lm_result17 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)
lm_result18 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)
lm_result19 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)
lm_result20 = lm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_origin_tweet + log_destination_tweet + log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt)

stargazer(lm_result1,
          lm_result2,
          lm_result3,
          lm_result4,
          lm_result5,
          lm_result6,
          lm_result7,
          lm_result8,
          type="html",out="gravity_model_regression_lm.html")

stargazer(lm_result9,
          lm_result10,
          lm_result11,
          lm_result12,
          lm_result13,
          lm_result14,
          lm_result15,
          lm_result16,
          type="html",out="gravity_model_regression_lm2.html")

stargazer(lm_result17,
          lm_result18,
          lm_result19,
          lm_result20,
          type="html",out="gravity_model_regression_lm3.html")

glm_result1 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance, data=dt, family=quasipoisson(link="log"))
glm_result2 = glm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance, data=dt, family=quasipoisson(link="log"))
glm_result3 = glm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance, data=dt, family=quasipoisson(link="log"))
glm_result4 = glm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance, data=dt, family=quasipoisson(link="log"))

glm_result5 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance + log_functional_distance_public_record_data, data=dt, family=quasipoisson(link="log"))
glm_result6 = glm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_public_record_data, data=dt, family=quasipoisson(link="log"))
glm_result7 = glm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data, data=dt, family=quasipoisson(link="log"))
glm_result8 = glm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance + log_functional_distance_public_record_data, data=dt, family=quasipoisson(link="log"))

glm_result9 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result10 = glm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result11 = glm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result12 = glm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))

glm_result13 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result14 = glm(log_traffic ~ log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result15 = glm(log_traffic ~ log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result16 = glm(log_traffic ~ log_origin_employee + log_destination_employee + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))

glm_result17 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result18 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_origin_tweet + log_destination_tweet + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result19 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))
glm_result20 = glm(log_traffic ~ log_origin_residential_population + log_destination_residential_population + log_origin_employee + log_destination_employee + log_origin_tweet + log_destination_tweet + log_origin_out_traffic + log_destination_in_traffic + log_distance + log_functional_distance_public_record_data + log_functional_distance_sns, data=dt, family=quasipoisson(link="log"))

stargazer(glm_result1,
          glm_result2,
          glm_result3,
          glm_result4,
          glm_result5,
          glm_result6,
          glm_result7,
          glm_result8,
          type="html",out="gravity_model_regression_glm.html")

stargazer(glm_result9,
          glm_result10,
          glm_result11,
          glm_result12,
          glm_result13,
          glm_result14,
          glm_result15,
          glm_result16,
          type="html",out="gravity_model_regression_glm2.html")

stargazer(glm_result17,
          glm_result18,
          glm_result19,
          glm_result20,
          type="html",out="gravity_model_regression_glm3.html")


