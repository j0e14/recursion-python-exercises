def extractDomain(url):
    # 関数を完成させてください
    s = url
    at1 = s.find("//")+len("//")
    at2 = s.find("/",at1)
    return s[at1:at2]

print(extractDomain("https://github.com/recursionist"))
