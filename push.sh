git config --global user.name "TravisCI"

git add -u
git commit -m "Update pdf and preview image(travis build $TRAVIS_BUILD_NUMBER) [skip ci]"
git remote set-url origin "https://${GH_TOKEN}@github.com/AleksaC/resume.git" &> /dev/null
git push origin HEAD:master
