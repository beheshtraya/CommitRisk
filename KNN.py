"""
Dataset: https://travistorrent.testroots.org/page_access/

"""
import time
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from pandas import DataFrame
import seaborn as sn

wantedcol=['gh_project_name', 'gh_is_pr', 'gh_pull_req_num', 'gh_lang', 'gh_num_commits_in_push', 'git_prev_commit_resolution_status' ,
'gh_team_size', 'git_num_all_built_commits', 'gh_num_issue_comments', 'gh_num_commit_comments', 'gh_num_pr_comments', 'git_diff_src_churn',                
'git_diff_test_churn', 'gh_diff_files_added', 'gh_diff_files_deleted',            
'gh_diff_files_modified','gh_diff_tests_added', 'gh_diff_tests_deleted','gh_diff_src_files','gh_diff_doc_files',               
'gh_diff_other_files','gh_num_commits_on_files_touched','gh_sloc',           
'gh_asserts_cases_per_kloc','gh_by_core_team_member','gh_description_complexity','tr_log_status']#'tr_status']

# read main data set
dataset = pd.read_csv('travistorrent_8_2_2017.csv', usecols=wantedcol)
dataset=dataset.loc[dataset['gh_project_name']=="rails/rails"]
del dataset['gh_project_name']
 
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,25].values

for i in range(0,len(y)):
    if y[i]!="ok":
        y[i]="fail"

# Encoding categorical string
lableencoder_y = LabelEncoder()
y = lableencoder_y.fit_transform(y)
lableencoder_X = LabelEncoder()
X[:,0] = lableencoder_X.fit_transform(X[:,0])
lableencoder_X = LabelEncoder()
X[:,2] = lableencoder_X.fit_transform(X[:,2]) 
lableencoder_X = LabelEncoder()
X[:,4] = lableencoder_X.fit_transform(X[:,4]) 
lableencoder_X = LabelEncoder()
X[:,23] = lableencoder_X.fit_transform(X[:,23]) 

# Handle Missing value
imputer = Imputer(missing_values='NaN',strategy="most_frequent",axis=0)
imputer = imputer.fit(X)
X = imputer.transform(X)
onehotencoder = OneHotEncoder(categorical_features=[0,2,4,23])
X=onehotencoder.fit_transform(X).toarray()

# Splitting the dataset inti the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) 

# FEATURE SCALLING
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

t1=time.time()
classifier = KNeighborsClassifier(n_neighbors=35,weights="distance",p=2)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("accuuracy:",accuracy)
t2=time.time()
print ("Time: ",t2-t1)

# Recall
recall_score(y_test, y_pred, average=None)

# F1-Score
f1_score(y_test, y_pred, average=None)

# Precision
precision_score(y_test, y_pred, average=None)

# Cross validation
accuracies = cross_val_score(estimator=classifier,X=X_train,y=y_train,cv=10)
print("accuracy : ",accuracies)

#Making confusion matrix
cm = confusion_matrix(y_test,y_pred)
df_cm = DataFrame(cm)
ax = sn.heatmap(df_cm, cmap='gist_heat_r', annot=True)
