from scapy.all import sniff, Ether

def process_packet(packet):
    if packet.haslayer(Ether):
        eth_layer = packet.getlayer(Ether)
        print(f"Pacote capturado:")
        print(f"  - Endereço MAC de Destino: {eth_layer.dst}")
        print(f"  - Endereço MAC de Origem: {eth_layer.src}")
        print(f"  - Tipo: {hex(eth_layer.type)}")
        print("-" * 50)

def main(interface):
    print(f"Iniciando captura de pacotes na interface {interface}...")
    sniff(iface=interface, prn=process_packet, filter="ether", store=0)

if __name__ == "__main__":
    interface = input("Digite a interface de rede para captura (ex: eth0, wlan0): ")
    main(interface)
