\#How to?



This is where I document whatever I am learning



\## How to setup this repo



1\. Created the repo on GitHub called `commodity\\\_lab` (I also already created there the README.md and roadmap.md - it is not mandatory at this stage)

2\. Cloned it locally with:

    git clone https://github.com/MYUSERNAME/commodity\_lab.git

3\. Entered the directory:

    cd commodity\_lab

4\. Created this how\_to.md file to document steps.

5\. Specify the file we want to commit next with:

 	git add how\_to.md

6\. Commit changes with a comment:

 	git commit -m "add how\_to.md to document workflow"

7\. Push to GitHub:

 	git push



Then we proceed to create all the folders!

Then we 
8. create docs folder:
	mkdir docs
9. move the file into docs:
	git mv how_to.md docs/how_to.md 

10. rename the file to 'basics_git_and_cp.md'
	git mv docs/how_to.md docs/basics_git_and_cp.md
	git commit -m "Rename how_to.md to basics_git_and_cp.md"
	git push origin main


	






