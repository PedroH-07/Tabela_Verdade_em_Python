valores = (0, 1) # Valores binarios (0 =  False, 1 = True)

print(" A | B | C | D || B OR C | A AND (B OR C) | A AND B AND D | (A AND (B OR C)) OR (A AND B AND D) ") # Cabeçalho da Tabela Verdade
print("-" * 95) # Separação do cabeçalho para a tabela

for A in valores:
    for B in valores:
        for C in valores:
            for D in valores:
                print(f" {A} | {B} | {C} | {D} || {B or C} | {A and (B or C)} | {A and B and D} | {A and (B or C) or (A and B and D)}")