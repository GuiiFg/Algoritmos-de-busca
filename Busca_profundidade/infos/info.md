# Busca em profundidade

Uma arvore não binaria onde serão inseridos elementos um a um de a acordo com suas fronteira seguindo algumas regras.
A partir de um ponto de inicio até um ponto de destino, os nós podem ser considerados estados. a busca em largura garante 
algumas coisas:

 - Um resultado, caso ele exista.
 - Um resultudado, não o melhor possivel, talvez não o pior.

A grande diferença entre a largura e profundidade, é que a largura expande os nos com os menores niveis possiveis,
já a prfundidade da preferencia a os nos que estão em camadas mais baixas da arvore! Em codigo não existe diferença
a não ser na seleção do no para expanção, "Busca_profundidade\struct.py" line 91


## Listas
 - Fronteira(Para onde pode ser expandido)
 - Fechada(lugares que já foram expandido)
 - Solução
