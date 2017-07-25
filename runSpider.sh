#!/bin/bash

cd /home/ian/Projects/uwo_scraper/coursesniper/
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl sniper
