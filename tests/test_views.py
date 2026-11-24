import unittest
from app import create_app, db
from app.models import Professor, Disciplina


class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        db.session.add(Disciplina(nome='DSWA5'))
        db.session.commit()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_mostra_nome_e_prontuario(self):
        resposta = self.client.get('/')
        self.assertEqual(resposta.status_code, 200)
        html = resposta.get_data(as_text=True)
        self.assertIn('Mario Antonio Bordignon', html)
        self.assertIn('PT3036413', html)

    def test_modulos_nao_desenvolvidos(self):
        for rota in ['/disciplinas', '/alunos', '/cursos', '/ocorrencias']:
            resposta = self.client.get(rota)
            self.assertEqual(resposta.status_code, 200)
            self.assertIn('Não disponível', resposta.get_data(as_text=True))

    def test_cadastro_de_professor(self):
        disciplina = Disciplina.query.first()
        resposta = self.client.post('/professores', data={
            'nome': 'Fabio Teixeira', 'disciplina': disciplina.id},
            follow_redirects=True)
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(Professor.query.count(), 1)
        html = resposta.get_data(as_text=True)
        self.assertIn('Fabio Teixeira', html)
        self.assertIn('DSWA5', html)

    def test_professor_sem_nome_nao_e_salvo(self):
        disciplina = Disciplina.query.first()
        self.client.post('/professores', data={
            'nome': '', 'disciplina': disciplina.id})
        self.assertEqual(Professor.query.count(), 0)

    def test_pagina_inexistente_da_404(self):
        self.assertEqual(self.client.get('/nao-existe').status_code, 404)
