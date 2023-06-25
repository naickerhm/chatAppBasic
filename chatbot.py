from cgitb import small
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import collections.abc


collections.Hashable = collections.abc.Hashable

# params: read_only (true = bot will not train)
#         logic_adapters (list of adapters bot trains from) 

# chatterbot.logic.MathematicalEvaluation: lib for maths problems
# chatterbot.logic.BestMatch: lib that helps bot choose best match from responses. Decision-making assistance
Rachael_Rosen = ChatBot(name='Nexus-6', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

# Material to train from:

corpus_trainer = ChatterBotCorpusTrainer(Rachael_Rosen)
corpus_trainer.train('chatterbot.corpus.english')

print("\nI'm Rachael Rosen and I've just completed my training.\n")

chat = ''
while chat != 'quit':
    chat = input("Rachael Rosen: ask me anything... or type quit...\n")
    response = Rachael_Rosen.get_response(chat)
    print("Rachael Rosen: ", response)

