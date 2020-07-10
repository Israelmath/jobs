# Python 3.6.9

import json
import datetime
from typing import Dict
import requests


class Degrees:
    """
    Classe responsável por organizar as informações dos cursos e graduações
    Obs: Algumas implementações de métodos serviram como testes
    """

    def __init__(self, instituicao: str, nome_curso: str, data_inicio: str, data_termino: str):
        self.institution_name = instituicao
        self.degree_name = nome_curso
        self.begin_date = data_to_epoch(data_inicio)
        self.end_date = data_to_epoch(data_termino)

    def to_dict(self) -> Dict:
        degrees_map = {
            'institution_name': self.institution_name,
            'degree_name': self.degree_name,
            'begin_date': self.begin_date,
            'end_date': self.end_date
        }
        return degrees_map

    def to_json(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return f'Instituição: {self.institution_name}\n' \
               f'Nome do curso: {self.degree_name}\n' \
               f'Data de início: {self.begin_date}\n' \
               f'Data de término: {self.end_date}\n'


class Candidato:
    """
    Classe responsável por organizar as informações de um candidato
    Obs: Algumas implementações de métodos serviram como testes
    """

    def __init__(self, nome, email, celular, idade, endereco, inicio_teste, oportunidade, experiencia, graduacao,
                 habilidades,
                 banco_de_dados, hobbies, motivo, url_git):
        self.__full_name = nome
        self.__email = email
        self.__mobile_fone = celular
        self.__age = idade
        self.__home_address = endereco
        self.__start_date = inicio_teste
        self.__opportunity_tag = oportunidade
        self.__past_jobs_experience = experiencia
        self.__degrees = graduacao
        self.__programming_skills = habilidades
        self.__database_skills = banco_de_dados
        self.__hobbies = hobbies
        self.__why = motivo
        self.__git_url_repositories = url_git

    def to_dict(self) -> Dict:

        candidato_map = {
            "full_name": self.__full_name,
            "email": self.__email,
            "mobile_phone": self.__mobile_fone,
            "age": self.__age,
            "home_address": self.__home_address,
            "start_date": self.__start_date,
            "opportunity_tag": self.__opportunity_tag,
            "past_jobs_experience": self.__past_jobs_experience,
            "degrees": self.__degrees,
            "programming_skills": self.__programming_skills,
            "database_skills": self.__database_skills,
            "hobbies": self.__hobbies,
            "why": self.__why,
            "git_url_repositories": self.__git_url_repositories
        }

        return candidato_map

    def __str__(self):
        infos =  f'''	"full_name": {self.__full_name},
	"email": {self.__email},
	"mobile_phone": {self.__mobile_fone},
	"age": {self.__age},
	"home_address": {self.__home_address},
	"start_date": {self.__start_date},
	"opportunity_tag": {self.__opportunity_tag},
	"past_jobs_experience": {self.__past_jobs_experience},
	"degrees": {self.__degrees},
	"programming_skills": {self.__programming_skills},
	"database_skills": {self.__database_skills},
	"hobbies": {self.__hobbies},
	"why": {self.__why},
	"git_url_repositories": {self.__git_url_repositories}
        '''

        return infos

class HttpClient:
    """
    Classe responsável pelas requisições HTTP
    Obs: Algumas implementações de métodos serviram como testes
    """

    def __init__(self):
        self.__address_get = ''
        self.__address_post = ''

    @property
    def address_get(self):
        return self.__address_get

    @property
    def address_post(self):
        return self.__address_post

    @address_get.setter
    def address_get(self, new_address):
        self.__address_get = new_address

    @address_post.setter
    def address_post(self, new_address):
        self.__address_post = new_address

    def post(self, dados: str = '', cabecalho: dict = ''):
        """
        Método responsável por enviar a requisição HTTP utilizando o método POST
        :param dados: arquivo opcional, no formato Dict ou JSON, enviado para a API
        :param cabecalho: arquivo opcional, no formato Dict ou JSON, para personalizar os headers
        :return: null
        """

        req = requests.post(self.__address_post, data=dados, headers=cabecalho)
        print(f'POST -> req.status_code: {req.status_code}')
        print(f'POST -> req.body: {req.text}')
        print(f'POST -> req.headers: {req.headers}')

    def get(self):
        req = requests.get(self.__address_get)
        print(f'GET -> req.status_code: {req.status_code}')
        print(f'GET -> req: {req}')
        print(f'GET -> req: {req.text}')

    def __str__(self):
        return f'''GET address -> {self.__address_get}\nPOST address -> {self.__address_post}'''


def data_to_epoch(date: str):
    """
    Função responsável por transformar uma string com uma data no formato dd/mm/aaaa em Unix epoch standard
    :param date: Data em string no formato dd/mm/aaaa
    :return: Unix epoch data
    """
    return int(datetime.datetime(year=int(date[4:8]), month=int(date[2:4]), day=int(date[:2])).timestamp())


def main():
    """
    Função responsável por todas as atribuições dos cursos, dados do candidato, http address para
    o método POST e envio dos dados.
    :return: null
    """

    url_job = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'

    lic_matematica = Degrees('Universidade de Sao Paulo - USP', 'Licenciatura em Matematica', '01022020', '01012023')
    formacao_python = Degrees('Alura', 'Formacao Python', '05022020', '17022020')
    formacao_sql = Degrees('Alura', 'Formacao SQL com MySQL Server da Oracle', '20042020', '04072020')
    formacao_ds = Degrees('Alura', 'Formacao Data Science', '05022020', '12042020')

    degs = [lic_matematica.to_dict(), formacao_python.to_dict(), formacao_sql.to_dict(), formacao_ds.to_dict()]

    nome = 'Israel Alves Lucena Gomes'
    email = 'israel.usp@gmail.com'
    celular = '+55 (11) 9.9800-7721'
    idade = 29
    endereco = 'Rua Doutor Angelo Vita, 180 - Sao Paulo'
    inicio_teste = data_to_epoch('07072020')
    oportunidade = 'Desenvolvedor Python'
    experiencia = 'Trabalhei quase dez anos na docencia, mas este ano resolvi mudar ' \
                  'integralmente minha carreira me voltando completamente para a ' \
                  'area do desenvolvimento.'
    certificados = degs
    habilidades = ['python', 'dart', 'C']
    banco_de_dados = ['mysql', 'mongodb', 'redis']
    hobbies = ['Jogar Magic: The Gathering', 'Assistir a filmes']
    motivo = 'Depois de tanto tempo na docencia, passando também pelo empreendedorismo ' \
             'e o gerenciamento de um site, percebi quanto o desenvolvimento de soluções ' \
             'digitais sao, cada vez mais, necessárias ao paradigma de sociedade neste e nos ' \
             'proximos seculos. Por isso resolvi fazer essa transformação na minha carreira, ' \
             'unindo a paixao pela matematica e o gosto por desenvolvimento.'
    url_git = 'https://github.com/Israelmath'

    content_type: Dict[str, str] = {
        'content-type': 'application/json'
    }

    israel = Candidato(
        nome,
        email,
        celular,
        idade,
        endereco,
        inicio_teste,
        oportunidade,
        experiencia,
        certificados,
        habilidades,
        banco_de_dados,
        hobbies,
        motivo,
        url_git
    )

    http_client_jobs = HttpClient()
    http_client_jobs.address_post = url_job
    http_client_jobs.post(dados=json.dumps(israel.to_dict()), cabecalho=content_type)


if __name__ == '__main__':
    main()

