from fpdf import FPDF

# Criando um novo documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Adicionando título
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "LUCAS ROSSINI CURI SILVA", ln=True, align="C")
pdf.ln(5)

# Adicionando informações de contato
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Londrina, PR | lucasrcs91@gmail.com | (43) 9 9846-3901", ln=True, align="C")
pdf.ln(10)

# Objetivo
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Objetivo", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 7, 
                   "Economista com experiência em inteligência de mercado, análise de dados e automação de processos. Experiência prática com ferramentas como Power BI, SQL, Python e técnicas estatísticas avançadas. Alta adaptabilidade, habilidade em diagnóstico empresarial e desenvolvimento de dashboards interativos. Proativo e eficiente na criação de soluções baseadas em dados.")
pdf.ln(5)

# Formação Acadêmica
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Formação Acadêmica", ln=True)
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 7, "Ciências Econômicas - Universidade Estadual de Londrina (2016 - 2020)", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 7, "Destaques: Láurea Acadêmica", ln=True)
pdf.ln(3)
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 7, "Pós-graduação em Machine Learning e Big Data - UEL (Interrompido)", ln=True)
pdf.ln(5)

# Habilidades Técnicas
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Habilidades Técnicas", ln=True)
pdf.set_font("Arial", size=12)
skills_fixed = [
    "Linguagens de Programação: Python (Pandas, NumPy), R, SQL",
    "Business Intelligence (BI): Power BI, QlikSense, Looker",
    "Banco de Dados: SQL",
    "Análises Estatísticas: Regressões multilineares, modelo log-lin, análise preditiva",
    "Automação de Processos: Python",
    "Metodologias de Trabalho: Kanban, Agile"
]
for skill in skills_fixed:
    pdf.cell(0, 7, f"- {skill}", ln=True)

pdf.ln(5)

# Experiência Profissional
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Experiência Profissional", ln=True)

# Rolemar
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 7, "Rolemar (15/06/2021 - Atualmente)", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 7, "Cargo: Coordenador de Inteligência de Mercado", ln=True)
rolemar_tasks_fixed = [
    "Desenvolvimento de dashboards e KPIs em Power BI para acompanhamento de indicadores",
    "Consultas e manipulação de dados em SQL para análise de pricing e rentabilidade",
    "Aplicação de modelos estatísticos para previsão de demanda e impacto de alterações tributárias",
    "Automação de processos com Python (Pandas, NumPy) para otimizar fluxos de trabalho",
    "Estruturação de ETL para extração e limpeza de grandes volumes de dados"
]
for task in rolemar_tasks_fixed:
    pdf.cell(0, 7, f"- {task}", ln=True)

pdf.ln(3)

# Sebrae
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 7, "Sebrae/PR (13/08/2018 - 29/04/2021)", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 7, "Cargo: Assistente de Inovação Aberta", ln=True)
sebrae_tasks_fixed = [
    "Desenvolvimento de ferramentas de BI utilizando QlikSense para acompanhamento de produtividade",
    "Análises de dados empresariais e estruturação de relatórios gerenciais",
    "Atendimento a empresas para planejamento estratégico baseado em dados"
]
for task in sebrae_tasks_fixed:
    pdf.cell(0, 7, f"- {task}", ln=True)

pdf.ln(3)

# Estágios Extra Curriculares
pdf.set_font("Arial", style='B', size=12)
pdf.cell(0, 7, "Estágios Extra Curriculares", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 7, "- Brisa Casa (2016-2017)", ln=True)
pdf.cell(0, 7, "- MMartan (2017)", ln=True)

pdf.ln(5)

# Idiomas
pdf.set_font("Arial", style='B', size=14)
pdf.cell(0, 10, "Idiomas", ln=True)
pdf.set_font("Arial", size=12)
pdf.cell(0, 7, "- Inglês: Avançado", ln=True)
pdf.cell(0, 7, "- Espanhol: Intermediário", ln=True)
