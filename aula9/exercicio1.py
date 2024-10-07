def calcularMedia(n1,n2):
    media = (n1 + n2)/2 
    return media

def imprimirAlunos(alunos):
    for aluno in alunos:
        print (aluno['nome'],'(média:', aluno ['media'],'-',aluno['resutado'],')')

def lervalor(mensagem):
    valorlido=input (mensagem)
    return valorlido
    

resposta=int(input('quantos alunos para calcular?'))

i=0
alunos = []

while i < resposta:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Primeira nota tirada: "))
    nota2 = float(input("Segunda nota tirada: "))
    media = (nota1 + nota2)/2
    resultado = "Aprovado" if media >= 6.5 else "reprovado"
    alunos.append({
         'nome': nome,
         'nota1': nota1,
         'nota2': nota2,
         'media': media,
         'resultado': resultado
    }
    )
    i=i+1



imprimirAlunos(alunos)