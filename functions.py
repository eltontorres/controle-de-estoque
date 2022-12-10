from componets import *
from database import recuperando_dados, remover_produto


def load_data():
    db = recuperando_dados()
    list_prod.clear()

    for i, table in enumerate(db):
        list_prod.append(
            DataRow(
                cells=[
                    DataCell(Text(table[0])),
                    DataCell(Text(table[1])),
                    DataCell(Text(table[2])),
                    DataCell(Text(table[3])),
                    DataCell(IconButton(icon=icons.DELETE, data=db[i][0], on_click=lambda e:remover_produto(e.control.data)))
                ]
            )
        )
