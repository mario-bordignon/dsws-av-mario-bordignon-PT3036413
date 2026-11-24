from datetime import datetime
from sqlalchemy import func
from flask import render_template, redirect, url_for, flash, current_app
from . import main
from .forms import ProfessorForm
from .. import db
from ..models import Professor, Disciplina


# --- Data e hora local (disponível em todos os templates) ---
@main.app_context_processor
def inject_time():
    return dict(current_time=datetime.utcnow())


# --- Página principal ---
@main.route('/')
def index():
    return render_template('index.html',
                           aluno=current_app.config['ALUNO_NOME'],
                           prontuario=current_app.config['ALUNO_PRONTUARIO'])


# --- Cadastro de Professores ---
@main.route('/professores', methods=['GET', 'POST'])
def professores():
    form = ProfessorForm()
    form.disciplina.choices = [
        (d.id, d.nome) for d in Disciplina.query.order_by(Disciplina.id).all()]
    if form.validate_on_submit():
        nome = ' '.join(form.nome.data.split())
        # Procura pelo nome em QUALQUER disciplina (sem diferenciar maiúsculas/minúsculas)
        existente = Professor.query.filter(
            func.lower(Professor.nome) == nome.lower()).first()
        if existente:
            flash('Professor já existe na base de dados!')
        else:
            professor = Professor(nome=nome,
                                  disciplina_id=form.disciplina.data)
            db.session.add(professor)
            db.session.commit()
            flash('Professor cadastrado com sucesso!')
        return redirect(url_for('.professores'))
    lista = Professor.query.order_by(Professor.id).all()
    return render_template('professores.html', form=form, professores=lista)


# --- Módulos ainda não desenvolvidos: só a mensagem "Não disponível" ---
@main.route('/disciplinas')
def disciplinas():
    return render_template('nao_disponivel.html',
                           modulo='Cadastro de Disciplinas')


@main.route('/alunos')
def alunos():
    return render_template('nao_disponivel.html', modulo='Cadastro de Alunos')


@main.route('/cursos')
def cursos():
    return render_template('nao_disponivel.html', modulo='Cadastro de Cursos')


@main.route('/ocorrencias')
def ocorrencias():
    return render_template('nao_disponivel.html',
                           modulo='Cadastro de Ocorrências')