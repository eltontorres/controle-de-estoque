from flet import Text, TextField, TextAlign, IconButton, Row, icons, MainAxisAlignment, DataColumn, DataTable, Tabs, Tab, Column, DataCell, DataRow, ScrollMode, OutlinedButton

txt_code = TextField(value="", border="none", read_only=True)
txt_date = TextField(value="", border="none", read_only=False)
txt_produto = TextField(value="", border="none", read_only=False)
txt_cod_bar = TextField(value="", border="none", read_only=False)
txt_descricao = TextField(value="", border="none", read_only=False)
txt_custo = TextField(value="", border="none", read_only=False)
txt_venda = TextField(value="", border="none", read_only=False)
txt_quantidade = TextField(value="", border="none", read_only=False)

txt_busca = TextField(
    label="Buscar", text_align=TextAlign.RIGHT, height=45, expand=1)

btn_add = OutlinedButton("Adicionar", icon=icons.ADD)
btn_edit = OutlinedButton("Editar", icon=icons.EDIT, disabled=True)
btn_save = OutlinedButton("Salvar", icon=icons.SAVE,  disabled=True)
btn_delete = OutlinedButton("Apagar",icon=icons.DELETE, )

btn_search = IconButton(icon=icons.SEARCH)

btn_cadastro = Row(
    [
        btn_add,
        btn_save,
        btn_edit,
        btn_delete
    ],
    alignment=MainAxisAlignment.SPACE_AROUND
)
brr_busca = Row(
    [
        txt_busca,
        btn_search
    ]
)

list_prod = []

table_prod = DataTable(
    columns=[
        #codigo, data, produto, barra, descricao, custo, venda, quantidade
        DataColumn(Text("Código")),
        DataColumn(Text("Data")),
        DataColumn(Text("Nome")),
        DataColumn(Text("Código de Barra")),
        DataColumn(Text("Descrição")),
        DataColumn(Text("Preço de Custo")),
        DataColumn(Text("Preço de Venda")),
        DataColumn(Text("Quantidade")),
    ],
    rows=list_prod,
    width=1000,
    show_checkbox_column=True

)

tab = Column([btn_cadastro, table_prod, brr_busca])