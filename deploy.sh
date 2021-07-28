set -xe

if [ $TRAVIS_BRANCH == 'cd-pipeline' ] ; then
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa

  rsync -a --exclude={'/node_modules','/src','/public'} client/ ubuntu@143.110.189.18:/home/ubuntu/demo/client
  rsync -a server/ ubuntu@143.110.189.18:/home/ubuntu/demo/server
else
  echo "Not deploying, since the branch isn't master."
fi
