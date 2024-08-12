import subprocess
import time
import argparse


def ping_ip(ip):
    """Pings the specified IP address and returns True if available, False otherwise."""
    response = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE)
    output = response.communicate()[0]
    return "Request timed out" not in output.decode('utf-8')


def main():
    parser = argparse.ArgumentParser(description="Checking the availability of IP addresses.")
    parser.add_argument('--iplist', metavar='file', default='ips.txt', help='file to process (defaults to ips.txt)')
    parser.add_argument('--interval', metavar='seconds', type=int, default=60,
                        help='interval between checks (defaults to 60 seconds)')
    args = parser.parse_args()

    print(f"File is using: {args.iplist}")

    with open(args.iplist, 'r') as f:
        ips = f.readlines()
        ips = [ip.strip() for ip in ips]

    try:
        while True:
            for ip in ips:
                if ping_ip(ip):
                    print(f"IP {ip} available")
                else:
                    print(f"IP {ip} not available")

            print(f"Next check in {args.interval} seconds...")
            time.sleep(args.interval)  # Pause for the specified interval
    except KeyboardInterrupt:
        print("\nExit after user interruption.")
        exit(0)


if __name__ == "__main__":
    main()
