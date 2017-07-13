setwd("D:/github/city_function/r")

library(reshape2)
library(geospacom)
library(Kormaps)
library(tmap)
library(ggmap)
library(GISTools)
library(rgdal)
library(ggplot2)
library(spdep)

#' Select subdata of map
#'
#' @param map an object of class Shape(SpatialPolygonsDataFrame)
#' @param area a string of area looking for
#'
#' @return Subdata of class Shape of which code matched with area
submap <- function(map,area){
  code<-area2code(area)
  print(code)
  if(length(code)>0) {
    code1=paste0("^",code)
    temp=Reduce(paste_or,code1)
    mydata<-map[grep(temp,map$code),]
  }
}

#' Returns whether x is integer(0)
#'
#' @param x a numeric vector
is.integer0 <- function(x) { is.integer(x) && length(x) == 0L}

#' Paste '|' between vectors
#' @param ... one or more R objects, to be converted to character vectors.
paste_or <- function(...) {
  paste(...,sep="|")
}


#' Seek area from data areacode and returns the code
#'
#' @param area a string looking for
#'
#' @return a code if the area is found, else returns NA
area2code <- function(area){
  result<-c()
  for(i in 1:length(area)){
    pos<-grep(area[i],areacode[[2]])
    if(!is.integer0(pos)) temp<-areacode[pos,1]
    else {
      pos<-grep(area[i],areacode[[3]])
      if(!is.integer0(pos)) temp<-areacode[pos,1]
    }
    result=c(result,temp)
  }
  result
}


areacode$name = as.character(areacode$name)
Encoding(areacode$name) <- "UTF-8"
areacode$name2 = as.character(areacode$name2)
Encoding(areacode$name2) <- "UTF-8"



Encoding(names(korpopmap3)) <- "UTF-8"

korpopmap3$행정구역별_읍면동 = as.character(korpopmap3$행정구역별_읍면동)
Encoding(korpopmap3$행정구역별_읍면동) <- "UTF-8"

korpopmap3$name = as.character(korpopmap3$name)
Encoding(korpopmap3$name) <- "UTF-8"


Seoul3=submap(korpopmap3,"서울")
Seoul3$name[8] = "종로1.2.3.4가동"
Seoul3$name[9] = "종로5.6가동"
Seoul3$name_eng[8] = "Jongno 1.2.3.4-ga-dong"
Seoul3$name_eng[9] = "Jongno 5.6-ga-dong"


Seoul3$name[330] = "관악구 신사동"
Seoul3$name[359] = "강남구 신사동"
Seoul3$name_eng[330] = "Gwanak-gu Sinsa-dong"
Seoul3$name_eng[359] = "Gannam-gu Sinsa-dong"

mdt = read.csv("../data/dong_data/dong_mass.csv",header=T)

Seoul3$residential_population = mdt$residential_population
Seoul3$out_traffic = mdt$out_traffic
Seoul3$in_traffic = mdt$in_traffic
Seoul3$tweet = mdt$tweet
Seoul3$employee = mdt$employee

nb = poly2nb(Seoul3)
lw = nb2listw(nb)

spatial_result = lagsarlm(out_traffic ~ employee + residential_population + tweet, data = Seoul3, listw=lw)
lm_result = lm(out_traffic ~ employee + residential_population + tweet, data = Seoul3)

sink("spatial_regression_result.txt")
summary(spatial_result)
summary(lm_result)
sink()
