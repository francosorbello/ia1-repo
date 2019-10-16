#--PARTE 2--#
setwd("/home/rulo/Documentos/UNCU LINUX/ia/ia1-repo/busqueda local")
library(dplyr)
data<-read.csv("datos.csv")
#EJ A)2)
ej2 <- data %>% 
    filter(h == 0) %>% 
    group_by(algoritmo,tablero) %>% 
    summarise(tot=n(),med_time=mean(tiempo),desv_time=sd(tiempo))
ej2
print('#--------------------#')
#EJ A)3) 
ej3 <- data %>% 
    filter(h > 0) %>% 
    group_by(algoritmo,tablero) %>% 
    summarise(med_h=mean(h),desv_h=sd(h))
ej3
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

#EJ A)5)
pdf("hPlots.pdf")
yHC <- data %>% filter(algoritmo=="ExecHillClimb") %>% select(h)
yHC <- as.numeric(unlist(yHC))
xHC <- 1:length(yHC)

yTS <- data %>% filter(algoritmo=="ExecTempleSim") %>% select(h)
yTS <- as.numeric(unlist(yTS))
xTS <-1:length(yTS)

yGEN <- data %>% filter(algoritmo=="ExecGenetic") %>% select(h)
yGEN <- as.numeric(unlist(yGEN))
xGEN <-1:length(yGEN)

par(mfrow=c(3,1))
plot(x=xHC,y=yHC,main="Hill Climbing",type="l")
plot(x=xTS,y=yTS,main="Temple Simulado",type="l")
plot(x=xGEN,y=yGEN, main="Genético",type="l")
dev.off()