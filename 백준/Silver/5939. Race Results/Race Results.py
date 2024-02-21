def record_sort(records):
    records.sort(key=lambda x: (x[0], x[1], x[2]))
    return records

def main():
    N = int(input())
    records = [list(map(int, input().split())) for _ in range(N)]
    records = record_sort(records)
    for record in records:
        print("{} {} {}".format(record[0],record[1],record[2]))

if __name__ == "__main__":
    main()