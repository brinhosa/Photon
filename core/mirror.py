import os
import base64


def mirror(url, response):
    print("Mirroring...")
    if response != 'dummy':
        clean_url = url.replace('http://', '').replace('https://', '').rstrip('/')
        parts = clean_url.split('?')[0].split('/')
        root = parts[0]
        webpage = parts[-1]
        parts.remove(root)
        try:
            parts.remove(webpage)
        except ValueError:
            pass
        prefix = root + '_mirror'
        try:
            os.mkdir(prefix)
        except OSError:
            pass
        suffix = ''
        if parts:
            for directory in parts:
                suffix += directory + '/'
                try:
                    os.mkdir(prefix + '/' + suffix)
                except OSError:
                    pass
        path = prefix + '/' + suffix
        trail = ''
        if '.' not in webpage:
            trail += '.html'
        if webpage == root:
            name = 'index.html'
        else:
            name = webpage
        if len(url.split('?')) > 1:
            trail += '?' + url.split('?')[1]
        print("Response from: "+url)
        print(path)
        print(name)
        print(trail)
        print(response.encode('utf-8')) 
        url64=base64.b64encode(url)
        print(url64)
        os.path.basename
        with open(path + os.path.basename(url), 'w+') as out_file:
            out_file.write(response.encode('utf-8'))
            print(os.path.basename(url))
        
        with open(path + name + trail, 'w+') as out_file:
            out_file.write(response.encode('utf-8'))
            print("--------------------------")
            print(url)
            print(path + name + trail)
            print(response)
            print("--------------------------")

            
