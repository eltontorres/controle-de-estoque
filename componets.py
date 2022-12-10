from flet import Text, TextField, TextAlign, IconButton, Row, icons, MainAxisAlignment, DataColumn, DataTable, Tabs, Tab, Column, DataCell, DataRow, ScrollMode

txt_code = Text(height=45, expand=2, text_align=TextAlign.LEFT)
txt_date = TextField(label="Data de Cadastro",
                     text_align=TextAlign.RIGHT, height=45, expand=1, read_only=True)
txt_produto = TextField(label="Nome", height=45, expand=2,
                        text_align=TextAlign.LEFT, read_only=True)
txt_cod_bar = TextField(label="Código de Barras",
                        text_align=TextAlign.RIGHT, height=45, expand=3, read_only=True)

txt_descricao = TextField(
    label="Descrição", text_align=TextAlign.LEFT, height=45, expand=1, read_only=True)

txt_custo = TextField(label="Preço de Custo",
                      text_align=TextAlign.RIGHT, height=45, expand=1, read_only=True)
txt_venda = TextField(label="Preço de Venda",
                      text_align=TextAlign.RIGHT, height=45, expand=1, read_only=True)

txt_quantidade = TextField(label="Qdt. no quantidade",
                           text_align=TextAlign.RIGHT, height=45, expand=1, read_only=True)

txt_busca = TextField(
    label="Buscar", text_align=TextAlign.RIGHT, height=45, expand=1)

btn_add = IconButton(icon=icons.ADD)
btn_save = IconButton(icon=icons.SAVE)
btn_delete = IconButton(icon=icons.DELETE)

btn_search = IconButton(icon=icons.SEARCH)

cadastro = [
        Row(
            [
                txt_code,
                txt_date,
                txt_produto,
                txt_cod_bar
            ],
            # width=page.window_width
        ),
        Row(
            [
                txt_descricao
            ],
            # width=page.window_width
        ),
        Row(
            [
                txt_custo,
                txt_venda
            ],
            width=400
        ),
        Row(
            [
                txt_quantidade
            ],
            width=180
        )
    ]

btn_cadastro = Row(
    [
        btn_add,
        btn_save,
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
        DataColumn(Text("Código")),
        DataColumn(Text("Nome")),
        DataColumn(Text("Preço"), numeric=True),
        DataColumn(Text("Quantidate"), numeric=True),
        DataColumn(IconButton(icon=icons.ADD))
    ],
    rows=list_prod,
    width=800

)

tab = Tabs(
    selected_index=0,
    animation_duration=300,
    expand=1,
    tabs=[
        Tab(
            text="Listagem",
            content=Column(
                [table_prod, brr_busca],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                scroll=ScrollMode.AUTO
            )
        ),
        Tab(
            text="Dados",
            content=Column(
                [Column(cadastro, expand=1), btn_cadastro],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        )
    ]
)
