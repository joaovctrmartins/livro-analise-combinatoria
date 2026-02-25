# 1. Entrada de dados
print("--- Calculadora de Lanches da Fernanda ---")
pao_sal = int(input("Digite a quantidade de pães de sal: "))
pao_doce = int(input("Digite a quantidade de pães doces: "))
ovo = int(input("Digite a quantidade de porções de ovo: "))
pasta = int(input("Digite a quantidade de porções de pasta de amendoim: "))
cafe = int(input("Digite a quantidade de porções de café: "))
suco = int(input("Digite a quantidade de porções de suco: "))

# 2. Processamento: Caso 1 - Lanches com Pão de Sal
# Regra: Obriga o uso da pasta de amendoim. Bebida é livre (café ou suco).
lanches_sal = pao_sal * pasta * (cafe + suco)

# 3. Processamento: Caso 2 - Lanches com Pão Doce
# Subcaso 2.1: Com ovo (obriga a ser suco)
lanches_doce_ovo = pao_doce * ovo * suco

# Subcaso 2.2: Com pasta de amendoim (bebida livre)
lanches_doce_pasta = pao_doce * pasta * (cafe + suco)

# Total de lanches com pão doce
lanches_doce = lanches_doce_ovo + lanches_doce_pasta

# 4. Processamento: Total Geral
total_lanches = lanches_sal + lanches_doce

# 5. Saída de dados
print("\n--- Resultado ---")
print(f"Lanches possíveis com pão de sal: {lanches_sal}")
print(f"Lanches possíveis com pão doce: {lanches_doce}")
print(f"Total de combinações possíveis: {total_lanches}")