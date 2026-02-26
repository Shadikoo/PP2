#1
import json

# Чтение данных из файла
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Заголовок
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 8 + " " + "-" * 6)

# Парсинг и вывод данных
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    descr = attributes.get('descr', '') or ''
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")

#2
import json

with open('sample-data.json', 'r') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 8 + " " + "-" * 6)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs["dn"]
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "inherit")
    mtu = attrs.get("mtu", "")
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")