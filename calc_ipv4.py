"""Cálculo de sub-redes IPV4

Processo para fazer o cálculo:
    1º - Converter números decimais do IP para Binário;
    2º - Descobrir a máscara de Sub Rede (para isso precisamos do prefixo
    ou se ter o prefixo e não a máscara conseguiremos descobrir a máscara
    com o préfixo também!);
    3º - Calcular a quantidade de hosts (IPs válidos para serem usados)
    que poderemos ter para essa rede;
    4º - Transformar os bits da máscara em decimal;
    5º Descobrir o IP da Rede (primeiro IP) e Broadcast (último IP);
"""


import re


class CalcIPV4:
    """Faz o cálculo de redes IPv4

    Modo de uso 1:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', prefixo=10)

    Modo de uso 2:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.0')
    """

    def __init__(self, ip, mascara=None, prefixo=None) -> None:
        """Inicializa/Constrói os dados necessários"""
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        if mascara is None and prefixo is None:
            raise ValueError('Precisa enviar máscara ou prefixo')

        if mascara and prefixo:
            raise ValueError('Precisa enviar máscara ou prefixo, não ambos.')
        # Verifica se foi enviado a máscara ou prefixo. Não pode enviar ambos!

        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):

        if not self._valida_ip(ip):
            # Se não for True
            raise ValueError('IP inválido.')

        self._ip = ip
        self._ip_bin = self._ip_to_bin(ip)

    @property
    def mascara(self):
        return self._mascara

    @mascara.setter
    def mascara(self, mascara):

        if not mascara:
            return

        if not self._valida_ip(mascara):
            # Se não for True
            raise ValueError('Máscara inválida.')

        self._mascara = mascara
        self._mascara_bin = self._ip_to_bin(mascara)

        if not hasattr(self, 'prefixo'):
            # Se não foi configurado o prefixo, configure
            self.prefixo = self._mascara_bin.count('1')

    @property
    def prefixo(self):
        return self._prefixo

    @prefixo.setter
    def prefixo(self, prefixo):
        if not prefixo:
            return

        if not isinstance(prefixo, int):
            # Se não for tipo inteiro
            raise TypeError('Prefixo precisa ser número inteiro')

        if prefixo > 32:
            # Se for mais que 32
            raise ValueError('Prefixo só pode ter até 32 bits')

        self._prefixo = prefixo
        self._mascara_bin = (prefixo * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            # Se não foi configurado a máscara, configure
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        """Valida IP decimal

        Função recebe um IP e válida.
        Se for válido com sucesso retorna True, se não, retorna nada

        O chápeu ^ significa valor inicial já o cifrão $ valor final;
        Quando tem os parênteses () será um conjunto dentro dele;
        [0-9] que dentro do conjunto possua somente números de 0 até 9;
        {1,3} que dentro do conjunto tenha no máximo 3 caracteres e
        no mínimo 1 caracter;
        Já o . seria do ip mesmo;
        E assim formamos a máscara de validação que queremos para o IP
        ser válido com sucesso.
        """
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        """Converte IP decimal para binário

        Função receberá um IP decimal, irá fazer o split dela pelo pontos
        e após isso irá fazer uma list compreehsion para converter para
        binário e por fim verifica a quantidade de bits (caracteres).
        """
        blocos = ip.split('.')
        blocos_bin = [bin(int(x))[2:].zfill(8) for x in blocos]
        blocos_bin_str = ''.join(blocos_bin)
        qtd_bits = len(blocos_bin_str)

        if qtd_bits > 32:
            raise ValueError('IP ou máscara tem mais que 32 Bits')

        return blocos_bin_str

    @staticmethod
    def _bin_to_ip(bin_ip):
        """Converte IP binário para decimal

        Função receberá um IP binário, irá fazer uma list compreehsion
        para converter de binario para decimal.
        Por fim irá juntar os blocos do IP decimal pelo ponto e retornará.
        """
        n = 8
        blocos = [str(int(bin_ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        """Configura o ip de broadcast"""
        hosts_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (hosts_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        """Configura o ip da rede"""
        hosts_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (hosts_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_numero_ips(self):
        """Retorna a quantidade de IPs válidos para serem usados"""
        return ((2 ** (32 - self.prefixo)) - 2)

    def info(self):
        """Exibe as informações do cálculo"""
        print(f'IP: {self.ip}')
        print(f'Máscara: {self.mascara}')
        print(f'Rede: {self.rede}')
        print(f'Broadcast: {self.broadcast}')
        print(f'Prefixo: /{self.prefixo}')
        print(f'Número de IPs válido para a Rede: {self.numero_ips}')


if __name__ == '__main__':
    calcipv4 = CalcIPV4(ip='192.168.6.26', mascara=None, prefixo=1)
    calcipv4.info()
