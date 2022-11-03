from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        1,
        "produto",
        "empresa",
        "2022-01-01",
        "2023-01-01",
        "123654",
        "instru_armazem"
    )

    assert produto.__str__() == "O produto produto fabricado em 2022-01-01" \
        " por empresa com validade até 2023-01-01" \
        " precisa ser armazenado instru_armazem."
