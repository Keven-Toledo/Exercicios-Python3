def notas(* nota, show=False):
    """
    Notas() cria um Dicionário que contém:
    — Total de notas,
    — maior nota,
    — menor nota,
    — média das notas.
        * A situação do aluno é opcional.
    : param *nota: Recebe várias valores
    : param show: (Opcional) mostra a situção
    do aluno.
    """
    total = len(nota)
    maior_nota = max(nota)
    menor_nota = min(nota)
    media_notas = sum(nota) / total
    if media_notas < 6:
        situacao = 'RUIM'
    elif 6 <= media_notas < 8:
        situacao = 'BOA'
    else:
        situacao = 'ÓTIMA'
    info = {
        'Total': total,
        'Maior': maior_nota,
        'Menor': menor_nota,
        'Média': f'{media_notas:.1f}',
    }
    if show:
        info['Situação'] = situacao
    return info


final = notas(10, 6, 8, 8, show=True)
help(notas)
