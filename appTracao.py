import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Analisador de Dados - Excel e CSV", layout="centered")

# Título da aplicação
st.title("📊 Ensaios de Tração")

# Upload do arquivo
arquivo = st.file_uploader("Selecione um arquivo Excel ou CSV", type=["xlsx", "xls", "csv"])

if arquivo:
    try:
        colunas = st.text_input("Colunas a serem carregadas (usecols)", value="mm, kN")

        # Verificar a extensão do arquivo
        if arquivo.name.endswith('.csv'):
            df = pd.read_csv(arquivo, delimiter=';', skiprows=2, usecols=lambda x: x in colunas.split(', '))
        else:
            # Obtendo os nomes das planilhas
            xls = pd.ExcelFile(arquivo, engine='openpyxl')
            planilhas = xls.sheet_names
            # Se houver mais de uma aba, permitir seleção
            aba_selecionada = st.selectbox("Selecione a aba:", planilhas)

            # Carregando dados da aba selecionada
            df = pd.read_excel(xls, sheet_name=aba_selecionada, skiprows=2, usecols=lambda x: x in colunas.split(', '))

        # Exibir as primeiras linhas do DataFrame
        st.subheader("📋 Dados Carregados")
        st.dataframe(df.head())

        # Definir colunas para os eixos X e Y
        col_x = "mm"
        col_y = "kN"

        # Criar gráfico interativo
        st.subheader("📈 Gráfico de Dados")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df[col_x], df[col_y], marker='o', linestyle='-', color='b', label=f'{col_x} x {col_y}')

        # Configuração do gráfico
        ax.set_xlabel(col_x)
        ax.set_ylabel(col_y)
        ax.set_title(f'Gráfico de {col_x} x {col_y}')
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.7)

        # Exibir gráfico no Streamlit
        st.pyplot(fig)

       
        L0 = st.number_input("Insira o valor de L0 da amostra", format="%.2f")
        area = st.number_input("Insira a área da amostra em mm²",format="%.2f")

     
        # Calcular os novos eixos
        df['Deformacao'] = (df['mm'] / L0) * 100
        df['Tensao'] = df['kN'] * 1000 / area
        
        
        # Exibir o DataFrame atualizado
        st.subheader("📋 Dados Atualizados com Deformação e Tensão")
        st.dataframe(df)


        # Criar gráfico de tensão por deformação
        st.subheader("📈 Gráfico de Tensão por Deformação")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df['Deformacao'], df['Tensao'], marker='o', linestyle='-', color='r', label='TensãoxDeformação')

        # Configuração do gráfico
        ax.set_xlabel('Deformação (%)')
        ax.set_ylabel('Tensão (MPa)')
        ax.set_title('Gráfico de Tensão x Deformação')
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.7)

        # Exibir gráfico no Streamlit
        st.pyplot(fig)
 
    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")

