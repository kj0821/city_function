#setwd("C:/Users/Berdomi/PycharmProjects/LDA")
setwd("C:/Users/Berdomi/workspace/RemoteSystemsTempFiles/143.248.156.240/home/placeness/impeachment/output")
dcv = read.csv("dong_cluster_word2vec.csv",header=F)

clustervec = dcv$V2
names(clustervec) = dcv$V1

clusterVector = c()
for(ename in Seoul3$name_eng){
  
  if(is.na(clustervec[ename]))
  {
    print(ename)
    print(clustervec[ename])
  }
  clusterVector = c(clusterVector, clustervec[ename])
}

Seoul3$cluster = clusterVector

Seoul3$cname = paste(as.character(Seoul3$cluster), Seoul3$name_eng, sep="_")




pdf("seoul_cluster.pdf",height = 15, width=15)

tm_shape(Seoul3) +
  tm_fill("cluster",n=clusternum, palette=brewer.pal(10,"Set3"), auto.palette.mapping=F) +
  tm_layout(legend.show = T, title.position = c("center", "center"), title.size = 2) +
  tm_borders() + tm_text("cname",size = 0.6)
dev.off()


pdf("seoul_cluster_only.pdf",height = 15, width=15)

tm_shape(Seoul3) +
  tm_fill("cluster",n=clusternum, palette=brewer.pal(10,"Set3"), auto.palette.mapping=F) +
  tm_layout(legend.show = T, title.position = c("center", "center"), title.size = 2) +
  tm_borders() + tm_text("cluster",size = 1)
dev.off()




