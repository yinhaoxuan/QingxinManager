sudo fuser -k 5000/tcp
cd frontend
npm install
npm run build
npm install -g serve
serve -s build &
