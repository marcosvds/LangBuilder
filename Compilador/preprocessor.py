import re

class PrePro:
    @staticmethod
    def filter(codigo):
        """
        Remove comentários do código-fonte da linguagem LangBuilder e linhas vazias resultantes.

        Esta função processa o código-fonte, identificando e removendo comentários e linhas vazias.
        Comentários são iniciados com '//' para uma linha e '/*' até '*/' para múltiplas linhas.
        Este método utiliza expressões regulares para remover ambos os tipos de comentários e linhas vazias,
        tornando-o adequado para arquivos de código-fonte completos.

        Parâmetros:
            codigo (str): O código-fonte a ser pré-processado.

        Retorna:
            str: O código-fonte com os comentários e linhas vazias removidos.
        """
        # Remove comentários de linha
        codigo = re.sub(r'//.*', '', codigo)
        # Remove comentários de bloco
        codigo = re.sub(r'/\*.*?\*/', '', codigo, flags=re.DOTALL)
        # Remove linhas vazias ou que contenham apenas espaços em branco
        codigo = re.sub(r'^\s*\n', '', codigo, flags=re.MULTILINE)
        # Remove quebras de linha e ponto e vírgula
        codigo = codigo.replace("\n", " ").replace(";", "")
        
        # Print de depuração
        #print("Código após pré-processamento:")
        #print(codigo)
        
        return codigo.strip()
