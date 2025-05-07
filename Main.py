
import dns.resolver

# List of DNS servers to test
dns_servers = ['192.168.100.120', '192.168.100.121', '192.168.100.122']

# Domain to test
domain = 'example.com'

def test_dns_servers(dns_servers, domain):
    for server in dns_servers:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [server]
        try:
            answer = resolver.resolve(domain)
            print(f"Server {server} resolved {domain} to {answer[0]}")
