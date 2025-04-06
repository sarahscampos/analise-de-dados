import sys

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


if __name__ == "__main__":
    terminal_tem_cenoura = sys.argv[1] == "Sim"
    terminal_tem_oleo = sys.argv[2] == "Sim"
    terminal_tem_fermento = sys.argv[3] == "Sim"
    terminal_tem_leite = sys.argv[4] == "Sim"
    terminal_tem_acucar = sys.argv[5] == "Sim"
    terminal_tem_ovos = sys.argv[6] == "Sim"

    total = soma_preco(terminal_tem_cenoura, terminal_tem_oleo, terminal_tem_fermento, terminal_tem_leite, terminal_tem_acucar, terminal_tem_ovos)

    print("O total da receita é: R$ ", total)