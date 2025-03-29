import csv

address_a = []
ports = []

final_ip = []
final_ports = []

def combine_lists(list1, list2):
  """Combines two lists in the format list1[0]:list2[0], list1[1], list2[1], ..."""
  combined_list = []
  min_length = min(len(list1), len(list2))

  for i in range(min_length):
      combined_list.append(f"{list1[i]}:{list2[i]}")

  combined_list.extend(list1[min_length:])
  combined_list.extend(list2[min_length:])

  return combined_list

with open('PCAP data 2.csv', newline='') as file:
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    data= (row[0].split(","))
    address_a.append(data[0])
    ports.append(data[1])
  ports.remove("Port A")
  address_a.remove("Address A")
  for item in address_a:
    format = item.replace('"','')
    final_ip.append(format)
  for item in ports:
    format = item.replace('"','')
    final_ports.append(format)

final_list=combine_lists(final_ip, final_ports)

print(final_list)
f = open("pcap_results.txt", "w")
f.write(f"Results: {final_list}")
f.close()
