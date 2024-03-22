# Dicionário de associação entre tipos de armas e raridades e os tipos de monstros fortes
armas_fortes_por_raridade = {
    'espada': {
        'único': ['fera', 'demônio', 'servo', 'troll'],
        'raro': ['fera', 'servo', 'troll', 'demônio'],
        'épico': ['trasgo', 'bandido', 'golem', 'milícia'],
        'lendário': ['zumbi', 'bandido']
    },
    'machado': {
        'único': ['fera', 'demônio', 'servo', 'troll'],
        'raro': ['bandido', 'zumbi'],
        'épico': ['fera', 'servo', 'troll', 'demônio'],
        'lendário': ['milícia', 'trasgo']
    }
}

# Função para obter os tipos de monstros fortes contra os quais uma arma deve ser forjada
def tipos_monstros_fortes(arma, raridade):
    if arma in armas_fortes_por_raridade and raridade in armas_fortes_por_raridade[arma]:
        return armas_fortes_por_raridade[arma][raridade]
    else:
        return "Combinação de arma e raridade não encontrada."

# Solicitar entrada do usuário para o tipo de arma e raridade desejada
arma_desejada = input("Digite o tipo de arma desejada (espada ou machado): ").lower()
raridade_desejada = input("Digite a raridade desejada (único, raro, épico, lendário): ").lower()

# Verificar os tipos de monstros fortes contra os quais a arma deve ser forjada
monstros_fortes = tipos_monstros_fortes(arma_desejada, raridade_desejada)
if monstros_fortes != "Combinação de arma e raridade não encontrada.":
    print(f"A {arma_desejada} de raridade {raridade_desejada} armas que podem forjar dessa raridade: {', '.join(monstros_fortes)}")
else:
    print("Combinação de arma e raridade não encontrada.")
