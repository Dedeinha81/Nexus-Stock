# 📦 Nexus-Stock 

O **Nexus-Stock** é um sistema completo de gestão de estoque . Ele foca em escalabilidade e segurança, utilizando uma arquitetura moderna baseada em Django e PostgreSQL para garantir que os dados de inventário sejam processados com integridade.

---

## 🌐 Demo Online
O sistema pode ser acessado em:  
👉 [https://nexus-stock.onrender.com](https://nexus-stock.onrender.com)

> **Nota:** Devido ao plano gratuito do Render, o servidor pode levar alguns minutos para "acordar" no primeiro acesso (Cold Start).

---

## 🛠️ Stack Técnica e Decisões de Projeto

* **Backend:** Framework **Django 6.0** pela sua robustez e facilidade de manutenção.
* **Banco de Dados:** **PostgreSQL** para persistência de dados em ambiente de produção, garantindo suporte a transações complexas.
* **Segurança e Ambiente:** Uso de **python-decouple** para gerenciar chaves secretas e credenciais, mantendo o projeto em conformidade com as melhores práticas (Twelve-Factor App).
* **Servidor de Produção:** **Gunicorn** (Green Unicorn) para lidar com múltiplas requisições de forma assíncrona.
* **Assets:** **WhiteNoise** configurado para servir arquivos estáticos (CSS/JS) diretamente da aplicação, otimizando a entrega.

---

## ✨ Funcionalidades Avançadas

### 🔍 Auditoria Completa (Audit Log)
Implementado via `django-simple-history`, permitindo rastrear cada alteração feita em um produto, incluindo quem alterou e qual era o valor anterior.

### 📊 Dashboard Dinâmico
Visualização em tempo real do status do estoque e métricas de produtos cadastrados via Django Admin.

### 🏗️ Normalização de Dados
Arquitetura de banco de dados relacional com vínculos inteligentes entre Categorias, Fornecedores e Produtos.

### 🔐 CORS & Headers
Configurado com `django-cors-headers` para permitir integrações seguras com frontends externos futuramente.

---

## 🚀 Como Rodar o Projeto Localmente

### 1. Clonar o repositório:

git clone https://github.com/Dedeinha81/Nexus-Stock.git
cd Nexus-Stock

---

2. Criar ambiente virtual:

python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

---

3. Instalar dependências:

pip install -r requirements.txt

---

4. Configurar variáveis de ambiente:
   
Crie um arquivo .env na raiz do projeto e adicione:

Fragmento do código

SECRET_KEY=sua_chave_aqui

DEBUG=True

DATABASE_URL=sqlite:///db.sqlite3

---

5. Executar migrações e rodar:

python manage.py migrate

python manage.py runserver

---

☁️ Infraestrutura de Deploy

O deploy foi realizado no Render, utilizando as seguintes configurações de build:

Build Command: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

Start Command: gunicorn core.wsgi

👤 Autor
Desenvolvido por Andrea Cruz
