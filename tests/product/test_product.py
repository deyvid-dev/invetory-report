from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "produto",
        "empresa",
        "2022-01-01",
        "2023-01-01",
        "123654",
        "instru_armazem"
    )

    assert produto.id == 1
    assert produto.nome_do_produto == "produto"
    assert produto.nome_da_empresa == "empresa"
    assert produto.data_de_fabricacao == "2022-01-01"
    assert produto.data_de_validade == "2023-01-01"
    assert produto.numero_de_serie == "123654"
    assert produto.instrucoes_de_armazenamento == "instru_armazem"
