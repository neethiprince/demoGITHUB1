#GIT is a popular version control system.Its a software which has git commands to talk to github
#For git hub account we need to install GIT,git hub is central repository where one can post code
#problems one face when host code in servers v/s github->in servers when one pushes the code other persons code overrides
#Tortoise GIT,Eclipse,intellij has GUI to communicate with GITHUB by button but to understand the basic commands and concepts we are sending commands through cmd
#site for basic git commands->https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
#first tell git who you are -> git config --global user.name "neethiprince
#email id validation -> git config --global user.name "neethiprince"
#start every git command with "git" keyword
#to goto the newly creayted folder type cd and folder name -> C:\Program Files\Git\cmd>cd gitstuff
# initializing git file into the local project for github to understand-> git init
#normal file->stash->commit->github
#after initializing add your files to stash(staging)->git add *
#for permissions error changed the path directory then while adding files to solve fatal: detected dubious ownership in repository error -> git config --global --add safe.directory "*"
#confirm what all files are added by git status
#command for committing-> git commit -m "1st_commit"(message in quotes)
#git remote add origin https://github.com/neethiprince/demogithub.git->b4 pushing the code need to establish remote connection
#push the code to origin->git push origin master
#While pushing the code GIT validates and authorizes the user->

