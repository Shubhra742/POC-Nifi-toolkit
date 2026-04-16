import sys
import json
import subprocess

flow_name = sys.argv[1].lower()
props_file = sys.argv[2]
root_pgid = sys.argv[3]

result = subprocess.run([
    '/opt/nifi/nifi-toolkit-2.8.0/bin/cli.sh',
    'nifi', 'pg-list',
    '-p', props_file,
    '-pgid', root_pgid,
    '-ot', 'json'
], capture_output=True, text=True)

data = json.loads(result.stdout)
for pg in data:
    flow_id = pg.get('versionControlInformation', {}).get('flowId', '').lower()
    if flow_id == flow_name and pg.get('versionControlInformation'):
        print(pg['id'])
        break
