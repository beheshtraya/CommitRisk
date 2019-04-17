library(foreign)
library(caret)
library(car)
library(nlme)
library(rms)
library(e1071)
library(BiodiversityR)
library(moments)


data = read.csv('~/travistorrent_8_2_2017.csv')
drop = c('tr_build_id', 'gh_pr_created_at', 'git_merged_with', 'git_branch', 'gh_commits_in_push', 'git_prev_built_commit', 'tr_prev_build', 'gh_first_commit_created_at', 'git_all_built_commits', 'git_trigger_commit', 'tr_virtual_merged_into', 'tr_original_commit', 'gh_pushed_at', 'gh_build_started_at', 'tr_status', 'tr_duration', 'tr_jobs', 'tr_build_number', 'tr_job_id', 'tr_log_setup_time', 'tr_log_bool_tests_ran', 'tr_log_bool_tests_failed', 'tr_log_num_tests_ok', 'tr_log_num_tests_failed', 'tr_log_num_tests_run', 'tr_log_num_tests_skipped', 'tr_log_tests_failed', 'tr_log_testduration', 'tr_log_buildduration')
data = data[, !(names(data) %in% drop)]

ok = subset(data, data$tr_log_status=='ok')
failed = subset(data, data$tr_log_status!='ok')
summary(ok)

wilcox.test(ok$gh_sloc, failed$gh_sloc)

plot(density(ok$gh_sloc))
plot(density(failed$gh_sloc))
plot(density(ok$gh_sloc))
plot(density(ok$gh_sloc))
plot(density(failed$gh_sloc))
     
drop = c('tr_log_status')
independant = data[, !(name(data) %in% drop)]

correlations = cor(independant, method = 'spearman')

print(correlations)

highCorr <- findCorrelation(correlations, cutoff = .75)

vcobj = varclus ( ~., data = independant ,trans ="abs")
redun_obj = redun (~. ,data = independant ,nk =0)

print(redun_obj)
