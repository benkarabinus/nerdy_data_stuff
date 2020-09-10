#Name: Ben Karabinus
#Date: 5/7/2020
#Description: This script was created in fulfillment of the final 
#project for Dr. Kiss' CIS 4370-001 class Spring 2020

########install the required packages########

if(!require(DataExplorer)){install.packages("DataExplorer")}
library(DataExplorer)
if(!require(psych)){install.packages("psych")}
library(psych)
if(!require(BBmisc)){install.packages("BBmisc")}
library(BBmisc)
if(!require(Metrics)){install.packages("Metrics")}
library(Metrics)
if(!require(caret)){install.packages("caret")}
library(caret)
if(!require(leaps)){install.packages("caret")}
library(leaps)
if(!require(randomForest)){install.packages("randomForest")}
library(randomForest)

#######Load the Data into R (testing data)########
housing_data <- read.csv("house_prices_training.csv",
                         header = TRUE)

#######Explore the testing dataset#########

# Explore dataset structure
summary(housing_data)
str(housing_data)
head(housing_data)

#explore the variables in the dataset
describe(housing_data)

#Plot basic description
plot_intro(housing_data)

#double check missing values
profile_missing(housing_data)

     #####dataset appears to be complete####


# View overall correlation heatmap to explore relationships
plot_correlation(housing_data)



#use linear regression exhaustive search method to
#reduce dimension (library = leaps)
var_search <- regsubsets(TOTAL.VALUE ~ ., data = housing_data,
                         nbest = 1, nvmax = 14, 
                            method = "exhaustive")

#create variable to store results of exhaustoive search
sum_var_search <- summary(var_search)

#print variables used in each subset
sum_var_search$which

#print AdjRsquared values for subsets 
sum_var_search$adjr2

#print Mallow's CP for subsets
sum_var_search$cp

#create subset based on results of dimension reduction
sub_housing_data <- housing_data[,c("TOTAL.VALUE", "LOT.SQFT",
      "YR.BUILT","GROSS.AREA","LIVING.AREA","FLOORS",
        "FULL.BATH","HALF.BATH","KITCHEN","FIREPLACE")]

#check head
head(sub_housing_data)


#create data partition within the reduced training set
indxTrain <- createDataPartition(y = sub_housing_data$TOTAL.VALUE,
                                 p = 0.7,list = FALSE)

training <- sub_housing_data[indxTrain,]
testing <- sub_housing_data[-indxTrain,]


#create exploratory linear regression model
exploratory_model <- lm(TOTAL.VALUE ~ ., data = training)

options(scipen=999)
summary(exploratory_model)


# Predict the testing set`s prices with  exploratory_model
predictions_training <- predict(exploratory_model, newdata = training)
predictions_training

# Predict the testing set`s prices with exploratory_model
predictions_testing <- predict(exploratory_model, newdata = testing)
predictions_testing

# compute RMSE and Pearson coefficient 

# For the training set:
rmse(training$TOTAL.VALUE, predictions_training)
cor(training$TOTAL.VALUE, predictions_training)

# For the testing set:
rmse(testing$TOTAL.VALUE, predictions_testing)
cor(testing$TOTAL.VALUE, predictions_testing)


####partition data again

# Set seed for reproducibility
set.seed(111)

### Spliting data as training and test set using sub_housing_data ##
indxTrain <- createDataPartition(y = sub_housing_data$TOTAL.VALUE,p = 0.75,list = FALSE)

training <- sub_housing_data[indxTrain,]
testing <- sub_housing_data[-indxTrain,]


#create random forest model for regression
myforest <- randomForest(formula = TOTAL.VALUE ~ ., data = training, 
                         importance = T, ntree = 200, mtry = 5)
#print model
myforest

var_importance <- importance(myforest)
var_importance[1:9,]
varImpPlot(myforest, type = 1)

# number of trees with lowest MSE
which.min(myforest$mse)

#plot prediction accuracy as a function of number of trees
plot(myforest)

#make predictions on training data using model myforest
forest_predictions_training <- predict(myforest, newdata = training)

#Print RMSE and Pearson coefficient(training)
rmse(training$TOTAL.VALUE, forest_predictions_training)
cor(training$TOTAL.VALUE, forest_predictions_training)

#make predictions on testing data using model myforest
forest_predictions_testing <- predict(myforest, newdata = testing)

#Print RMSE and Pearson coefficient(testing)
rmse(testing$TOTAL.VALUE, forest_predictions_testing)
cor(testing$TOTAL.VALUE, forest_predictions_testing)


######Load data from the holdout set#####
housing_data_holdout <- read.csv("house_prices_testing.csv",
                         header = TRUE)

#create subset of data from the holdout set
sub_housing_data_holdout <- housing_data_holdout[,c("TOTAL.VALUE", "LOT.SQFT",
                                    "YR.BUILT","GROSS.AREA","LIVING.AREA","FLOORS",
                                    "FULL.BATH","HALF.BATH","KITCHEN","FIREPLACE")]
#verify subset was created
head(sub_housing_data_holdout)

#create predictions for holdout set
forest_predictions_testing <- predict(myforest, 
                          newdata = sub_housing_data_holdout)

#Print RMSE and Pearson coefficient(holdout)
cor(sub_housing_data_holdout$TOTAL.VALUE, forest_predictions_testing)
sd(sub_housing_data_holdout$TOTAL.VALUE)
rmse(sub_housing_data_holdout$TOTAL.VALUE, forest_predictions_testing)







