library(caret)
library(car)
library(randomForest)


data = read.csv('~/data_after_redun.csv')
print(names(data))

form = as.formula(paste("tr_log_status!='ok'~", paste(names(data), collapse="+")))
model = randomForest(formula=form, data=data, ntree=100, type='classification', importance=TRUE)

print(vif(model))


# we have to repeat this process until no variable with score > 5 exists

drop = c('gh_diff_files_modified')
data = data[~, !(names(data) %in% drop)]

form = as.formula(paste("tr_log_status!='ok'~", paste(names(data), collapse="+")))
model = randomForest(formula=form, data=data, ntree=100, type='classification', importance=TRUE)

write.csv(data, file = "~/data_after_redun.csv")