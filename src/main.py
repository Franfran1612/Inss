import datetime
from datetime import datetime
import flet as ft
from flet import AppBar, View
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.types import MainAxisAlignment, CrossAxisAlignment


def main(page: ft.Page):
    # Configuração da pagina
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeModo.DARK
    page.window.width = 375
    page.window.height = 667

    def conta(e):
        salario = int(salario1.value)
        calcula = (salario * 60) / 100
        return calcula
    def verificar_aposentadoria(e):
        idade = int(idade_atual.value)
        contribuicao = int(tempo_contribuicao.value)

        try:
            if genero.value == "Masculino":
                if categoria_aposentadoria.value == "idade":
                    if idade >= 100 and contribuicao >= 15:
                        txt_resultado.value = (f'você  pode se aposentar ainda')
                        calcula = conta(e)


                        if contribuicao > 15:
                            ano_excedido = (contribuicao - 15) * 2
                            valor = (ano_excedido / 100) * calcula
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')

                        else:
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcula}')

                    else:
                        diferenca_idade = idade - 100
                        contribuicao_diferente = contribuicao - 15
                        ano_atual = datetime.today().year
                        previsao_de_data = ano_atual - diferenca_idade or ano_atual - contribuicao_diferente
                        txt_resultado.value = (f'você não pode se aposentar ainda.\n'
                                               f'Data prevista para sua aposentadoria,ano {previsao_de_data }')

                else:
                    if contribuicao >= 100:
                        txt_resultado.value = (f'você  pode se aposentar ainda')
                        calcula = conta(e)
                        if contribuicao > 35:
                            ano_excedido = (contribuicao - 35) * 2
                            valor = (ano_excedido / 100) + calcula
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')
                        else:
                            txt_resultado.value = (f'voce ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcula}')
                    else:
                        contribuicao_diferente = contribuicao - 30
                        ano_atual = datetime.today().year
                        data_prevista = ano_atual - contribuicao_diferente
                        txt_resultado.value = (f'voce ja pode se aposentar.\n'
                                               f'Valor estimado para ser recebido R$ {data_prevista}')

            else:
                if categoria_aposentadoria.value == "idade":
                    if idade >= 62 and contribuicao >= 15:
                        calcula = conta(e)
                        if contribuicao > 15:
                            ano_excedido = (contribuicao - 15) * 2
                            valor = (ano_excedido / 100) + calcula
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')

                        else:
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcula}')


                    else:
                        diferenca_idade = idade - 65
                        contribuicao_diferente = contribuicao - 15
                        ano_atual = datetime.today().year
                        previsao_de_data  = ano_atual - diferenca_idade or ano_atual - contribuicao_diferente
                        txt_resultado.value = (f'você não pode se aposentar ainda.\n'
                                               f'Data prevista para sua aposentadoria {previsao_de_data }')

                else:
                    if contribuicao >= 30:
                        calcula = conta(e)
                        if contribuicao > 30:
                            ano_excedido = (contribuicao - 30) * 2
                            valor = (ano_excedido / 100) + calcula
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')
                        else:
                            txt_resultado.value = (f'voce ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcula}')
                    else:
                        contribuicao_diferente = contribuicao - 35
                        ano_atual = datetime.today().year
                        data_prevista = ano_atual - contribuicao_diferente
                        txt_resultado.value = (f'voce ja pode se aposentar.\n'
                                               f'Valor estimado para ser recebido R$ {data_prevista}')


            page.update()
            page.go('/Pagina')

        except ValueError as e:
            txt_resultado.value = 'Por favor digite só numero inteiro'
            page.update()

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Tela inicial"), bgcolor=Colors.BLACK),
                    ft.Image(src='img_1.png'),
                    ElevatedButton(text="Regras", on_click=lambda _: page.go("/Regras")),
                    ElevatedButton(text="Simulação", on_click=lambda _: page.go("/Simulação")),
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                bgcolor='#44803F',
            )
        )

        if page.route == "/Regras":
            page.views.append(
                View(
                    "/Regras",
                    [
                        AppBar(title=Text("Tela sobre as regras"), bgcolor=Colors.BLACK),
                        Text(value=f'\nAposentadoria por Idade:\n\n'

                                   f'Homens: 65 anos de idade e pelo menos 15 anos de contribuição.\n'
                                   f'Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n\n'
                                   f'\nAposentadoria por Tempo de Contribuição:\n\n'
                                   f'Homens: 35 anos de contribuição.\n'
                                   f'Mulheres: 30 anos de contribuição.\n\n'
                                   f'\nValor Estimado do Benefício:\n\n'
                                   f'O valor da aposentadoria será uma média de 60% Valor Estimado do Benefício: '
                                   f' O valor da aposentadoria será uma média de 60% da média salarial informada,'
                                   f' acrescido de 2% por ano que exceder o tempo mínimode contribuição.'),
                    ],
                    bgcolor='#44803F',
                )  # INDIGO_500
            )

        elif page.route == "/Simulação":
            page.views.append(
                View(
                    "/Simulação",
                    [
                        AppBar(title=Text("Tela de simulação "), bgcolor=Colors.BLACK),
                        idade_atual,
                        genero,
                        tempo_contribuicao,
                        categoria_aposentadoria,
                        salario,
                        ElevatedButton(text="Enviar", on_click=lambda _:verificar_aposentadoria(e)),

                    ],
                    bgcolor='#44803F',
                )
            )
        elif page.route == "/Pagina":
            page.views.append(
                View(
                    "/Pagina",
                    [
                        AppBar(title=Text("Resposta"), bgcolor=Colors.BLACK),
                        Text(value=f'Idade "{idade_atual.value}"'),
                        Text(value=f'Genero "{genero.value}"'),
                        Text(value=f'Contribuição"{tempo_contribuicao.value}"'),
                        Text(value=f'Categoria "{categoria_aposentadoria.value}"'),
                        Text(value=f'Salario "{salario.value}"'),
                        txt_resultado,
                    ],
                    bgcolor='#44803F',
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    txt_resultado = ft.Text()
    idade_atual = ft.TextField(label='Idade',focused_border_color=Colors.BLACK,)
    tempo_contribuicao = ft.TextField(label='Contribuição', focused_border_color=Colors.BLACK)  # hint_text : exemplo de algo
    salario = ft.TextField(label='Salario', focused_border_color=Colors.BLACK)
    salario1 = ft.TextField(label='Salario',focused_border_color=Colors.BLACK)# hint_text : exemplo de algo

    genero = ft.Dropdown(label='Genero',focused_border_color=Colors.BLACK,
                         width=page.window.width,
                         options=[Option(key='Masculino', text='Masculino'), Option(key='Fem', text='Feminino')],

    )
    categoria_aposentadoria = ft.Dropdown(
                            label='Categoria da Aposentadoria',focused_border_color=Colors.BLACK,
                            width=page.window.width,
                            options=[Option(key='idade', text='Aposentadoria por Idade'),
                                     Option(key='Aposentadoria por Tempo de Contribuição', text='Aposentadoria por Tempo de Contribuição')],

    )


    page.on_route_change = gerenciar_rotas
    page.go(page.route)
    page.on_view_pop = voltar



ft.app(main)
