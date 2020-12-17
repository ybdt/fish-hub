import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: below usage is from linux");
        print("Usage: python3 check-index-suffix.py http://www.example.com/");
        exit();
    else:
        url = sys.argv[1];
        # url = url.strip("/");
        file = "index";
        suffix = [".php", ".jsp", ".asp", ".aspx", ".html"];
        for i in range( len(suffix) ):
            filename = file + suffix[i];
            full_url = url + filename;
            r = requests.get(full_url);
            if r.status_code == 200:
                print(full_url + " status code is 200");
            elif r.status_code == 404:
                print(full_url + " status code is 404");
            else:
                print(full_url + " status code is unknown");

main();
