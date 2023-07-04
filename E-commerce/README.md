# Relatório - E-Commerce

A aplicação foi construída utilizando os conceitos de microsserviços e arquitetada com Docker e Docker-Compose.

## Novas Atualizações

- Agora, é possivel cadastrar mais de 2 produtos e Usuarios.
- Alteração de Produtos e Usuarios ja cadastrados.
- Exclusão de Produtos e Usuarios ja cadastrados.
- Criação da Imagem no Docker Compose
- Modelo de Front-end

## Requisitos

- Java 17 – JDK:
- Maven
- Docker
- IntelliJ IDEA
- Postgresql
- Postman

## Arquitertura do Sistema

![Green Minimalist Process System Mind Map](https://github.com/JassonJr1/sistemas-distribuidos/assets/99465676/c7c56a8a-0447-429a-936d-9da1331278f0)

### Micro-serviços

- Custumer
- Product
- Order

# Executando

- Verifique se todos os requisitos estão ativos
- Clone o repositorio
- Inicie o processo do docker compose:
  
      docker compose up --build
  
- Para testar os micro-serviços, abra o POSTMAN
