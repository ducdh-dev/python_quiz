from urllib.parse import urlparse, parse_qs
from itertools import takewhile


def url_similarity(url1, url2):
    o1 = urlparse(url1)
    o2 = urlparse(url2)
    print(o1)
    s = (o1.scheme == o2.scheme) * 5 + (o1.netloc == o2.netloc) * 10

    p1 = o1.path.split('/')[1:]
    p2 = o2.path.split('/')[1:]
    s += len(list(takewhile(lambda x: x[0] == x[1], zip(p1, p2))))
    """
    takewhile()
    
    pred, seq
    
    seq[0], seq[1], until pred fails
    
    takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    """

    q1 = parse_qs(o1.query)
    q2 = parse_qs(o2.query)
    s += sum(2 if q1[q] == q2[q] else 1 for q in q1.keys() & q2.keys())
    # q1.keys() & q2.keys() => keep if key in q1 and q2

    return s


url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"
url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"
print(url_similarity(url1, url2))
