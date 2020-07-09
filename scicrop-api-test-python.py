import json
import datetime
import requests


class Degrees:

    def __init__(self, instituicao, nome_curso, data_inicio, data_termino):
        self.institution_name = instituicao
        self.degree_name = nome_curso
        self.begin_date = data_to_epoch(data_inicio)
        self.end_date = data_to_epoch(data_termino)

    def to_map(self):
        degrees_map = {
            'institution_name': self.institution_name,
            'degree_name': self.degree_name,
            'begin_date': self.begin_date,
            'end_date': self.end_date
        }
        return degrees_map

    def to_json(self):
        return json.dumps(self.to_map())

    def __str__(self):
        return f'Instituição: {self.institution_name}\n' \
               f'Nome do curso: {self.degree_name}\n' \
               f'Data de início: {self.begin_date}\n' \
               f'Data de término: {self.end_date}\n'


class Candidato:

    def __init__(self, nome, email, celular, idade, endereco, inicio_teste, oportunidade, experiencia, graduacao,
                 habilidades,
                 banco_de_dados, hobbies, motivo, url_git):
        self.full_name = nome
        self.email = email
        self.mobile_fone = celular
        self.age = idade
        self.home_address = endereco
        self.start_date = inicio_teste
        self.opportunity_tag = oportunidade
        self.past_jobs_experience = experiencia
        self.degrees = graduacao
        self.programming_skills = habilidades
        self.database_skills = banco_de_dados
        self.hobbies = hobbies
        self.why = motivo
        self.git_url_repositories = url_git

    def to_map(self):
        candidato_map = {
            "full_name": self.full_name,
            "email": self.email,
            "mobile_phone": self.mobile_fone,
            "age": self.age,
            "home_address": self.home_address,
            "start_date": self.start_date,
            "opportunity_tag": self.opportunity_tag,
            "past_jobs_experience": self.past_jobs_experience,
            "degrees": self.degrees,
            "programming_skills": self.programming_skills,
            "database_skills": self.database_skills,
            "hobbies": self.hobbies,
            "why": self.why,
            "git_url_repositories": self.git_url_repositories
        }

        return candidato_map

    def __str__(self):
        return f'''	"full_name": {self.full_name},
	"email": {self.email},
	"mobile_phone": {self.mobile_fone},
	"age": {self.age},
	"home_address": {self.home_address},
	"start_date": {self.start_date},
	"opportunity_tag": {self.opportunity_tag},
	"past_jobs_experience": {self.past_jobs_experience},
	"degrees": {self.degrees},
	"programming_skills": {self.programming_skills},
	"database_skills": {self.database_skills},
	"hobbies": {self.hobbies},
	"why": {self.why},
	"git_url_repositories": {self.git_url_repositories}
        '''

class Http:

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

    def post(self, dados=''):
        req = requests.post(self.__address_post, data=dados)
        print(f'POST -> req: {req}')
        print(f'POST -> req: {req.text}')

    def get(self):
        req = requests.get(self.__address_get)
        print(f'GET -> req: {req}')
        print(f'GET -> req: {req.text}')

    def __str__(self):
        return f'''GET address -> {self.__address_get}\nPOST address -> {self.__address_post}'''


# http_responses = Http()
#
# http_responses.address_get = 'https://github.com/timeline.json'
# http_responses.address_post = 'http://httpbin.org/post'
#
# http_responses.get()
# http_responses.post()


def data_to_epoch(date):
    return int(datetime.datetime(year=int(date[4:8]), month=int(date[2:4]), day=int(date[:2])).timestamp())


def main():
    lic_matematica = Degrees('Universidade de Sao Paulo - USP', 'Licenciatura em Matematica', '01022020', '01012023')
    formacao_python = Degrees('Alura', 'Formacao Python', '05022020', '17022020')
    formacao_sql = Degrees('Alura', 'Formacao SQL com MySQL Server da Oracle', '20042020', '04072020')
    formacao_ds = Degrees('Alura', 'Formacao Data Science', '05022020', '12042020')

    degs = [lic_matematica.to_map(), formacao_python.to_map(), formacao_sql.to_map(), formacao_ds.to_map()]

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
    hobbies = ['Jogar Magic: The Gathering']
    motivo = 'Depois de tanto tempo na docencia, passando também pelo empreendedorismo ' \
             'e o gerenciamento de um site, percebi quanto o desenvolvimento de soluções ' \
             'digitais sao, cada vez mais, necessárias ao paradigma de sociedade neste e nos ' \
             'proximos seculos. Por isso resolvi fazer essa transformação na minha carreira, ' \
             'unindo a paixao pela matematica e o gosto por desenvolvimento.'
    url_git = 'https://github.com/Israelmath'

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

    # i = 1
    # for deg in degs:
    #     print(f'{i} {"=" * 15}')
    #     print(deg)
    #     print('Map: ', deg)
    #     print('JSON: ', deg.to_json(), '\n\n')
    #     i += 1

    # print(israel)
    print(json.dumps(israel.to_map(), indent=4))


if __name__ == '__main__':
    main()

