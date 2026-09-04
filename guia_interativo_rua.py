import streamlit as st
import pandas as pd

# Configurações de página para emular uma tela de celular (Pocket/Bolso)
st.set_page_config(
    page_title="Guia de Apoio de Bolso DF",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Estilização CSS personalizada para dar um acabamento moderno de aplicativo móvel
st.markdown("""
<style>
    /* Estilos globais */
    .stApp {
        background-color: #F8F9FA;
        color: #333333;
    }
    
    /* Cabeçalhos e títulos */
    h1, h2, h3 {
        color: #2E5A44 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Customização dos botões e guias */
    .stButton>button {
        background-color: #2E5A44;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1F3F2E;
        color: white;
    }
    
    /* Box do painel de bolso */
    .pocket-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #2E5A44;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 15px;
    }
    
    /* Box para telefones úteis */
    .phone-card {
        background-color: #EBF3EC;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #C3E2CD;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .phone-number {
        font-weight: bold;
        color: #1F3F2E;
        font-size: 1.1em;
    }
    
    /* Selo de Garantia Legal */
    .legal-seal {
        background-color: #D4EDDA;
        color: #155724;
        padding: 10px 15px;
        border-radius: 8px;
        border: 1px solid #C3E6CB;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO DO APP ---
st.write("### 📱 GUIA DE APOIO DE BOLSO")
st.title("Serviços do GDF para Pessoas em Situação de Rua")

# Selo de Garantia Legal (Lei 7.923/2026)
st.markdown(
    '<div class="legal-seal">🛡️ Seus direitos estão garantidos por Lei! '
    'Nova Lei Distrital nº 7.923, de 17 de julho de 2026.</div>',
    unsafe_allow_html=True
)

# --- NAVEGAÇÃO POR ABAS (EMULANDO O MODELO SANFONA) ---
# Separamos o conteúdo do folheto em 6 abas que correspondem aos 6 painéis originais
tabs = st.tabs([
    "🏠 Capa", 
    "🍽️ Alimentação", 
    "🏥 Saúde & Mulher", 
    "📍 Centros Pop", 
    "💼 Trabalho & Auxílios", 
    "📞 Apoio & Contatos"
])

# --- ABA 1: CAPA ---
with tabs[0]:
    st.image("https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&q=80&w=400", use_container_width=True, caption="DF Apoio e Direitos")
    st.markdown(
        """
        <div class="pocket-card">
            <h4><b>Você não está sozinho(a).</b></h4>
            <p>Este guia foi feito para ser leve, rápido e fácil de usar no celular.</p>
            <p>Aqui você encontra apoio para conseguir <b>comida gratuita, banho, atendimento médico, documentos, abrigos e vagas de emprego</b> perto de você no Distrito Federal.</p>
            <p style="color: #666; font-size: 0.9em;"><i>Arraste ou clique nas abas acima para navegar pelas seções do guia rápido.</i></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- ABA 2: ALIMENTAÇÃO ---
with tabs[1]:
    st.markdown("### 🍽️ Refeições Gratuitas e Comida de Graça")
    st.write(
        "A nova lei garante o acesso à alimentação sem barreiras. "
        "Se você estiver sem documento, a equipe do restaurante ou do Centro Pop ajuda você na hora."
    )
    
    # Busca e filtro interativo de Restaurantes Comunitários
    st.markdown("#### 🔍 Encontre um Restaurante Comunitário")
    
    filtro_dia = st.selectbox(
        "Filtrar por dias de funcionamento:",
        ["Todos", "Domingo a Domingo (Todos os dias)", "Segunda a Sábado"]
    )
    
    # Dados estruturados dos restaurantes conforme o folheto revisado
    restaurantes_data = [
        {"Região": "Arniqueira", "Funcionamento": "Domingo a Domingo", "Refeições": "Café, Almoço e Jantar", "Endereço": "QS 9, Avenida Águas Claras, Lote 3"},
        {"Região": "Itapoã", "Funcionamento": "Domingo a Domingo", "Refeições": "Café, Almoço e Jantar", "Endereço": "Quadra 61, Área Especial (Entre Conjuntos D/E)"},
        {"Região": "Planaltina", "Funcionamento": "Domingo a Domingo", "Refeições": "Café, Almoço e Jantar", "Endereço": "Quadra 2, Lote A, Feira Livre"},
        {"Região": "Recanto das Emas", "Funcionamento": "Domingo a Domingo", "Refeições": "Café, Almoço e Jantar", "Endereço": "Avenida Recanto das Emas, Quadra 205, Lote 01"},
        {"Região": "Sol Nascente", "Funcionamento": "Domingo a Domingo", "Refeições": "Café, Almoço e Jantar", "Endereço": "QNR 1, Área Especial 2"},
        {"Região": "Pôr do Sol", "Funcionamento": "Domingo a Domingo", "Refeições": "Café, Almoço e Jantar", "Endereço": "Quadra 105, Conjunto O, Área Especial 1 (Trecho 2)"},
        {"Região": "Brazlândia", "Funcionamento": "Segunda a Sábado", "Refeições": "Café e Almoço", "Endereço": "Quadra 36, Área Especial nº 01"},
        {"Região": "Ceilândia", "Funcionamento": "Segunda a Sábado", "Refeições": "Café e Almoço", "Endereço": "QNM 1, Bloco 1, Lote 1"},
        {"Região": "Estrutural (Brasília)", "Funcionamento": "Segunda a Sábado", "Refeições": "Café e Almoço", "Endereço": "Quadra 14, Área Especial"},
        {"Região": "Paranoá", "Funcionamento": "Segunda a Sábado", "Refeições": "Café e Almoço", "Endereço": "Quadra 2, Área Especial, Lote A"},
        {"Região": "Samambaia", "Funcionamento": "Segunda a Sábado", "Refeições": "Café e Almoço", "Endereço": "ADE, Conjunto 15, Lotes 01/02 (BR-060)"},
        {"Região": "São Sebastião", "Funcionamento": "Segunda a Sábado", "Refeições": "Café e Almoço", "Endereço": "CMA, Área Especial 02"},
        {"Região": "Gama", "Funcionamento": "Segunda a Sábado", "Refeições": "Apenas Almoço", "Endereço": "Área Especial 1, Complexo Esportivo (Estádio Bezerrão)"},
        {"Região": "Santa Maria", "Funcionamento": "Segunda a Sábado", "Refeições": "Apenas Almoço", "Endereço": "Av. Alagados, Área Central"},
        {"Região": "Riacho Fundo II", "Funcionamento": "Segunda a Sábado", "Refeições": "Apenas Almoço", "Endereço": "Quadra 10, Conjunto 01, Lote 01"},
    ]
    
    df_restaurantes = pd.DataFrame(restaurantes_data)
    
    if filtro_dia == "Domingo a Domingo (Todos os dias)":
        df_filtrado = df_restaurantes[df_restaurantes["Funcionamento"] == "Domingo a Domingo"]
    elif filtro_dia == "Segunda a Sábado":
        df_filtrado = df_restaurantes[df_restaurantes["Funcionamento"] == "Segunda a Sábado"]
    else:
        df_filtrado = df_restaurantes
        
    for index, row in df_filtrado.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="pocket-card">
                <b>📍 {row['Região']}</b><br>
                🟢 <b>Funcionamento:</b> {row['Funcionamento']}<br>
                🍽️ <b>Refeições:</b> {row['Refeições']}<br>
                🏠 <b>Endereço:</b> {row['Endereço']}
            </div>
            """, unsafe_allow_html=True)

# --- ABA 3: SAÚDE & MULHER ---
with tabs[2]:
    st.markdown("### 🏥 Saúde, Cuidado e Acolhimento")
    st.write(
        "A saúde é um direito sagrado. De acordo com o Art. 5º da nova lei, "
        "**nenhum hospital ou postinho (UBS) pode recusar atendimento por falta de documentos ou comprovante de endereço.**"
    )
    
    # Interatividade: Simule um teste de elegibilidade a direitos
    st.markdown("#### 🛡️ Guia Rápido de Direitos")
    opcao_direito = st.selectbox(
        "Selecione uma situação para ver seus direitos garantidos por lei:",
        [
            "Preciso de atendimento médico e estou sem meus documentos",
            "Sou mulher e quero saber sobre a minha segurança nos abrigos",
            "Preciso de ajuda com problemas de álcool, drogas ou saúde mental",
            "Tenho filhos pequenos e preciso de acolhimento"
        ]
    )
    
    if opcao_direito == "Preciso de atendimento médico e estou sem meus documentos":
        st.success(
            "**Seu Direito Garantido:** Você tem o direito legal de ser atendido em qualquer hospital, "
            "UPA ou UBS (Postinho) sem apresentar RG, CPF ou comprovante de moradia. "
            "O governo é obrigado a registrar você usando meios alternativos de identificação que preservem sua dignidade."
        )
    elif opcao_direito == "Sou mulher e quero saber sobre a minha segurança nos abrigos":
        st.success(
            "**Seu Direito Garantido:** Por lei (Art. 17, § 4º), todas as unidades de acolhimento (abrigos) "
            "do DF são obrigadas a possuir **alas ou espaços exclusivos para mulheres**, garantindo sua privacidade, "
            "segurança e total proteção contra qualquer tipo de violência."
        )
    elif opcao_direito == "Preciso de ajuda com problemas de álcool, drogas ou saúde mental":
        st.success(
            "**Seu Direito Garantido:** Você pode procurar qualquer CAPS (Centro de Atenção Psicossocial) "
            "da rede de saúde. O atendimento é por demanda espontânea (não precisa marcar hora). "
            "A nova lei distrital também proíbe o recolhimento forçado nas ruas e assegura tratamento humanizado."
        )
    elif opcao_direito == "Tenho filhos pequenos e preciso de acolhimento":
        st.success(
            "**Seu Direito Garantido:** É garantido por lei o acolhimento conjunto de mães com seus filhos "
            "e dependentes em situação de vulnerabilidade, impedindo a separação compulsória da família."
        )

# --- ABA 4: CENTROS POP ---
with tabs[3]:
    st.markdown("### 📍 Centros Pop (Seus Pontos de Apoio)")
    st.write(
        "Os Centros Pop são espaços públicos abertos onde você pode passar o dia, "
        "fazer refeições, tomar banho, lavar suas roupas e guardar suas coisas de graça."
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="pocket-card" style="height: 100%;">
            <b>📍 Centro Pop Asa Sul</b><br>
            🏠 SGAS 903, Conjunto C — Plano Piloto<br>
            📞 3773-7561 / 7562 / 7563<br>
            ⏰ 7h30 às 17h, todos os dias (inclusive feriados)
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="pocket-card" style="height: 100%;">
            <b>📍 Centro Pop Taguatinga</b><br>
            🏠 QNF 24, A/E nº 2, Mód. A — Taguatinga Norte<br>
            📞 3773-7556 / 7557<br>
            ⏰ 7h30 às 18h, todos os dias (inclusive feriados)
        </div>
        """, unsafe_allow_html=True)
        
    st.info("💡 **Dica importante:** Seu animal de estimação é super bem-vindo nos Centros Pop do DF!")

# --- ABA 5: TRABALHO & AUXÍLIOS ---
with tabs[4]:
    st.markdown("### 💼 Capacitação, Trabalho e Renda")
    st.write(
        "Aproveite as oportunidades e cursos gratuitos que oferecem auxílio financeiro e transporte:"
    )
    
    # Accordion interativo de Programas
    with st.expander("🛠️ RENOVA DF (Curso prático de 3 meses)"):
        st.markdown("""
**O que ensina:** Construção civil e jardinagem (com consertos de praças públicas).

**Benefícios:**
* Bolsa de **1 salário mínimo nacional por mês**
* Auxílio-transporte e lanche diário
* Diploma e kit estudante completo (uniforme, botas e equipamentos)
* **Vagas exclusivas reservadas para quem está na rua.**
        """)
        
    with st.expander("🎓 QUALIFICA DF (50 cursos profissionais rápidos)"):
        st.markdown("""
**Cursos como:** Auxiliar administrativo, eletricista, mecânica de motos, manicure, maquiagem e cuidador de idosos.

**Benefícios:**
* Vale-transporte de graça e lanches diários
* Uniforme e material de estudo completo
* Diploma reconhecido.
* *Pode usar o endereço do Centro Pop como comprovante de residência.*
        """)
        
    with st.expander("🚌 Passagem de Graça para Volta para Casa"):
        st.markdown("""
**Como funciona:** Se você deseja voltar para seu estado ou cidade de origem, e possui familiares ou apoios esperando por você lá, o governo do DF pode pagar a sua **passagem interestadual de ônibus**.

**Onde solicitar:** Procure a assistência social do Centro Pop ou do CREAS para que eles comprovem a rede de apoio e emitam a passagem.
        """)

# --- ABA 6: PROTOCOLOS & CONTATOS ---
with tabs[5]:
    st.markdown("### 📞 Telefones e Apoio de Emergência")
    st.write("Clique ou salve os números abaixo em caso de necessidade de apoio ou urgências:")
    
    contatos = [
        {"Nome": "🚑 Emergência Médica (SAMU)", "Numero": "192"},
        {"Nome": "⚖️ Defensoria Pública do DF (Justiça de graça)", "Numero": "129"},
        {"Nome": "🤝 Abordagem Social de Rua (SEAS)", "Numero": "(61) 3322-1441"},
        {"Nome": "🏢 Assistência Social / Serviços Rua (Central Sedes)", "Numero": "156 (Opção 1, depois 1)"},
        {"Nome": "🛡️ Disque Direitos Humanos", "Numero": "100"},
        {"Nome": "👩 Central de Atendimento à Mulher", "Numero": "180"},
        {"Nome": "🚒 Bombeiros / Primeiros Socorros", "Numero": "193"},
        {"Nome": "👶 Violência contra Criança/Adolescente", "Numero": "125"}
    ]
    
    for contato in contatos:
        st.markdown(f"""
        <div class="phone-card">
            <span>{contato['Nome']}</span>
            <span class="phone-number">📞 {contato['Numero']}</span>
        </div>
        """, unsafe_allow_html=True)

# Rodapé institucional do app
st.markdown("---")
st.caption(
    "Guia de Bolso Interativo • Desenvolvido em conformidade com a Lei Distrital nº 7.923/2026. "
    "Dados integrados das Secretarias de Saúde (SES) e Desenvolvimento Social (Sedes) do Distrito Federal."
)
