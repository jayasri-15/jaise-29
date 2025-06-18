posts=[
{"user":"alice","post":"hi"},
{"user":"bob","post":"hello"},
{"user":"alice","post":"again"},
{"user":"x","post":"xyz"},
{"user":"bob","post":"xyz"},
]
# frequency=Counter(posts["post"])
# print(frequency)
frequency={
}
for i in posts:
    if i["user"] in frequency:
        frequency [i["user"]]= frequency [i["user"]] +1
    else:
        frequency [i["user"]]=1

        print(frequency)