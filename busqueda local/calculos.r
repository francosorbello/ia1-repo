#--PARTE 2--#
setwd("/home/rulo/Documentos/UNCU LINUX/ia/ia1-repo/busqueda local")
library(dplyr)
data<-read.csv("datos.csv")
options(pillar.sigfig = 8)
#EJ A)2)
ej2 <- data %>% 
    filter(h == 0) %>% 
    group_by(algoritmo,tablero) %>% 
    summarise(tot=n(),med_time=mean(tiempo),desv_time=sd(tiempo))

ej2
print('#--------------------#')

#EJ A)3) 

#ej3 <- data %>% 
#    group_by(algoritmo,tablero) %>% 
#    summarise(med_pasos=mean(pasos),desv_pasos=sd(pasos))
#ej3

ej3 <- data %>% 
    filter(h==0) %>%
    group_by(algoritmo,tablero) %>% 
    summarise(med_pasos=mean(pasos),desv_pasos=sd(pasos))
ej3

#error raro
#a <- data %>% filter(h>0 & algoritmo=="ExectTempleSim" & tablero==10) %>% group_by(algoritmo)

#EJ A)4)
#dev.set(which = dev.next())

pdf("boxplots.pdf")
#genero datos
timeTS <- data %>% filter(algoritmo=="ExecTempleSim") %>% select(tiempo)
timeGEN <- data %>% filter(algoritmo=="ExecGenetic") %>% select(tiempo)
timeHC <- data %>% filter(algoritmo=="ExecHillClimb") %>% select(tiempo)
#genero los graficos
par(mfrow=c(1,3))
boxplot(timeHC,main="Hill Climbing")
boxplot(timeTS,main="Temple Simulado")
boxplot(timeGEN, main="Genético")
#guardo en un pdf
dev.off()

#EJ B)
data2 <- read.csv("ejb.csv", header = FALSE)

pdf("hPlots.pdf")
yHC <- data2[1,]
yHC <- as.numeric(unlist(yHC))
yHC <- yHC[!is.na(yHC)]
xHC <- 1:length(yHC)

yTS <- data2[2,]
yTS <- as.numeric(unlist(yTS))
yTS <- yTS[!is.na(yTS)]
xTS <-1:length(yTS)

yGEN <- data2[3,]
yGEN <- as.numeric(unlist(yGEN))
yGEN <- yGEN[!is.na(yGEN)]

xGEN <-1:length(yGEN)

par(mfrow=c(3,1))
plot(x=xHC,y=yHC,main="Hill Climbing",type="l", xlab="iteración",ylab="h")
plot(x=xTS,y=yTS,main="Temple Simulado",type="l", xlab="iteración",ylab="h")
plot(x=xGEN,y=yGEN, main="Genético",type="l", xlab="iteración",ylab="h")
dev.off()
