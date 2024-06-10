import sys
from preprocessor import PrePro
from parser_base import Parser
from Compilador.symbol_table import SymbolTable

def executar():
    # Verifica se um arquivo de código-fonte foi fornecido como argumento
    if len(sys.argv) < 2:
        print("Modo de uso: python main.py <arquivo_de_codigo>", file=sys.stderr)
        sys.exit(1)

    # Tenta abrir e ler o arquivo de código-fonte
    nome_arquivo = sys.argv[1]
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo_codigo = arquivo.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.", file=sys.stderr)
        sys.exit(1)

    # Filtra o código-fonte
    codigo_processado = PrePro.filter(conteudo_codigo)

    try:
        # Analisa o código-fonte processado
        analisador_sintatico = Parser(codigo_processado)
        arvore_sintatica = analisador_sintatico.parse()

        # Inicializa a tabela de símbolos e executa o programa
        tabela_de_simbolos = SymbolTable()
        arvore_sintatica.evaluate(tabela_de_simbolos)

        # Imprime a tabela de símbolos resultante
        #print("Tabela de Símbolos:", tabela_de_simbolos.table)
    except Exception as excecao:
        print("Erro durante a execução:", excecao, file=sys.stderr)

if __name__ == "__main__":
    executar()
