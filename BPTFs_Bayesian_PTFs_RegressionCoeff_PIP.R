
#################################################################
###//Bayesian Pedotransfer Functions (BPTFs)
###//Kevin Achieng
###//Department of Civil & Architectural Engineering 
###//University of Wyoming
###//kachieng@uwyo.edu
###//04/27/2019
#################################################################
rm(list=ls())
#//Set the directory where the input soil data is
setwd("E:/Spring2019/SSURGO/Science of The Total Environment/Code/")                    #unique directory
getwd()
#################################################################
#Set start time: 
################################################################
#Install packages (BMS & biomod2) 
#install.packages("BMS") #uncomment this line to isntall BMS
#install.packages("biomod2") #uncomment this line to isntall biomod2

##//Get the packages you will need
require("BMS") 
require("biomod2")
##//Import the soil.file data
file.list <- dir(pattern = ("_Data.csv"))
##//Get the dataframe headers
file.name <- file.list[1]
length(file.list)
soil.file <- read.csv(file.name,  row.names = 1, header = T)
soil.file.name = names(soil.file)
#//Set up the Progress bar 
j=0; j.max = length(file.list); pb <- txtProgressBar(min = 0, max = j.max, style = 3) # for progress bar
print("Analyzing soil.file data.  Keep Calm.....")

for (i in 1:length(file.list)){
  
  ##//Import data as dataframe
  soil.file <- read.csv(file.list[i],  row.names = 1, header = T)
  # update progress bar  
  j=j+1; setTxtProgressBar(pb, j) 
  #Define name of output
  soil.file.name =substr(file.list[i], 1, nchar(file.name))
  print(paste("Analyzing soil.file file", soil.file.name))

  #################################################################
  ##  Implement BMA Analysis                                    ###
  ##  1st create BMA Object(s)                                  ###
  #################################################################
  
  #Bayesian Analysis with mprior = "uniform" and Emperical Bayes Local (EBL) g-Prior
  soil.file_g.EBL = bms(soil.file,burn=20000,iter=1e+6, g="EBL", mprior = "uniform", nmodel = 2000, 
                        mcmc = "bd",user.int=F )
  # REGRESSION COEFFICIENTS & PIP
  Anaytical_coef.file_g.EBL = coef(soil.file_g.EBL, order.by.pip=FALSE, include.constant=TRUE, exact =T)
  #'Save the COEFFICIENTS & PIP
  write.csv(Anaytical_coef.file_g.EBL, file=paste(soil.file.name, "_PIP_Regresssion_coefficients", ".csv ", sep = ""))
  
  #//Determine relative importance of the explanatory variables 
  ##############################################################################
  ##'  Use biomod2 package to                                                ###
  ##'  Implement variables_importance Variables importance calculation       ###
  ##'  This function will return a variable importance value for each        ###
  ##'  variable involved within your model.                                  ###
  ##############################################################################
  mod <- glm(AWC_cm.per.cm.~Sand_Percent+Silt_Percent+Clay_Percent+Moist.BD_g.per.cm3.+OM_Percent, data=soil.file)
  var_importance=variables_importance(model=mod, data=soil.file[,c('Sand_Percent','Silt_Percent', 'Clay_Percent', 'Moist.BD_g.per.cm3.', 'OM_Percent')], method="full_rand", nb_rand=10)
  
  #'Save the var_importance
  var_importance=as.data.frame(var_importance$mat)
  write.csv(var_importance, file=paste(soil.file.name, "_variables_importance", ".csv ", sep = ""))
  
  print("Relax, analysis is done.")    
}
