# 🚗 Sistema Web para Locadora de Veículos

<p align="center">
    Bem-vindo ao repositório do <strong>Sistema de Gerenciamento para Locadora de Veículos</strong>!  
    Este projeto foi desenvolvido utilizando <strong>Django</strong>, com foco em organização, controle operacional e gerenciamento completo de uma locadora de veículos.
</p>

---

# 🧐 Sobre o Projeto

O sistema foi criado com o objetivo de auxiliar no gerenciamento interno de uma empresa de locação de veículos, permitindo o controle de:

- Clientes
- Motoristas
- Veículos
- Fornecedores
- Rotas
- Diário de Bordo
- Filiais
- Usuários e permissões

O projeto possui autenticação de usuários, controle por filial, dashboard administrativo e sistema de perfis com gerenciamento de acesso.

Além disso, o sistema foi desenvolvido com foco em:

✅ Organização de código utilizando arquitetura MVC/MVT  
✅ Interface moderna com Bootstrap  
✅ Segurança de autenticação do Django  
✅ Relacionamentos entre tabelas  
✅ Escalabilidade para futuras melhorias  

---

# 🛠️ Tecnologias Utilizadas

<div align="center">

<img src="https://img.icons8.com/color/96/python.png" height="40" alt="Python" title="Python"/>
<img width="12" />

<img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" height="40" alt="Django" title="Django"/>
<img width="12" />

<img src="https://img.icons8.com/color/96/html-5--v1.png" height="40" alt="HTML5" title="HTML5"/>
<img width="12" />

<img src="https://img.icons8.com/color/96/css3.png" height="40" alt="CSS3" title="CSS3"/>
<img width="12" />

<img src="https://img.icons8.com/color/96/javascript--v1.png" height="40" alt="JavaScript" title="JavaScript"/>
<img width="12" />

<img src="https://img.icons8.com/color/96/bootstrap.png" height="40" alt="Bootstrap" title="Bootstrap"/>
<img width="12" />

<img src="https://img.icons8.com/fluency/96/sql.png" height="40" alt="SQLite" title="SQLite"/>

</div>

---

# 📂 Funcionalidades do Sistema

## 👤 Usuários
- Login e logout
- Cadastro de usuários
- Perfis personalizados
- Alteração de senha
- Edição de perfil
- Controle de permissões
- Verificação de e-mail duplicado

---

## 🏢 Filiais
- Cadastro de filiais
- Relacionamento entre usuários e filiais
- Controle de dados separados por filial

---

## 👥 Clientes
- Cadastro de clientes
- Edição e exclusão
- Associação automática à filial do usuário logado

---

## 🚚 Motoristas
- Cadastro de motoristas
- Controle por filial
- Edição e exclusão

---

## 🚗 Veículos
- Cadastro de veículos
- Controle de informações dos veículos
- Gerenciamento por filial

---

## 🗺️ Rotas
- Cadastro de rotas
- Controle de trajetos
- Relacionamento com motoristas e veículos

---

## 📦 Fornecedores
- Cadastro de fornecedores
- Associação com filiais
- Edição e exclusão

---

## 📘 Diário de Bordo
- Registro de atividades
- Controle operacional
- Histórico interno

---

# ⚡ Como Executar o Projeto

## 📌 Pré-requisitos

Antes de começar, você precisará ter instalado:

- Python 3.10+
- Pip
- Git

---

# 🚀 Passo a Passo

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd ProjetoIntegrador
```

---

## 3️⃣ Crie um ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Execute as migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Crie um superusuário

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Inicie o servidor

```bash
python manage.py runserver
```

---

## 8️⃣ Acesse no navegador

```txt
http://127.0.0.1:8000/
```

---

# 🔐 Sistema de Autenticação

O sistema utiliza autenticação nativa do Django com:

- Login seguro
- Sessões autenticadas
- Controle de permissões
- Proteção CSRF
- Restrição de acesso por usuário

---

# 🎨 Interface do Sistema

O sistema possui:

✅ Sidebar moderna  
✅ Dashboard administrativo  
✅ Layout responsivo  
✅ Bootstrap Icons  
✅ Cartões informativos  
✅ Destaque de menu ativo  
✅ Perfil de usuário estilizado  

---

# 🧠 Estrutura do Projeto

```txt
ProjetoIntegrador/
│
├── clientes/
├── fornecedores/
├── motoristas/
├── veiculos/
├── rotas/
├── diario/
├── core/
│
├── templates/
├── static/
│
├── manage.py
└── db.sqlite3
```

---

# 🔄 Melhorias Futuras

Algumas melhorias planejadas:

- Upload de imagens
- Relatórios em PDF
- Sistema de locação completo
- Controle financeiro
- API REST
- Deploy em nuvem
- Notificações
- Dashboard avançado
- Sistema de manutenção de veículos
- Controle de combustível

---

# 🤝 Como Contribuir

Contribuições são muito bem-vindas!

## Passos:

### 1. Faça um fork do projeto

### 2. Clone o fork

```bash
git clone https://github.com/seu-usuario/seu-fork.git
```

### 3. Crie uma branch

```bash
git checkout -b minha-feature
```

### 4. Faça suas alterações

### 5. Commit

```bash
git commit -m "Minha nova feature"
```

### 6. Push

```bash
git push origin minha-feature
```

### 7. Abra um Pull Request 🚀

---

# 🛠️ Problemas Comuns

## ❌ Porta já em uso

```bash
Error: That port is already in use
```

Use outra porta:

```bash
python manage.py runserver 8001
```

---

## ❌ Migration quebrada

Tente:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ❌ Ambiente virtual não ativa

No PowerShell:

```bash
Set-ExecutionPolicy Unrestricted
```

---

# 🌎 Acesso Externo

Para acessar o sistema em outro dispositivo:

```bash
python manage.py runserver 0.0.0.0:8000
```

Ou utilize:

- Ngrok
- Render
- Railway

---

# 📝 Licença

Este projeto está sob a licença MIT.

---

# 👨‍💻 Desenvolvedor

<div align="center">

<a href="https://github.com/jailsonneve" target="_blank">
<img src="https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="mailto:daiarthur053@gmail.com" target="_blank">
<img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

<a href="https://www.instagram.com/arthur.dai.52" target="_blank">
<img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/>
</a>

</div>

---

<div align="center">

🚀 Projeto desenvolvido para fins acadêmicos e aprimoramento profissional.

</div>

---

# 👀 Visitantes

<div align="center">
  <img src="https://profile-counter.glitch.me/ProjetoIntegrador/count.svg?" />
</div>