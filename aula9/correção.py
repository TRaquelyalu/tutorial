def calculamedia(n1,n2):
    media=(n1+n2)/2
    return media
def imprimirAluno(alunos):
    for aluno in alunos:
        print (aluno['nome'],'(média:', aluno ['media'],'-',aluno['resutado'],')')

resposta=int(input('quantos alunos para calcular?'))
i=0
alunos=[]
while i < resposta:
    nomeAluno= input('digite o nome do aluno')
    nota1= float(input('digite a primeira nota'))
    nota2=float(input('digitea segunda nota '))

        