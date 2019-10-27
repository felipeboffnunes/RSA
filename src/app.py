from .components import rsa

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

app.layout = html.Div(

    children=[
        html.H1(children='RSA'),

        html.Div(children=[
            html.Button('Ascii Message', id='ascii-button'),
            dcc.Textarea(
                id='input-area',
                placeholder='',
                value='Message here'
            ),
            
            html.H4('Int Ascii Message:'),
            html.Div(id='ascii-output', children='10'),
        ]),

        

        html.Button('Private Key', id='private-key-button'),
        dcc.Input(
            id='private-bits-input',
            type='number',
            value=10
        ),
        html.H4('Private Key:'),
        html.Div(id='private-key-output', children='10'),

        html.Button('Public Key', id='public-key-button'),
        dcc.Input(
            id='public-bits-input',
            type='number',
            value=10
        ),
        html.H4('Public Key:'),
        html.Div(id='public-key-output', children='10'),
        html.Button('Get n', id='n-button'),
        html.H4('N:'),
        html.Div(id='n-output', children='100'),
        html.Button('Get totient', id='totient-button'),
        html.H4('Totient:'),
        html.Div(id='totient-output', children='100'),
        html.Button('Find coprime', id='coprime-button'),
        html.H4('Coprime:'),
        html.Div(id='coprime-output', children='100'),
        html.Button('Find d', id='d-button'),
        html.H4('d:'),
        html.Div(id='d-output', children='100'),
        html.Button('Encrypt message', id='encrypt-button'),
        html.H4('Encrypted message:'),
        html.Div(id='encrypt-output', children='100'),
        html.Button('Decrypt message', id='decrypt-button'),
        html.H4('Decrypted message:'),
        html.Div(id='decrypt-output', children='100'),
        html.Button('Convert message to string', id='message-button'),
        html.H4('Original message:'),
        html.Div(id='message-output', children='aaa'),

    ])


@app.callback(
    Output('private-key-output', 'children'),
    [Input('private-key-button', 'n_clicks')],
    [State('private-bits-input', 'value')],
)
def get_private_key(n_clicks, value):
    private_key = rsa.find_prime(int(value))
    return f'{private_key}'


@app.callback(
    Output('public-key-output', 'children'),
    [Input('public-key-button', 'n_clicks')],
    [State('public-bits-input', 'value')],
)
def get_public_key(n_clicks, value):
    public_key = rsa.find_prime(int(value))
    return f'{public_key}'


@app.callback(
    Output('totient-output', 'children'),
    [Input('totient-button', 'n_clicks')],
    [State('private-key-output', 'children'),
     State('public-key-output', 'children')],
)
def get_totient(n_clicks, value1, value2):
    totient = rsa.get_totient(int(value1), int(value2))
    return f'{totient}'


@app.callback(
    Output('coprime-output', 'children'),
    [Input('coprime-button', 'n_clicks')],
    [State('totient-output', 'children')],
)
def get_coprime(n_clicks, value):
    coprime = rsa.find_coprime(int(value))
    return f'{coprime}'


@app.callback(
    Output('d-output', 'children'),
    [Input('d-button', 'n_clicks')],
    [State('totient-output', 'children'),
     State('coprime-output', 'children')],
)
def get_d(n_clicks, value1, value2):
    if int(value1) == 100:
        return '100'
    d = rsa.find_d(int(value1), int(value2))
    return f'{d}'


@app.callback(
    Output('encrypt-output', 'children'),
    [Input('encrypt-button', 'n_clicks')],
    [State('ascii-output', 'children'),
     State('coprime-output', 'children'),
     State('n-output', 'children')],
)
def encrypt(n_clicks, value1, value2, value3):
    encrypted_message = rsa.encrypt(int(value1), int(value2), int(value3))
    return f'{encrypted_message}'


@app.callback(
    Output('n-output', 'children'),
    [Input('n-button', 'n_clicks')],
    [State('private-key-output', 'children'),
     State('public-key-output', 'children')],
)
def get_n(n_clicks, value1, value2):
    n = rsa.get_n(int(value1), int(value2))
    return f'{n}'


@app.callback(
    Output('decrypt-output', 'children'),
    [Input('decrypt-button', 'n_clicks')],
    [State('encrypt-output', 'children'),
     State('d-output', 'children'),
     State('n-output', 'children')],
)
def decrypt(n_clicks, value1, value2, value3):
    decrypted_message = rsa.decrypt(int(value1), int(value2), int(value3))
    return f'{decrypted_message}'

@app.callback(
    Output('ascii-output', 'children'),
    [Input('ascii-button', 'n_clicks')],
    [State('input-area', 'value')],
)
def get_ascii(n_clicks, value):
    ascii_message = rsa.str_to_ascii(value) 
    return f'{ascii_message}'


@app.callback(
    Output('message-output', 'children'),
    [Input('message-button', 'n_clicks')],
    [State('decrypt-output', 'children')],
)
def convert_message(n_clicks, value):
    original_message = rsa.ascii_to_str(str(value))
    return f'{original_message}'



def start():
    app.run_server(debug=True)
