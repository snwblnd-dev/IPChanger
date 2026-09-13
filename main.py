import argparse
import requests
from stem.process import launch_tor

if __name__ == '__main__':


    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--tor', action='store_true', help = 'Use the Tor Browser')
    parser.add_argument('-p', '--proxy', type=str, help='Set the Proxy IP')
    parser.add_argument('--torcmd', type=str, help = 'Specify the Tor Browser Path', default=r"tor")

    tor = None
    try:

        print('Direct Connection: ')
        data = requests.get('https://api.ipify.org?format=json')
        print(data.json())

        args = parser.parse_args()



        #use the custom proxy if provided
        if args.proxy:

            proxies = {'http': 'http://' + args.proxy, 'https': 'http://' + args.proxy}
            print("connecting via proxy: " + args.proxy)
            new_ip = requests.get('https://api.ipify.org?format=json', proxies=proxies)
            print(new_ip.json())

        #use the tor network otherwise
        if args.tor:
            if args.torcmd:
                tor = launch_tor(tor_cmd=args.torcmd, take_ownership=True)
            else:
                tor = launch_tor(tor_cmd='tor', take_ownership=True)


            proxies = {'https': 'socks5h://127.0.0.1:9050', 'http': 'socks5h://127.0.0.1:9050'}

            print("connecting via tor:")
            new_ip = requests.get('https://api.ipify.org?format=json', proxies=proxies)
            print(new_ip.json())



    except Exception as e:
        print(e)
    finally:
        if tor:
            tor.terminate()




