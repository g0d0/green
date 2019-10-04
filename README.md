# green
Green - OSINT Recon tool

## PREREQUISITES
- git
- python 3.x
- John The Ripper
- Netcat
- Scapy (0.25)
- Requests (2.19.1)
- Shodan (1.9.0)
- Beautiful Soup (bs4 0.0.1)

## MAINTAINERS
* **JC GreenMind** |
Twitter: <a href="http://twitter.com/greenmind_br">GreenMind</a>
Github: <a href="https://github.com/greenmind-sec/">GreenMind</a>

## DISCLAIMER
<p align="center">
  TO BE USED FOR EDUCATIONAL PURPOSES ONLY
</p>

The use of the Green is COMPLETE RESPONSIBILITY of the END-USER. Developer assume NO liability and are NOT responsible for any misuse or damage caused by this program.

"DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
Taken from [LICENSE](LICENSE).

## TESTED ON
* **Debian - Stretch**

## CLONE
```sh
git clone https://github.com/greenmind-sec/Green
```

## Ferramenta ainda em desenvolvimento
Recomendamos que use essa Ferramenta junto com o Docker já que é necessario instalar algumas bibliotecas , alem do projeto estar ainda em fase de testes e desenvolvimento.

## Antes de começar

### Configurando keys.json
Vamos criar um arquivos chamado **keys.json** na raiz do projeto.
```sh
{
  "whatcms": "key-whatcms",
  "shodan": "key-shodan",
  "hunter-io": "key-hunterio",
  "green": {
    "version": "v0.3.1DEV"
}
}
```

#### Criando key shodan
```sh
https://account.shodan.io/register
```
> Depois de logado podemos encontrar no topo **Show API Key**

#### Criando key whatcms
```sh
https://whatcms.org/API
```
> Depois de criar uma conta você pode ter acesso a chave.

#### Criando chave hunter.io
```sh
https://hunter.io/api_keys
```
> Depois de criar uma conta só precisamos entrar nesse link e obter a key.

### Criando container docker
Vamos criar nossa imagem do docker com todos os requisitos necessarios.
> Essa é uma versão **Beta** ainda.

Para criar a imagem podemos usar:
```sh
sudo docker build -t "green:1" .
```

Para usar a imagem podemos usar
```sh
sudo docker container run -it --rm -v "${PWD}:/root" "green:1" bash
```
> Dessa forma só precisar ir até o diretorio **cd ~** e dar um **ls** para listar o diretorio.

## Comandos basicos

### Archive
```sh
python3 green.py -t archive -u businesscorp.com.br -o text.txt
```

### Shodan
```sh
python3 green.py -t shodan-search -u businesscorp.com.br -o text.txt
```

### Whois URL
```sh
python3 green.py -t whois-url -u businesscorp.com.br -o text.txt
```

### Whois IP
```sh
python3 green.py -t whois-ip -u 37.59.174.225 -o text.txt
```

### Check Robots.txt
```sh
python3 green.py -t check_robots -u http://businesscorp.com.br -o text.txt
```

### Sharingmyip
```sh
python3 green.py -t sharingmyip -u http://fatecourinhos.edu.br -o text.txt
```

### WhatCMS
```sh
python3 green.py -t check_cms -u http://fatecourinhos.edu.br -o text.txt
```

### hunter.io
```sh
python3 green.py -t hunter-io -u businesscorp.com.br -o text.txt
```

## Donation

## Video
