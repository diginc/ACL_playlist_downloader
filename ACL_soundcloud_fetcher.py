#!/usr/bin/env python
import requests
import re
import json
import time
import os
import urllib
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display

# Fetches the list of soundcloud streamed songs off ACL's site
url = 'http://www.aclfestival.com/2013-schedule/weekend-two'
r = requests.get(url)
if (r.status_code == requests.codes.ok):
  sc_links_page = r.text
  # minidom freaked out over malformed tags, BeautifulSoup works!
  dom = BeautifulSoup(sc_links_page)
  # XPath we want: //*[@id="myacl-menu"]/div[3]/div[1]/div/div
  # can't search by xpath so...find by tag + contents
  scripts = dom.find_all("script")
  for s in scripts:
    # Next get rid of the CDATA wrapper around json var
    match = re.search('track__title', str(s))
    if match:
      songs_match = re.search(r"(var C3FMConfig = )(.*);", s.text)
      if songs_match:
        songs_json = songs_match.group(2)
        songs = json.loads(songs_json)
        #pprint(songs) # (sample.json)

# Wait for JS pause + don't be a hammer pause = total time between songs (not inc. download time)
js_pause = 15
dbah_pause = 15
save_to_folder = './music/'
# Mainly for testing purposes, leave at 0 to grab all songs
song_limit = 0
i=0

# Requires Xvfb
display = Display(visible=0, size=(400, 320))
display.start()
for song in songs['allArtistsTracks']:
  song_info = songs['allArtistsTracks'][song][0]
  file_name = song_info['track__artist'] +" - "+ song_info['track__title'] + ".mp3"
  full_file = save_to_folder+file_name
  if os.path.isfile(full_file) and os.path.getsize(full_file) > 100:
    print "Already Downloaded "+ full_file +" - "+ str(os.path.getsize(full_file)) +"K"
  else:
    # Had issues not getting mp3s when re-using browser (slower but, hey it works)
    browser = webdriver.Firefox()
    print "Attempting to find "+ file_name +" ("+ song_info['track__url'] +")"
    soundcloud_mp3_fetcher = 'http://offliberty.com/#'+song_info['track__url']
    browser.get(soundcloud_mp3_fetcher)

    print "."
    time.sleep(js_pause)

    # you won't find this unless you wait long enough for js
    try:
      dl_link = browser.find_element_by_xpath('//*[@id="form_div"]/a[1]')
      sc_aws_url = dl_link.get_attribute('href')
      if not os.path.isfile(full_file):
        print "Saving "+ full_file +" from "+ sc_aws_url
        urllib.urlretrieve(sc_aws_url, full_file)
      if os.path.isfile(full_file):
        print "Download Complete, File Size: "+ str(os.path.getsize(full_file)) +"K"
    except:
      print "Failed to find mp3 using: "+ soundcloud_mp3_fetcher
    print ".."
    time.sleep(dbah_pause)
    browser.close()

  if song_limit > 0:
    i = i + 1
    if song_limit == i: break

display.stop()
