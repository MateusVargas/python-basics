from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))# convertendo pro formato brasileiro
    print(data_atual.strftime('%A %B %Y'))#trazendo dia mes e ano

def trabalhando_com_time():
    horario = time(15,17,50)#criando variavel com formato de hora
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data_atual = datetime.now()#pegando data e hora atuais
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S'))#só a hora
    print(data_atual.strftime('%d-%m-%Y'))#só a data
    print(data_atual.day)#pegando o número do dia
    print(data_atual.year)#pegando o ano
    print(data_atual.month)#pegando o mês
    dias = ('segunda','terça','quarta','quinta','sexta','sábado','domingo')
    print(dias[data_atual.weekday()])#dia da semana
    data_criada = datetime(2020, 5, 26, 19, 2, 12)#criando uma datas
    print(data_criada)

    data_string = '09/12/2001'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

    nova_data = data_convertida - timedelta(days=350, hours=4, minutes=34)#subtraindo dias, horas e minutos de uma data
    print(nova_data)#tambem pode-se somar dias, horas etc..



if __name__ == "__main__":
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()