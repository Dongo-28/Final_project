# 📝 README Completo - Análise de Mudanças Climáticas

##🌡️ Relatório Integrado

##📊 Resultados Chave
Tendência de Aquecimento Global

Aumento médio: +0.18°C/década (1880-2023)

2023 foi o ano mais quente (+1.02°C acima da média)


Elevação do Nível do Mar

Modelo de regressão linear: 3.78 mm/ano

Precisão: RMSE = 4.92 mm, R² = 0.979


Correlação Estatística

Pearson: r = 0.98 (p < 0.001)

Teste ANOVA: Diferenças significativas entre décadas

##🛠️ Como Executar o Projeto

# Clone o repositório
git clone https://github.com/Dongo-28/Final_project.git

# Instale as dependências
pip install -r requirements.txt

# Execute os notebooks na ordem:
jupyter notebook notebooks/1_eda_preprocessing.ipynb
jupyter notebook notebooks/2_statistical_analysis.ipynb
jupyter notebook notebooks/3_machine_learning.ipynb

##📂 Estrutura do Projeto
Final_project/

├── data/

│   ├── global_temperature.csv

│   ├── sea_level.csv

│   └── sea_surface_temperature.csv

├── notebooks/

│   ├── 1_eda_preprocessing.ipynb

│   ├── 2_statistical_analysis.ipynb

│   └── 3_machine_learning.ipynb

├── reports/

│   ├── temp_trend.png

│   └── regressao_linear.png

└── docs/

    └── literature_review.md

##📈 Métodos Utilizados
Pré-processamento

Tratamento de valores ausentes

Normalização de dados

Análise Estatística

Correlação de Pearson

Teste ANOVA

Machine Learning

Regressão Linear

Métricas: RMSE e R²

##💡 Conclusões
Confirmação do aquecimento global acelerado

Relação direta entre temperatura e nível do mar

Modelo preciso para projeções futuras

##📚 Referências
IPCC (2023). AR6 Climate Change Report

NASA GISS (2024). Global Temperature Data

NOAA (2023). Sea Level Rise Technical Report

##👥 Como Contribuir
Faça um fork do projeto

Crie sua branch (git checkout -b feature/nova-analise)

Commit suas mudanças (git commit -m 'Adiciona nova análise')

Push para a branch (git push origin feature/nova-analise)

Abra um Pull Request
