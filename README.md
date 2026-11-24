# Avaliação semestral — Desenvolvimento de Sistemas Web

Aluno: Mario Antonio Bordignon
Prontuário: PT3036413

Aplicação Flask hospedada no PythonAnywhere. Funcionalidades implementadas:
página principal (`/`) e Cadastro de Professores (`/professores`). Os demais
módulos (`/disciplinas`, `/alunos`, `/cursos`, `/ocorrencias`) mostram apenas
"Não disponível".

![Tela inicial](docs/tela-inicial.png)

## Estrutura do projeto

```
├── app/
│   ├── __init__.py        # create_app() (application factory) e extensões
│   ├── models.py          # Disciplina, Professor
│   ├── main/              # blueprint "main"
│   │   ├── __init__.py
│   │   ├── errors.py      # páginas 404 e 500
│   │   ├── forms.py       # ProfessorForm
│   │   └── views.py       # rotas
│   ├── static/            # favicon
│   └── templates/         # base, index, professores, nao_disponivel, 404, 500
├── migrations/
├── tests/
├── config.py              # configurações (development / testing / production)
├── flasky.py              # ponto de entrada (FLASK_APP)
├── requirements.txt
└── .env.example
```

## 1. Preparando o ambiente

```powershell
python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. Variáveis de ambiente

Copie `.env.example` para `.env` e preencha. O `.env` não vai para o GitHub.

## 3. Criando o banco de dados (com as disciplinas)

```powershell
flask shell
```

```python
db.create_all()
disciplinas = ['DSWA5', 'GPSA5', 'IHCA5', 'SODA5', 'PJIA5', 'TCOA5']
db.session.add_all([Disciplina(nome=n) for n in disciplinas])
db.session.commit()
exit()
```

## 4. Iniciando localmente

```powershell
flask run --debug
```

Acesse: http://127.0.0.1:5000

## 5. Testes

```powershell
flask test
```

## 6. Produção (PythonAnywhere)

No `.env` do servidor, defina `FLASK_CONFIG=production` e uma `SECRET_KEY` própria
(banco usado: `data.sqlite`). No arquivo WSGI da web app:

```python
from flasky import app as application
```