from tvdb_v4_official import TVDB as Tvdb

API_KEY = "0416a0de-181b-46a9-a1aa-95e8a53d7877" # SECURE!!!!!!
tvdb = Tvdb(apikey=API_KEY)

var = tvdb.search("Kiff", type = "series")
print(var)