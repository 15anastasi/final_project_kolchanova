library(ggplot2)
library(dplyr)
library(scales)
library(tidyverse)
library(readr)
library(zeallot)
library(countrycode)
library(ISLR)
library(caret)
library(rpart)
library(rpart.plot)
library(rattle)
library(GoodmanKruskal)
library(arm)
library(randomForest)

hotel_data <- read.csv('../input/hotel-booking-demand/hotel_bookings.csv')

cols(
  .default = col_double(),
  hotel = col_character(),
  arrival_date_month = col_character(),
  meal = col_character(),
  country = col_character(),
  market_segment = col_character(),
  distribution_channel = col_character(),
  reserved_room_type = col_character(),
  assigned_room_type = col_character(),
  deposit_type = col_character(),
  agent = col_character(),
  company = col_character(),
  customer_type = col_character(),
  reservation_status = col_character(),
  reservation_status_date = col_date(format = "")
)
hotel_data[sapply(hotel_data, is.character)] <-
  lapply(hotel_data[sapply(hotel_data, is.character)], as.factor)
