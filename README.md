# 🧮 SENAI - Calculadora de IMC com Django

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Linguagem](https://img.shields.io/badge/Python-3.x-blue)
![Framework](https://img.shields.io/badge/Django-5.x-092e20)

### 📋 Sobre o Projeto
Esta é uma aplicação web desenvolvida durante as aulas de Python no SENAI. O objetivo é calcular o Índice de Massa Corporal (IMC) a partir do peso e altura fornecidos pelo usuário, retornando o valor exato e a classificação oficial de saúde.

### 🚀 Funcionalidades
* Cálculo de IMC em tempo real.
* Classificação automática (Abaixo do peso, Peso normal, Obesidade, etc.).
* Interface responsiva e personalizada com CSS.
* Proteção de segurança nativa do Django (CSRF Token).

### 🛠️ Tecnologias Utilizadas
* **Python**: Lógica de programação e cálculos.
* **Django**: Framework web para estruturação do sistema.
* **HTML5/CSS3**: Estrutura visual e estilização profissional.

### 🔧 Como rodar o projeto localmente

1. **Clone este repositório:**
   ```bash
   git clone https://github.com
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv .venv
   ```

3. **Ative o ambiente:**
   * Windows: `.venv\Scripts\activate`
   * Linux/Mac: `source .venv/bin/activate`

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute as migrações e inicie o servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---
🎨 **Desenvolvido por:** [Guilherme Moreli]  
🏫 **Instituição:** SENAI Sertãozinho
