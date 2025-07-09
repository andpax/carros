from openai import OpenAI

# Inicializa o cliente com a chave e o endpoint do DeepSeek
client = OpenAI(
    api_key='',
    base_url='https://api.deepseek.com'
)

def get_car_ia_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres.
    Fale coisas específicas desse modelo.
    Não adicione no fim da descrição :  (250 caracteres)
    '''
    prompt = prompt.format(brand, model, year)
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {'role': 'system', 'content': 'Você é um assistente de IA especializado em criar descrições criativas de carros.'},
            {'role': 'user', 'content': prompt},
        ],
        max_tokens=1000,
        temperature=0.8,
        stream=False
    )

    return response.choices[0].message.content





# def get_car_ia_bio(model, brand, year):
#     prompt = '''
#     '''
#     openai.OpenAI = ''
#     response = openai.Completion.create(
#         model='',
#         prompt=prompt,
#         max_tokens=1000,
#     )
#     return response['choise'][0]['text']