git push
ssh -i ~/.ssh/id_rsa root@45.76.244.125 'cd ~/GitHub/QingxinManager; git pull; sh deploy_frontend.sh &; sh deploy_backend.sh &'
