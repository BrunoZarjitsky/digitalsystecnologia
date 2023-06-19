# Sistema de gestão de propostas de empréstimo pessoal

Desafio técnico proposto pela DigitalsysTecnologia

## Desafio

- Criar um sistema onde os usuários possam cadastrar propostas de empréstimo pessoal.
- As propostas devem ser enviadas para uma fila no RabbitMQ, e o Django Celery ficará responsavel por fazer a avaliação da proposta.
- No Django admin, deve ser possivel visualizar as propostas cadastradas juntamente com seus respectivos status.
- Deve ser criada uma página para que o cliente faça o preenchimento da proposta, essa pagina não deve se comunicar diretamente com o Django, ou seja, toda comunicação deve ser feita através do Django Rest Framework.

## Estrutura da Proposta

- Nome completo
- CPF
- Endereço
- Valor do empréstimo pretendido

## Orientações de execução do projeto

Clone este repositório em sua maquina, e execute o projeto com o comando 
```
docker-compose up
```
Aguarde a inicialização de todos os containers, geralmente na primeira execução do projeto, o ultimo a terminar de iniciar é o frontend_1.

Para acessar o frontend, acesse em seu browser o endereço:

http://localhost:3000/

Onde você poderá ver uma lista com todas as propostas já cadastradas, ou ir para a pagina de cadastro de nova proposta, clicando no link Nova Proposta, ou acessando o endereço:

http://localhost:3000/nova_proposta

Para o admin, vá para o endereço:

http://localhost:8000/admin/

E use para acessar as seguintes credenciais

- Usuário: digitalsystecnologia
- Senha: admin

Para visualisar as propostas já cadastradas, acesse o endereço:

http://localhost:8000/admin/propostas/proposta/

Para fins de validação do funcionamento do sistema, criei duas ações no admin
- Bota em análise: Define o status de todas as propostas selecionadas como em analise.
- Solicitar avaliação: Envia as propostas selecionadas para a fila de avaliação no RabbitMQ

### Espero que gostem da minha solução, obrigado =)