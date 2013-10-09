# Austin City Limits playlist downloader
A simple sequential python command line script to fetch music found on ACL Festival's site playlist.

## Requirements
Xvfb + required pip modules.  Python requests might need to be upgraded so add --upgrade if you have an older version.
```
sudo pip install -r requirements.txt
OR
sudo pip install -r requirements.txt --upgrade
AND
sudo apt-get install xvfb

```

## Usage
`python ACL_soundcloud_fetcher.py`

Output:
```
Already Downloaded ./music/Tim and the Space Cadets with Mother Falcon - Tim and the Space Cadets- Superhero.mp3 - 2924459K
python ACL_soundcloud_fetcher.py 
Attempting to find Noah and the Whale - Heart of Nowhere feat. Anna Calvi.mp3 (https://soundcloud.com/noah-and-the-whale/heart-of-nowhere-feat-anna)
.
Saving ./music/Noah and the Whale - Heart of Nowhere feat. Anna Calvi.mp3 from http://ec-media.soundcloud.com/GqA28b2TZRVw.128.mp3?ff61182e3c2ecefa438cd02102d0e385713f0c1faf3b033959566bfb0c06e81d1748e0c911661bd66277f02f931b537f5dc9d6f00ccab99529d6f26f6887ca1f661dbbd397&AWSAccessKeyId=AKIAJ4IAZE5EOI7PA7VQ&Expires=1381333963&Signature=wcuLZt3FKWElcW7ik8YMp6fbPL8%3D
Download Complete, File Size: 3924217K
..
Attempting to find Luella and the Sun - 01 Fly So Free.mp3 (https://soundcloud.com/bookimbrash/01-fly-so-free-1)
.
Saving ./music/Luella and the Sun - 01 Fly So Free.mp3 from http://ec-media.soundcloud.com/iwGZWlSp2i6v.128.mp3?ff61182e3c2ecefa438cd02102d0e385713f0c1faf3b033959566bfb0c06ef14883b2989e2211599e4dabc980766b5f1ff5a6917d610a11900fe37f65863e1a52bcc9f129a&AWSAccessKeyId=AKIAJ4IAZE5EOI7PA7VQ&Expires=1381334006&Signature=oh2bQSB%2BgYfgdblWh%2BprvyulV5U%3D
Download Complete, File Size: 3505840K
..
...etc...
```

## Wha? Why?
I wanted as much of the music as possible from the ACL festival artists and they conveniently provided a bunch of soundcloud links in the source of their page prime for the picking.  I wrote this in one night a couple days before my road trip down to Austin so I could have mp3s to help decide which of the bands I didn't know to go see.

