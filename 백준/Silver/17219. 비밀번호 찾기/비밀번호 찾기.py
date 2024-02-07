def find_passwords(N, M, site_passwords, queries):
    password_dict = {}
    for site, password in site_passwords:
        password_dict[site] = password
    
    for query in queries:
        print(password_dict[query])

N, M = map(int, input().split())
site_passwords = [input().split() for _ in range(N)]
queries = [input().strip() for _ in range(M)]

find_passwords(N, M, site_passwords, queries)