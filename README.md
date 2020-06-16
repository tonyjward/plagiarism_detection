# plagiarism_detection

first run this
`sudo docker run -d --rm --name standalone-firefox -p 4444:4444 -p 5900:5900 --shm-size 2g selenium/standalone-firefox-debug:3.141.59`
to start a selenium server

run using
`./scrape_data.sh '[drawing pin, 'nasty surprise]' data
./check_plagiarism.sh '[drawing pin, nasty surprise]' data`
