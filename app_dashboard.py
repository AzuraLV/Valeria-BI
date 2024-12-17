from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd

df = pd.read_csv(r'C:\Users\annab\OneDrive\Documentos\GitHub\Valeria-BI\bases\ecommerce_dataset_updated.csv')

app = Dash()

app.layout = html.Div(
    style={
        'textAlign': 'center',  # Centraliza o conteúdo
        'margin': '0 auto',  # Ajusta as margens
        'padding': '20px',  # Adiciona espaçamento interno
        'fontFamily': 'Arial, sans-serif',  # Define a fonte
        'backgroundColor': '#f0f2f5'  # Cor de fundo
    },
    children=[
        html.H1("Bem-vindo ao meu App Dash!", style={'color': '#333'}),
        html.P("Este é um layout HTML básico usando o Dash 🚀", style={'color': '#555'}),
        html.Ul([
            html.Li("Item 1: Personalize o conteúdo facilmente."),
            html.Li("Item 2: Adicione estilos e funcionalidades."),
            html.Li("Item 3: Deixe sua imaginação fluir! 🎨"),
        ]),
        html.A("Clique aqui para saber mais", href="https://dash.plotly.com", target="_blank",
               style={'color': 'blue', 'textDecoration': 'none'})
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
