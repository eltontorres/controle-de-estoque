from flet import Page, app, Banner, colors, Icon, TextButton, InputBorder
from componets import *
from database import *

def main(page: Page):
    db = recuperando_dados()

    def map_dict(item):
        item_dict = {
            'codigo': item[0],
            'data': item[1],
            'produto': item[2],
            'barra': item[3],
            'descricao': item[4],
            'custo': item[5],
            'venda': item[6],
            'quantidade': item[7]
        }

        return item_dict
    dict_db = [map_dict(item) for item in db]

    print(dict_db)
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

    selecteds = {}

    def delete(e):
        btn_add.disabled = False
        btn_edit.disabled = True
        btn_save.disabled = True
        btn_delete.disabled = True

        for item in selecteds:
            if selecteds[item] == 'true':
                remover_produto(item)

        db = recuperando_dados()
        load_data(db)
        page.update()

    def selected(e):
        e.control.selected = not e.control.selected

        selecteds.update({e.control.cells[0].content.value: e.data})

        status = [True if selecteds[item] == "true" else False for item in selecteds]

        global row_selected
        row_selected = []
        
        for index, linha in enumerate(table_prod.rows):
            if linha.selected == True:
                row_selected.append(index)
        print(row_selected)

        if status.count(True) == 1:
            btn_edit.disabled=False
            btn_delete.disabled=False
        else:
            btn_edit.disabled=True
            btn_save.disabled=True

        if status.count(True) == 0:
            btn_add.disabled=False
            btn_delete.disabled=True
        else:
            btn_add.disabled=True
        page.update()

    def load_data(db):
        db = recuperando_dados()
        list_prod.clear()
        dict_db = [map_dict(item) for item in db]

        for i, linha in enumerate(dict_db):
            list_prod.append(
                DataRow(
                    #codigo, data, produto, barra, descricao, custo, venda, quantidade
                    cells=[
                        DataCell(TextField(value=linha['codigo'], border="none", read_only=True)),
                        DataCell(TextField(value=linha['data'], border="none", read_only=True)),
                        DataCell(TextField(value=linha['produto'], border="none", read_only=True)),
                        DataCell(TextField(value=linha['barra'], border="none", read_only=True)),
                        DataCell(TextField(value=linha['descricao'], border="none", read_only=True)),
                        DataCell(TextField(value=linha['custo'], border="none", read_only=True)),
                        DataCell(TextField(value=linha['venda'], border="none", read_only=True)),
                        DataCell(TextField(value=linha['quantidade'], border="none", read_only=True)),
                    ],
                    on_select_changed=selected,
                    selected=False
                )
            )
        page.update()

    def add(e):
        btn_add.disabled = True
        btn_save.disabled = False
        list_prod.append(
                DataRow(
                    #codigo, data, produto, barra, descricao, custo, venda, quantidade
                    cells=[
                        DataCell(txt_code),
                        DataCell(txt_date),
                        DataCell(txt_produto),
                        DataCell(txt_cod_bar),
                        DataCell(txt_descricao),
                        DataCell(txt_custo),
                        DataCell(txt_venda),
                        DataCell(txt_quantidade),
                    ],
                    on_select_changed=selected,
                    selected=True
                )
            )
        page.update()

    def edit(e):
        btn_edit.disabled = True
        btn_save.disabled=False
        for i in range(len(table_prod.rows[0].cells)):
            table_prod.rows[row_selected[0]].cells[i].content.read_only = False
        page.update()

    def save(e):
        btn_add.disabled = False
        btn_save.disabled = True
        btn_edit.disabled=True
        btn_delete.disabled=True

        selecteds.clear()

        list_item =[]
        for item in table_prod.rows[0].cells:
            list_item.append(item.content.value)

        item = map_dict(list_item)
        print(item)

        if table_prod.rows[row_selected[0]].cells[0].content.value != "":
            codigo = table_prod.rows[row_selected[0]].cells[0].content.value
            print(codigo, item['data'])
            atualizar_estoque(codigo, 'data', table_prod.rows[row_selected[0]].cells[1].content.value)
            
            #item = map_dict(list_item)
        

        #adicionar_produto(item)

        txt_date.value, txt_produto.value, txt_cod_bar.value, txt_descricao.value, txt_custo.value, txt_venda.value, txt_quantidade.value = "", "", "", "", "", "", ""

        load_data(db)



    # configuração da função dos botões e textos
    btn_add.on_click = add
    btn_edit.on_click = edit
    btn_save.on_click = save
    btn_delete.on_click = delete

    load_data(db)
    page.add(tab)


app(target=main)
