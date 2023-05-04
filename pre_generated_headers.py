# * header vlaues to avoid being blocked
header_values = [
    # FireFox 58 Windows 7
    {
        'Accept' : 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.5',
        # 'Connection' : 'keep-alive'
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
    },

    # Safari on OSX
    {
        # 'Connection' : 'keep-alive'
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/601.5.17 (KHTML, like Gecko) Version/9.1 Safari/601.5.17',
        'Upgrade-Insecure-Requests' : '1',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.9'
    },

    # FireFox 58 Linux
    {
        'Accept' : 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.5',
        # 'Connection' : 'keep-alive'
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Wayland; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'
    },

    # Chrome 63 on Linux
    {
        # 'Connection' : 'keep-alive'
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Upgrade-Insecure-Requests' : '1',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.9'
    },

    # FireFox 58 Windows 10
    {
        'Accept' : 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.5',
        # 'Connection' : 'keep-alive'
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
    },

    # Chrome 63 Windows 7
    {
        # 'Connection' : 'keep-alive'
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Upgrade-Insecure-Requests' : '1',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.9'
    },

    # Chrome 63 Windows 10
    {
        # 'Connection' : 'keep-alive'
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Upgrade-Insecure-Requests' : '1',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'en-US,en;q=0.9'

    },

    # Edge on windows 10
    {
        'Accept' : 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'en-US',
        # 'Connection' : 'keep-alive'
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    },
    ];