def calcularMedia(n1,n2):
    media = (n1 + n2)/2 
    return media

def imprimirAlunos(alunos):
    for aluno in alunos:
        print (aluno['nome'],'(média:', aluno ['media'],'-',aluno['resutado'],')')


    

resposta=int(input('quantos alunos para calcular?'))

i=0

alunos = []

while i < resposta:
    nomeAluno = input('digite o Nome do aluno: ')
    nota1 = float(input('digite a Primeira nota tirada: '))
    nota2 = float(input('digite a Segunda nota tirada: '))
    
    media = calcularMedia(nota1,nota2)

    resultado = "Aprovado" if media >= 6.5 else "reprovado"
    
    alunos.append(
    {
         'nome': nomeAluno,
         'nota1': nota1,
         'nota2': nota2,
         'media': media,
        
        
    }
    )
i=i+1



imprimirAlunos(alunos)