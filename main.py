from flet import Page, app, Banner, colors, Icon, TextButton
from componets import *
from database import *


def main(page: Page):
    page.title = "Controle de Estoque"

    # definição das funções

    def fecha_banner(e):
        page.banner.open = False
        page.update()

    page.banner = Banner(
        content=Text(
            value='Todos os campos precisam ser preenchidos!', color=colors.BLACK),
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color=colors.RED_400,
            size=40
        ),
        actions=[TextButton('Entendi', on_click=fecha_banner)]
    )

    def delete(e):
        remover_produto(e.control.data)
        load_data()
        page.update()

    def load_data():
        db = recuperando_dados()
        list_prod.clear()

        for i, table in enumerate(db):
            list_prod.append(
                DataRow(
                    cells=[
                        DataCell(TextField(value=table[0], border="none")),
                        DataCell(Text(table[1])),
                        DataCell(Text(table[2])),
                        DataCell(Text(table[3])),
                        DataCell(IconButton(
                            icon=icons.DELETE, data=db[i][0], on_click=lambda e:delete(e)))
                    ]
                )
            )

    def add(e):
        txt_produto.read_only = False
        txt_date.read_only = False
        txt_cod_bar.read_only = False
        txt_descricao.read_only = False
        txt_custo.read_only = False
        txt_venda.read_only = False
        txt_quantidade.read_only = False

        page.update()

    def save(e):
        if txt_date.value == '' or txt_produto.value == '' or txt_cod_bar.value == '' or txt_descricao.value == '' or txt_custo.value == '' or txt_venda.value == '' or txt_quantidade.value == '':
            page.banner.open = True
            page.update()
            return

        item = {
            'data': txt_date.value,
            'produto': txt_produto.value,
            'barra': txt_cod_bar.value,
            'descricao': txt_descricao.value,
            'custo': txt_custo.value,
            'venda': txt_venda.value,
            'quantidade': txt_quantidade.value
        }
        adicionar_produto(item)

        txt_date.value, txt_produto.value, txt_cod_bar.value, txt_descricao.value, txt_custo.value, txt_venda.value, txt_quantidade.value = "", "", "", "", "", "", ""

        load_data()

        page.update()

    # configuração da função dos botões e textos
    btn_add.on_click = add
    btn_save.on_click = save
    btn_delete.on_click = delete

    load_data()
    page.add(tab)


app(target=main)
