
import streamlit as st

# Configuração da página
st.set_page_config(page_icon="🍔", page_title="Lanchonete")

# Título do sistema
st.title("🍔 Caixa da Lanchonete")

# Lista de produtos e seus preços
cardapio = {
    "Coxinha": 6.00,
    "Risole": 7.00,
    "Coca lata 350 ml": 3.50,
    "Pastel": 8.00,
    "Empada": 6.50,
    "Pão de queijo": 4.00,
    "Hambúrguer": 15.00,
    "X-Burguer": 18.00,
    "Hot Dog": 12.00,
    "Batata frita": 10.00,
    "Suco natural": 7.00,
    "Água mineral": 3.00,
    "Brigadeiro": 3.00,
    "Bolo de chocolate": 6.00
}

# Permite escolher um produto do cardápio
produto = st.selectbox("Escolha um produto:", cardapio)

# Permite informar a quantidade
quantidade = st.number_input("Quantidade:", min_value=1, step=1)

# Busca o preço do produto escolhido
preco = cardapio[produto]

# Calcula o valor total do produto
total = preco * quantidade

# Mostra as informações do produto
st.text("Produto: " + produto)
st.text(f"Preço: R$ {preco:.2f}")
st.text(f"Quantidade: {quantidade}")
st.text(f"Total: R$ {total:.2f}")

# Cria a lista de compras
if "compras" not in st.session_state:
    st.session_state.compras = []

# Botão para adicionar produto
if st.button("Adicionar produto"):

    # Guarda o produto e a quantidade
    st.session_state.compras.append(
        [produto, quantidade, preco, total]
    )

    st.success("Produto adicionado!")

# Mostra os produtos escolhidos
st.subheader("🛒 Minha compra")

# Calcula o valor da compra
soma = 0

for item in st.session_state.compras:

    st.text(f"{item[0]} - Quantidade: {item[1]}")
    st.text(f"Valor: R$ {item[3]:.2f}")

    soma = soma + item[3]

# Mostra o valor total
st.subheader(f"Total da compra: R$ {soma:.2f}")

# Botão para finalizar a compra
if st.button("Finalizar compra"):

    if len(st.session_state.compras) > 0:

        st.success(f"Compra finalizada! Total: R$ {soma:.2f}")

        st.session_state.compras = []

    else:
        st.warning("Adicione algum produto primeiro!")
