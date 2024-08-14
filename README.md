[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fsaleonhard%2Fmestredosbots_novospupilos&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
<p align="center">
  <img src="https://github.com/user-attachments/assets/56c16b3d-37d3-498f-849b-1932b37069bb" alt="Descrição da Imagem" width="900" height="auto" />
</p>

# 🧙‍Mestre Dos Bots - Saudação Mágica para Novos Seguidores

## Descrição

🚀 Este projeto implementa um processo secundário, ou worker, do bot "Mestre Dos Bots" no Twitter. Este worker é responsável por saudar novos seguidores da conta @mestredosbots com mensagens personalizadas. Além disso, o processo também seleciona novas frases criativas feitas pelos seguidores ✨, que são salvas e podem ser usadas em saudações futuras. O worker foi originalmente projetado para rodar no ambiente de nuvem Heroku ☁️, utilizando a API do Twitter via a biblioteca Tweepy 🐦, e interage com o Google Sheets para armazenar e ler dados 📊.

## Worker Principal

Este projeto faz parte de um conjunto de processos. Para acessar o repositório do worker principal, visite [🧙‍♂️Mestre Dos Bots](https://github.com/saleonhard/mestredosbots_).


## Requisitos

Para rodar este projeto, você precisará dos seguintes itens:

1. **Python 3.x**
2. **Bibliotecas Python**:
   - `tweepy`: Biblioteca para interagir com a API do Twitter.
   - `gspread`: Biblioteca para manipular planilhas do Google Sheets.
   - `oauth2client`: Biblioteca para autenticação via OAuth 2.0.

3. **Credenciais**:
   - **Twitter API**: Você precisa de uma chave e um segredo do consumidor (Consumer Key e Consumer Secret), além de um token de acesso e seu segredo (Access Token e Access Secret). Esses valores devem ser armazenados em um arquivo `keys.py`.
   - **Google Sheets API**: Gere e faça o download das credenciais JSON para a API do Google Sheets e renomeie para `credenciais.json`.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas. Você pode instalar todas as dependências com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Estrutura do Código

### Autenticação

O script faz autenticação tanto com a API do Twitter quanto com a API do Google Sheets.

### Leitura de Dados

O número atual de seguidores e o último usuário seguido são armazenados em uma planilha do Google Sheets.

### Saudação de Novos Seguidores

- O bot compara o número atual de seguidores com o último número registrado e, se houver novos seguidores, envia uma mensagem personalizada a cada novo seguidor.
- As mensagens variam de acordo com um número aleatório, designando ao novo seguidor uma classe fictícia relacionada aos personagens do desenho animado 'Caverna do Dragão', como Sheila, Bobby, Presto, Diana, Eric, ou Hank. Cada personagem é representado por um GIF exclusivo, tornando a saudação ainda mais divertida e personalizada.

<p align="center">
  <img src="https://github.com/user-attachments/assets/b4426e4f-27e2-43ef-9969-6764f6f0a246" alt="1" width="200" height="200" />
  <img src="https://github.com/user-attachments/assets/aead142e-e575-4de7-9203-cdace21e25d5" alt="5" width="200" height="200" />
  <img src="https://github.com/user-attachments/assets/8f0221fe-5833-4a53-a397-bdb6af361146" alt="4" width="200" height="200" />
  <img src="https://github.com/user-attachments/assets/ffbeec73-cf0a-4926-a07d-61d479fbf4d8" alt="3" width="200" height="200" />
  <img src="https://github.com/user-attachments/assets/fc473229-0d49-4df9-8ba5-bca2a379e700" alt="2" width="200" height="200" />
  <img src="https://github.com/user-attachments/assets/834131b4-2671-403b-b43e-602473961a1d" alt="6" width="200" height="200" />
</p>


### Atualização de Dados

Após cada verificação, o número atual de seguidores e o nome do último seguidor são atualizados na planilha do Google Sheets.

## Função Principal: `saudar`

A função `saudar` é responsável por:

- Verificar o número de novos seguidores.
- Se houver novos seguidores, saudá-los com uma mensagem personalizada e uma imagem correspondente.
- Atualizar as informações na planilha do Google Sheets.

### Exemplo de Uso

```python
import time

while True:
    saudar()
    time.sleep(900)  # Espera 15 minutos antes de verificar novamente

```
Este processo worker foi configurado para rodar como um "dyno worker" no Heroku, sendo executado em segundo plano. Ele complementa o processo principal do bot, que gerencia outras funcionalidades.

## Como Executar

1. Certifique-se de que todas as dependências estão instaladas.
2. Coloque suas credenciais nos arquivos `keys.py` e `credenciais.json`.
3. Execute o script principal.

```bash
python timeline.py

```
## Observações

- ⏳ O bot foi configurado para esperar 15 minutos entre cada verificação de novos seguidores, para evitar o limite de taxa da API do Twitter.
- 🖼️ As imagens e mensagens devem estar corretamente configuradas no diretório onde o script é executado.

## Licença

📜 Este projeto é distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo como quiser! ✨.

## Contato
Se você tiver alguma dúvida ou sugestão, entre em contato:
    
- ✉️ **Email:** sa.leonardo13@gmail.com
- 🔗 **LinkedIn:** [LinkedIn - Leonardo Aquino](https://linkedin.com/in/aquinoleonardo/)  
