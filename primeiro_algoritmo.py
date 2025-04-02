preco_cenoura = 4.5
preco_oleo = 10
preco_fermento = 7.9 
preco_leite = 14.5
preco_acucar = 9.9
preco_ovos = 11

def soma_preco(tem_cenoura, tem_oleo, tem_fermento, tem_leite, tem_acucar, tem_ovos):
    total = 0
    if tem_cenoura:
        total = total + preco_cenoura
    if tem_oleo:
        total = total + preco_oleo
    if tem_fermento:
        total = total + preco_fermento
    if tem_leite:
        total = total + preco_leite
    if tem_acucar:
        total = total + preco_acucar
    if tem_ovos:
        total = total + preco_ovos

    return total

total = soma_preco(True, True, True, True, True, True)

print(total)
    