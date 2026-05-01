import model

def adicionar_nota(texto:str) -> bool:
    if texto:
        model.salvar_no_banco(texto)
        return True
    return False

def listar_notas() -> list:
    return model.ler_do_banco()
