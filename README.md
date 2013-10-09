# Austin City Limits playlist downloader
A simple sequential python command line script 

## Requirements
`
sudo pip install -r requirements.txt
OR
sudo pip install -r requirements.txt --upgrade
`
requests might need to be upgraded so add --upgrade if you have an old version

## Usage
`python ACL_soundcloud_fetcher.py`

Output:
`
Already Downloaded ./music/Tim and the Space Cadets with Mother Falcon - Tim and the Space Cadets- Superhero.mp3 - 2924459K
Attempting to find Noah and the Whale - Heart of Nowhere feat. Anna Calvi.mp3
.
Saving ./music/Noah and the Whale - Heart of Nowhere feat. Anna Calvi.mp3 from http://ec-media.soundcloud.com/GqA28b2TZRVw.128.mp3?ff61182e3c2e
efa438cd02102d0e385713f0c1faf3b033959566bfb0d0dea1623ca59cfb2846d14599bf14e53f7cd8ab91fc76cbe8e4bfc7c076bf68e83f3f7653eefb058&AWSAccessKeyId=AK
AJ4IAZE5EOI7PA7VQ&Expires=1381281227&Signature=DJTjsJUEwErKRdNm6512%2BMs3XJU%3D
Download Complete, File Size: 3924217K
..
Attempting to find Luella and the Sun - 01 Fly So Free.mp3
...etc...
`

## Wha? Why?
I wanted as much of the music as possible from the ACL festival artists and they conveniently provided a bunch of soundcloud links in the source of their page prime for the picking.  I wrote this in one night a couple days before my road trip down to Austin so I could have mp3s to help decide which of the bands I didn't know to go see.

