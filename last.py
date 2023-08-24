import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "a57d3c3e5003f22fdbfa26fc099d6e69"  # this is a sample key
API_SECRET = "e34ba5772946e28ba392b4aeee349be3"

# In order to perform a write operation you need to authenticate yourself
username = "etgrives"
password_hash = pylast.md5("qwerty@1234")

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=username,
    password_hash=password_hash,
)
track = network.get_artist("Adele")
print(track.get_bio_summary())