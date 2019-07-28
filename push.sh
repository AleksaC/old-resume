git config --global user.name "TravisCI"

git add .
git commit -m "Update pdf and preview image(travis build $TRAVIS_BUILD_NUMBER) [skip ci]"
git remote set-url origin https://${GH_TOKEN}@github.com/AleksaC/resume.git > /dev/null 2>&1
git push origin HEAD:master
