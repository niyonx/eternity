#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

git checkout gh-pages

# navigate into the build output directory
cd dist

# if you are deploying to a custom domain
# echo 'www.example.com' > CNAME

git init
git add -A
git commit -m 'deploy'

git remote add origin https://github.com/niyonx/eternity.git

# if you are deploying to https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git master

# if you are deploying to https://<USERNAME>.github.io/<REPO>
git push -f origin master:gh-pages

git checkout master

cd -