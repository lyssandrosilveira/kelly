import streamlit as st

def kelly_criterion(probabilidade, odd, stake):
    p = probabilidade / 100
    q = 1 - p
    b = odd - 1

    kelly_fraction = (b * p - q) / b

    if kelly_fraction < 0:
        kelly_fraction = 0

    valor_apostado = kelly_fraction * stake

    return kelly_fraction, valor_apostado

# Interface do Streamlit
st.title("Quanto devo apostar?")

# Entrada dos dados
probabilidade = st.number_input("Digite a probabilidade de vitória em %:", min_value=0.0, max_value=100.0, step=0.1)
odd = st.number_input("Digite a odd decimal:", min_value=1.0)
stake = st.number_input("Digite o valor da sua stake:", min_value=0.0)

# Cálculo do Critério Kelly
if st.button("Calcular"):
    kelly_fraction, valor_apostado = kelly_criterion(probabilidade, odd, stake)
    
    # Saída do resultado
    st.write("Porcentagem da stake a ser apostada: {:.2f}%".format(kelly_fraction * 100))
    st.write("Valor em reais a ser apostado: R$ {:.2f}".format(valor_apostado))
