import csv
import time

def filter_logs(file_path, ip_range, methods, min_responce_time):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ip = row['ip']
            method = row['method']
            response_time = float(row['response_time'])

            if ip_in_range(ip, ip_range) and method in methods and response_time >= min_responce_time:
                yield row

def ip_in_range(ip, ip_range):
    start, end = ip_range
    return start <= ip <= end

def analyze_logs(file_path, ip_range, methods, min_responce_time):
    unique_ips = set()
    method_counts = {method: 0 for method in methods}
    total_response_time = 0
    log_count = 0

    for log in filter_logs(file_path, ip_range, methods, min_responce_time):
        unique_ips.add(log['ip'])
        method_counts[log['method']] += 1
        total_response_time += float(log['response_time'])
        log_count += 1

    avg_response_time = total_response_time / log_count if log_count else 0;

    return {
        'unique_ips': len(unique_ips),
        'method_counts': method_counts,
        'average_response_time': avg_response_time
    }

if __name__ == '__main__':
    file_path = 'server_logs.csv'
    ip_range = ('192.168.1.1', '192.168.1.255')
    methods = ['GET', 'POST']
    min_response_time = 100

    stats = analyze_logs(file_path, ip_range, methods, min_response_time)
    print("Log Analysis Statistics:", stats)
