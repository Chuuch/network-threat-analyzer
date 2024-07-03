from scanner import port_scan

def main():
    target = input("Enter the target IP address or hostname: ")
    port_scan(target)

if __name__ == "__main__":
    main()