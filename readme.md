# Captura e Análise de Pacotes com Scapy

Este projeto tem como objetivo capturar e analisar pacotes Ethernet em uma rede usando a biblioteca Python `scapy`. O script captura pacotes em tempo real e exibe informações sobre os quadros Ethernet, como endereços MAC e tipo de protocolo encapsulado.

### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/Package_Capture.git
```


### Instalação das Dependências

Se ainda não tiver as bibliotecas instaladas, use:

```
pip install scapy
```

### Executando o Projeto

Para iniciar o programa, execute:

```
sudo python3 main.py
```

Quando solicitado, insira o nome da interface de rede para captura (por exemplo, `eth0` para Ethernet ou `wlan0` para Wi-Fi).

### Observações
- Você pode verificar o nome da interface de rede com:
    ```
    ifconfig
    ```
- Pode ser necessário rodar a aplicação como superusuário para ter o acesso necessário. Em caso de erro na importação tente instalar o scapy com o mesmo usuário que executa aplicação.

<div align="center">
<img src=print.png >

<i><b>Simulação</b> da execução do programa</i>
</div>


## Teoria de Comunicação de Dados

### Protocolo Ethernet

O protocolo Ethernet é uma tecnologia de rede usada para comunicação em redes locais (LANs). Ele opera na camada de enlace do modelo OSI e define o formato dos quadros de dados transmitidos entre dispositivos na mesma rede.

#### Estrutura do Quadro Ethernet

Um quadro Ethernet é composto pelos seguintes campos:

1. **Preamble (Pré-cabeça):** Sequência de bits usada para sincronizar o receptor com o início do quadro.
2. **Endereço MAC de Destino:** Identifica o dispositivo destinatário na rede.
3. **Endereço MAC de Origem:** Identifica o dispositivo remetente.
4. **Tipo (ou EtherType):** Indica o protocolo de camada superior encapsulado no quadro (por exemplo, IPv4, ARP).
5. **Dados:** Contém o pacote de camada superior (por exemplo, um pacote IP).
6. **FCS (Frame Check Sequence):** Usado para verificar a integridade dos dados transmitidos.

### Captura de Pacotes

A captura de pacotes permite monitorar o tráfego de rede e diagnosticar problemas. O `scapy` é uma biblioteca Python que facilita a criação, manipulação e análise de pacotes de rede.

