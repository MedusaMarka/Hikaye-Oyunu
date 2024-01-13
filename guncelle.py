import git 

# Instantiate repo object
repo = git.Repo("https://github.com/MedusaMarka/Hikaye-Oyunu.git")
# pull down 
repo.remotes.origin.pull()
