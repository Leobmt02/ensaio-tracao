# Analisador de Dados de Ensaios de Tração (Excel/CSV)

Este é um aplicativo Streamlit que permite aos usuários carregar arquivos Excel (.xlsx, .xls) ou CSV para analisar dados de ensaios de tração. Ele oferece as seguintes funcionalidades:

-   **Upload de Arquivo:** Permite selecionar arquivos Excel ou CSV diretamente do seu computador.
-   **Seleção de Colunas:** Você pode especificar quais colunas do seu arquivo deseja carregar, útil para focar nos dados relevantes (por padrão, carrega colunas com os nomes "mm" e "kN").
-   **Seleção de Aba (Excel):** Se o arquivo Excel contiver múltiplas planilhas, o aplicativo permite que você selecione qual aba deseja analisar.
-   **Visualização de Dados:** Exibe as primeiras linhas dos dados carregados em um formato de tabela para inspeção rápida.
-   **Gráfico Interativo:** Plota um gráfico dos dados carregados (por padrão, "mm" no eixo X e "kN" no eixo Y), permitindo uma visualização inicial do comportamento dos dados.
-   **Cálculo de Deformação e Tensão:** Permite inserir o valor de $L_0$ (comprimento inicial) da amostra e a área da seção transversal para calcular e exibir novas colunas de "Deformação (%)" e "Tensão (MPa)". As fórmulas utilizadas são:
    $$\text{Deformação (%) } = \left( \frac{\text{mm}}{L_0} \right) \times 100$$
    $$\text{Tensão (MPa)} = \frac{\text{kN} \times 1000}{\text{Área}}$$
-   **Gráfico de Tensão por Deformação:** Gera um gráfico da tensão (MPa) em função da deformação (%), fundamental para analisar as propriedades mecânicas do material testado.

## Como Usar

1.  **Faça o Upload do Arquivo:** Clique no botão "Selecione um arquivo Excel ou CSV" e escolha o arquivo contendo os dados do seu ensaio de tração.
2.  **Especifique as Colunas (Opcional):** Se as colunas de deslocamento e força no seu arquivo tiverem nomes diferentes de "mm" e "kN", insira os nomes corretos no campo "Colunas a serem carregadas (usecols)", separados por vírgula. Por exemplo: `deslocamento, forca`.
3.  **Selecione a Aba (Apenas para Excel):** Se o arquivo Excel tiver várias abas, escolha a aba que contém os dados desejados no menu suspenso "Selecione a aba:". Os nomes das abas disponíveis serão listados.
4.  **Visualize os Dados:** As primeiras linhas dos dados carregados serão exibidas em uma tabela usando `st.dataframe(df.head())`.
5.  **Analise o Gráfico Inicial:** Um gráfico de dispersão com linhas conectando os pontos será mostrado, com a primeira coluna especificada no eixo X (rótulo "mm") e a segunda coluna especificada no eixo Y (rótulo "kN"). O título do gráfico será "Gráfico de mm x kN". Uma legenda identificará a curva como "mm x kN", e uma grade de fundo será exibida para facilitar a leitura dos valores.
6.  **Insira $L_0$ e Área:** Digite o valor do comprimento inicial ($L_0$) da amostra no campo "Insira o valor de L0 da amostra" e a área da seção transversal em $mm^2$ no campo "Insira a área da amostra em mm²". Certifique-se de usar o formato numérico correto (por exemplo, `10.50` para dez e cinquenta).
7.  **Visualize os Dados Atualizados:** Uma nova tabela será exibida mostrando o DataFrame original acrescido de duas novas colunas: "Deformacao (%)" e "Tensao (MPa)", calculadas com base nos valores de $L_0$ e área fornecidos.
8.  **Analise o Gráfico de Tensão por Deformação:** Um gráfico de dispersão com linhas conectando os pontos será gerado, com a coluna "Deformacao (%)" no eixo X (rótulo "Deformação (%)") e a coluna "Tensao (MPa)" no eixo Y (rótulo "Tensão (MPa)"). O título do gráfico será "Gráfico de Tensão x Deformação", com uma legenda identificando a curva como "TensãoxDeformação" e uma grade de fundo.
9.  **Erros:** Se houver algum problema ao processar o arquivo (por exemplo, arquivo não encontrado, formato incorreto, colunas não existentes), uma mensagem de erro será exibida na tela usando `st.error()`, detalhando a exceção ocorrida.

## Dependências

Este aplicativo foi desenvolvido usando as seguintes bibliotecas Python:

-   **streamlit** (`import streamlit as st`): Para criar a interface web interativa e os elementos visuais.
-   **pandas** (`import pandas as pd`): Para manipulação e análise de dados tabulares (DataFrames), leitura de arquivos CSV e Excel.
-   **matplotlib.pyplot** (`import matplotlib.pyplot as plt`): Para geração de gráficos estáticos que são exibidos no Streamlit via `st.pyplot()`.
-   **openpyxl**: Necessário para ler arquivos Excel com extensão `.xlsx`. Geralmente instalado como uma dependência do pandas ao lidar com arquivos Excel.

Certifique-se de ter essas bibliotecas instaladas em seu ambiente Python para executar o aplicativo. Você pode instalá-las usando o pip:

```bash
pip install streamlit pandas matplotlib openpyxl
