import csv

address_a = []
packets = []

final_ip = []
final_packets = []

with open('PCAP Data.csv', newline='') as file:
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    data= (row[0].split(","))
    address_a.append(data[0])
    address_a.append(data[1])
    packets.append(data[2])
    packets.append(data[5])
    packets.append(data[7])
  ip_list = sorted(set(address_a))
  packets_list = sorted(set(packets))
  packets_list.pop(-1)
  packets_list.pop(-1)
  packets_list.pop(-1)
  ip_list.pop(-1)
  ip_list.pop(-1)
  for item in ip_list:
    format = item.replace('"','')
    final_ip.append(format)
  for item in packets_list:
    format = item.replace('"','')
    final_packets.append(format)

f = open("pcap_results.txt", "w")
f.write(f"Unique IP Addresses: {final_ip} \n\nUnique Packets: {final_packets}")
f.close()
