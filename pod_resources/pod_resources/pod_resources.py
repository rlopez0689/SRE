import json
import argparse

parser = argparse.ArgumentParser(description='Pod Resources')
parser.add_argument('manifest')
arguments = parser.parse_args()

with open(arguments.manifest) as data_file:
    data = json.load(data_file)

print('podname', 'cpu_requests', 'cpu_limits', 'ram_requests', 'ram_limits')
for item in data['items']:
    name = item['metadata']['name']
    cpu_limits = memory_limits = cpu_requests = memory_requests = ''
    if item['spec']['containers'][0]['resources'].get('limits'):
        cpu_limits = item['spec']['containers'][0]['resources']['limits'].get('cpu', '')
        memory_limits = item['spec']['containers'][0]['resources']['limits'].get('memory', '')
    if item['spec']['containers'][0]['resources'].get('requests'):
        cpu_requests = item['spec']['containers'][0]['resources']['requests'].get('cpu', '')
        memory_requests = item['spec']['containers'][0]['resources']['requests'].get('memory', '')
    print(name, cpu_requests, cpu_limits, memory_requests, memory_limits, sep='\t')
