import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Carrega o .env usando o caminho absoluto do projeto,
# funcionando não importa de onde o Flask for iniciado
load_dotenv(os.path.join(basedir, '.env'), override=True)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Identificação do aluno (mostrada na página inicial) ---
    ALUNO_NOME = 'Mario Antonio Bordignon'
    ALUNO_PRONTUARIO = 'PT3036413'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = Config.SECRET_KEY or 'chave-apenas-para-desenvolvimento'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SECRET_KEY = Config.SECRET_KEY or 'chave-apenas-para-testes'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        if not app.config.get('SECRET_KEY'):
            raise RuntimeError(
                'Defina SECRET_KEY no .env de produção (gere uma com: '
                'python -c "import secrets; print(secrets.token_hex(32))").')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
