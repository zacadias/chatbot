import chatterbot.trainers
from chatterbot import ChatBot

bot = ChatBot('Bot')

nome = input('Digite seu nome: ')

convA = ('oi', 'ola', 'ola, bom dia', 'bom dia', 'bom dia, como vai?', 'estou bem!', 'boa noite', 'durma bem')

convB = ('Qual filme voce gosta?', 'Eu gosto de Eu Robo.', 'tem outro filme?', 'hackers!')

convC= ('Qual e o seu nome', 'meu nome é bot', 'bot?', 'e, nao gostou?', 'estranho', 'diferente', 'é diferente, ne?')

convD = ('noticias', 'que tipo de noticias?', 'noticias variadas', 'do brasil?', 'sim, e do mundo tambem')

bot.set_trainer(chatterbot.trainers.ListTrainer)

bot.train(convA)
bot.train(convB)
bot.train(convC)
bot.train(convD)
print('-=' * 40)

print('Bem Vindo ao Chat!')

print('-=' * 40)
while True:
    quest = input(nome )

    response = bot.get_response(quest)

    if float(response.confidence) > 0.5:

        print('Bot:', response)

    else:

        print('Bot: Não entendi, isso não está na minha base de dados')
