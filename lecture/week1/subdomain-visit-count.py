class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)

        for domain in cpdomains:
            num_visits, subdomain = domain.split(' ')
            
            domains[subdomain] += int(num_visits)
            for i in range(len(subdomain) - 1, -1, -1):
                if subdomain[i] == '.':
                    domains[subdomain[i+1:]] += int(num_visits)
                
        result = []
        for key, value in domains.items():
            result.append(str(value) + " " + key)

        return result