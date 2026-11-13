def toHttps(url):
    if url[0:8] == "https://":
        return url
    return url.replace("http://","https://")

print(toHttps("http://example.com"))
print(toHttps("https://google.com"))
print(toHttps("http://recursion.io/me"))
print(toHttps("http://github.com/user/repo"))
